from django.contrib import admin
from .models import Category, Listing, Event

admin.site.register(Category)
admin.site.register(Listing)
admin.site.register(Event)