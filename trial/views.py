from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import auth_login
from django.shortcuts import redirect


def index(request):


    return render(request, './base_generic.html' )

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return auth_login(request)