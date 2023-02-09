# Generated by Django 4.1.6 on 2023-02-09 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adirondack_upcycled_app', '0015_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='mainPhoto',
            field=models.ImageField(upload_to='staticfiles/images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo1',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo2',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo3',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/images/'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/images/'),
        ),
    ]