from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required  # стянули декоратор чтоб не было возможности открыть страницы без авторизации



def index(request):
    return render(request, './base_generic.html' )

@login_required
def playgame(request):
    return render(request, './play_game.html')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

