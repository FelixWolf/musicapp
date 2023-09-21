# Generated by Django 4.2.2 on 2023-09-21 20:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rendition',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('duration', models.FloatField()),
                ('segmentLength', models.FloatField()),
                ('_segments', models.BinaryField(max_length=65535)),
                ('score', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rendition_creator', to='user.user')),
                ('modifier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rendition_modifier', to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='RenditionVote',
            fields=[
                ('id', models.PositiveBigIntegerField(primary_key=True, serialize=False)),
                ('vote', models.SmallIntegerField()),
                ('rendition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rendition.rendition')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]