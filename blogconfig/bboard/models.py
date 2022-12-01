from re import S
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


class Bb(models.Model):
    author = models.ForeignKey(User, null= True,on_delete=models.CASCADE, verbose_name="Пользователь")
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Опубликовано"
    )
    image = models.ImageField(
        upload_to="images",
        null=True,
        blank=False,
        verbose_name="Картинка",
        default="images/default_pic.jpg",
    )
    rubric = models.ForeignKey(
        "Rubric", null=True, on_delete=models.PROTECT, verbose_name="Рубрика"
    )

    class Meta:
        verbose_name_plural = "Посты"
        verbose_name = "Пост"
        ordering = ["-published"]


class Rubric(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название", db_index=True)

    # метод, позволяющий видеть название рубрики в Django admin
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = "Рубрика"
        ordering = ["name"]
