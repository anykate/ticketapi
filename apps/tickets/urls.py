from django.urls import path, include
from . import views
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('tickets', views.TicketViewSet)
router.register('category', views.CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls), name='api_urls'),
    path('rest-api/', include('rest_framework.urls'), name='rest_api_urls'),
]
