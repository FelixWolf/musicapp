# Generated by Django 4.2.2 on 2023-09-21 20:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('album', '0001_initial'),
        ('artist', '0001_initial'),
        ('rendition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('artwork', models.UUIDField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('maturity', models.IntegerField(choices=[(None, '(Unrated)'), (13, 'General'), (21, 'Moderate'), (42, 'Adult')], null=True)),
                ('score', models.IntegerField(default=0)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='album.album')),
                ('artist', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='artist.artist')),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='track_creator', to='user.user')),
                ('modifier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modifier_modifier', to='user.user')),
                ('rendition', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='track_rendition', to='rendition.rendition')),
            ],
        ),
        migrations.CreateModel(
            name='TrackVote',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('vote', models.SmallIntegerField()),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='track.track')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'unique_together': {('track', 'user')},
            },
        ),
    ]
