from django.urls import path, include
from django.contrib import admin
from . import views
from .views import SignUpView
from django.contrib.auth import views as auth_views
from django.conf import settings  # для статик файлов
from django.conf.urls.static import static # для статик файлов

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('play_game/', views.playgame, name = "play_game")
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#smth added