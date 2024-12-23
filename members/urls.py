from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *


app_name = 'members'

router = DefaultRouter()
router.register(r'members', MemberViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
