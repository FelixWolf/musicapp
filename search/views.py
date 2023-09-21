from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.core.paginator import Paginator
from django.db.models import Q, F, Value, CharField
from collections import namedtuple
from track.models import Track
from artist.models import Artist
from album.models import Album
from user.models import User

searchables = {
    "track": {
        "table": Track,
        "fields": ["title"],
        "sort": "created"
    },
    "album": {
        "table": Album,
        "fields": ["title"],
        "sort": "created"
    },
    "artist": {
        "table": Artist,
        "fields": ["name"],
        "sort": "created"
    },
    "user": {
        "table": User,
        "fields": ["username", "displayname"],
        "sort": "registered"
    }
}

class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

@never_cache
def search(request):
    types = request.GET.getlist("type[]")
    if not types:
        types = ['track', 'album', 'artist']
    
    qs = []
    columns = {}
    for cat in types:
        if cat in searchables:
            filters = None
            for field in searchables[cat]["fields"]:
                search = Q(**{
                    field+"__icontains": request.GET.get("query", "")
                })
                if filters == None:
                    filters = search
                else:
                    filters |= search
                columns[field] = Value("", CharField())
            
            qs.append((
                searchables[cat]["table"].objects.filter(filters).annotate(**{"_SORT": F(searchables[cat]["sort"])}).values_list("id","_SORT",*searchables[cat]["fields"]),
                searchables[cat]["fields"],
                cat
            ))
    
    results = []
    if qs:
        qs = list(map(
            lambda x: x[0].annotate(**{k:v for k,v in columns.items() if not k in x[0]._fields}, **{cat:Value(x[2], CharField())}),
            qs
        ))
        results = qs[0].union(*qs[1:]).order_by("_SORT").all()
    
    paginator = Paginator(results, 25)
    
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    page_obj.adjusted_elided_pages = paginator.get_elided_page_range(page_number)
    page_obj.object_list = list(page_obj.object_list)
    for i in range(len(page_obj)):
        fields = searchables[page_obj.object_list[i][-1]]["fields"]
        page_obj.object_list[i] = AttrDict({
            "type": page_obj.object_list[i][-1],
            "id": page_obj.object_list[i][0],
            "date": page_obj.object_list[i][1],
            **{
                fields[_]: page_obj.object_list[i][_+2] for _ in range(len(fields))
            }
        })
    
    return render(request, "search.htm", {
        "query": request.GET.get("query", ""),
        "page_obj": page_obj
    })