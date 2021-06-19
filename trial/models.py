from django.db import models

class Articles(models.Model): # Чтоб создать таблицу нужно юзать моделс, в таблице будет 4 параметра (заголовок, текст итд)
    title = models.CharField("Название", max_length=50, default="Пока что заголовок не придумали") # заголовок, max_length - длина заголовка не больше 50 символов, default - если ничего не вводишь то это по умолчанию высветится
    anons = models.CharField("Анонс", max_length=250) # в классе Charfield максимум возможных символов 250
    full_text = models.TextField("Статья") # Поэтому для статей юзаем класс TextField
    date = models.DateTimeField("Дата публикации") # Через этот класс можно указать дату и время

    def __str__(self):
        return self.title # Возврат в строковом представлении
