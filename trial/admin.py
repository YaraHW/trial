from django.contrib import admin
from .models import Articles

admin.site.register(Articles) # регистрируем нашу табличку Articles чтоб видеть ее на сайте в админке