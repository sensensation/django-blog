from re import S
from tabnanny import verbose
from django.db import models
from django import forms
from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    published = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name="Опубликовано"
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
    
    #метод, позволяющий видеть название рубрики в Django admin
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Рубрики"
        verbose_name = "Рубрика"
        ordering = ["name"]

class Message(models.Model):
    slug_message = models.SlugField(max_length=150, blank=False, unique=True)
    message = models.TextField(('Сообщение'))
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')
    is_update = models.BooleanField(default=False, verbose_name='Редактировано')
    date_update = models.DateTimeField(null=True, blank=True)
    test = models.CharField(max_length=2000, blank=True, null=True)
