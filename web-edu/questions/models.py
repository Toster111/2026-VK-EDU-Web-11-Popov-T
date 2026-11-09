from django.db import models

class User(models.Model):
    name = models.CharField(max_length=225)
    id_icon = models.IntegerField(null=True, blank=True) # Иконка, как в вашей таблице

    def __str__(self):
        return self.name

class Tag(models.Model): # Ваша таблица TEGS
    # Вместо ENUM используем CharField (текстовое поле).
    # unique=True не даст создать два одинаковых тега.
    name = models.CharField(max_length=50, unique=True)
    popularity = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Question(models.Model): # Объединяем QUESTIONS и QUESTIONS_LISTS
    header = models.TextField()
    title = models.TextField()

    # Связь "Многие к одному": У одного юзера много вопросов
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')

    # Связь "Многие ко многим": У одного вопроса много тегов, один тег у многих вопросов
    tags = models.ManyToManyField(Tag, related_name='questions')

    date_create = models.DateField(auto_now_add=True) # Дата создастся сама
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.header
