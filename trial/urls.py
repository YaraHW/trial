from django.urls import path, include
from django.contrib import admin
from . import views
from .views import SignUpView
from .views import custom_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),


    path('accounts/login/', custom_login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]