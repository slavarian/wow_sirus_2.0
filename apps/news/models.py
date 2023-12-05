from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class News(models.Model):
    title = models.CharField(
        verbose_name='Заголовок',
        max_length=100)
    content = models.TextField(
        verbose_name="Содержание",
    )
    date_create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пост создан',
    )

    def __str__(self):
        return self.title
