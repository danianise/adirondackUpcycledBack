# Generated by Django 4.1.6 on 2023-02-09 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adirondack_upcycled_app', '0014_alter_listing_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=1, primary_key=True, serialize=False),
        ),
    ]
