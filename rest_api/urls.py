from django.urls import path
from django.conf.urls import url

from . import views 

urlpatterns = [
    # path('', views.LocationsView.as_view(), name='locations-post'),
    # path('<int:location_id>/', views.LocationsView.as_view(), name='locations-post'),
    # url(r'^$', views.LocationsList.as_view(), name='locations-list'),
    # url(r'^weather/$', views.LocationsList.as_view(), name='locations-list'),

    path('', views.LocationList.as_view(), name='locations-list'),
    path('<int:pk>/', views.LocationDetail.as_view(), name='locations-detail'),
]