from django.conf.urls import url, include
from migrate import views
from rest_framework import routers
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from migrate.views import GeoViewSet
router = routers.DefaultRouter()
router.register('geo/search', views.GeoViewSet) # User CRUD
router.register('sector/search', views.SectorsViewSet) # User Requirement CRUD




urlpatterns = [
    url(r'^', include(router.urls)),
#    url(r'^geo', GeoViewSet)
#     url(r'^', GeoViewSet.as_view({'get': 'list'}), name='base'),
]