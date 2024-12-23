from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('accounts/')),
    path('admin/', admin.site.urls),
    path('api/', include('members.urls')),  
    path('accounts/profile/', include('login.urls')),  
    path('accounts/', include('allauth.urls')),
]