from django.shortcuts import redirect
class requireLogin:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Allow authenticated OR guests if a radio authorized them
        if not ("userid" in request.session or "connection" in request.session):
            return redirect("/user/login")
        response = self.get_response(request)
        return response 
