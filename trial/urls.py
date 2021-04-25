from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('trial', views.trial, name='trial'),   #path('trial' - trial это сам url
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accountsregistration.urls')),   # url на страницу регистрации нового пользователя

]