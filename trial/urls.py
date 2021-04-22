from django.urls import path
from django.contrib import admin
from django.contrib import auth
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('trial', views.trial, name='trial'),   #path('trial' - trial это сам url
    path('accounts/', include('django.contrib.auth.urls')),
]
