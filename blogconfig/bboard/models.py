from re import S
from tabnanny import verbose
from django.db import models

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    content = models.TextField(null=True, blank=True, verbose_name="Описание")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Опубликовано")
    image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name="Картинка") 
    rubric = models.ForeignKey("Rubric", null=True, on_delete=models.PROTECT, verbose_name="Рубрика")

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


