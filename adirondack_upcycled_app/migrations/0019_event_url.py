# Generated by Django 4.1.6 on 2023-02-16 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adirondack_upcycled_app', '0018_alter_listing_mainphoto_alter_listing_photo1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
