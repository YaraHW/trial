from django.urls import path, include
from django.contrib import admin
from . import views
from .views import SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),

    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),

    path('accounts/', include('django.contrib.auth.urls')),
]