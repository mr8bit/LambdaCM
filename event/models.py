from django.db import models
from filebrowser.fields import FileBrowseField
from ckeditor_uploader.fields import RichTextUploadingField
from blog.models import Tag
from LambdaCM import settings

class EventLocation(models.Model):
    address = models.CharField("Адресс", max_length=500)
    name = models.CharField("Название", max_length=300, blank=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.address

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"


# Create your models here.
class Event(models.Model):
    title = models.CharField(verbose_name="Название", max_length=300)
    start = models.DateTimeField(verbose_name="Начало")
    end = models.DateTimeField(verbose_name="Окончание", blank=True, null=True)
    allow_comments = models.BooleanField(verbose_name="Открыть коменты?", default=True)
    location = models.ForeignKey('EventLocation', verbose_name="Местоположение")
    description = RichTextUploadingField(verbose_name="Статья")
    featured_image = FileBrowseField("Главное изображение", max_length=200, directory="event/", blank=True, null=True)
    profile_image = FileBrowseField("Изображение профиля", max_length=200, directory="event/", blank=True, null=True)
    tags = models.ForeignKey("blog.Tag", verbose_name="Тэги", default="")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ("-start",)


class AdditionInfo(models.Model):
    internet_available = models.BooleanField(verbose_name="Есть доступ к интернету")
    take_computer = models.BooleanField(verbose_name="Брать компьютер")
    site = models.URLField(verbose_name="Сайт мероприятия")
    value = models.CharField(verbose_name="Стоимость", max_length=300)
    event = models.OneToOneField("Event")

    def __str__(self):
        return "Доп. Информация для "  +  self.event.title

    class Meta:
        verbose_name = "Дополнительная информация"
        verbose_name_plural = "Дополнительная информация"
        ordering = ("-event",)
