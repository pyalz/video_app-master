# Generated by Django 4.1.4 on 2022-12-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_vidstream_playlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vidstream',
            name='playlist',
            field=models.TextField(blank=True, max_length=60),
        ),
    ]
