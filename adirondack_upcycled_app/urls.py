from django.urls import path
from . import views

urlpatterns = [
    path('listings/', views.ListingView.as_view(), name='listings_all'),
]