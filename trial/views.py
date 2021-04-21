from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def test(request):
    return HttpResponse("TEST")    # TEST - текст отображенный по url  http://localhost:8100/test

def trial(request):
    return HttpResponse("TRIAL")