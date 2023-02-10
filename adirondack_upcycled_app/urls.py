from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('categories/', views.CategoryView.as_view(), name='categories_all'),
    path('categories/<int:pk>', views.CategoryDetail.as_view(), name='category_detail'),

    path('listings/', views.ListingList.as_view(), name='listings_all'),
    path('listings/<int:pk>', views.ListingDetail.as_view(), name='listing_detail'),

    path('events/', views.EventView.as_view(), name='events_all'),
    path('events/<int:pk>', views.EventDetail.as_view(), name='event_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)