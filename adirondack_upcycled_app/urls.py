from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('listings/', views.ListingView.as_view(), name='listings_all'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)