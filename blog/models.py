from django.db import models
from colorfield.fields import ColorField
from meta.models import ModelMeta
from ckeditor_uploader.fields import RichTextUploadingField
from filebrowser.fields import FileBrowseField
from LambdaCM import settings


class Article(ModelMeta, models.Model):
    title = models.CharField(max_length=300, verbose_name="Название")
    sub_title = models.CharField(max_length=300, verbose_name="Слоган")
    short_description = RichTextUploadingField(verbose_name="Короткое описание")
    description = RichTextUploadingField(verbose_name="Статья")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор", null=True, blank=True)
    tags = models.ManyToManyField("Tag", verbose_name="Тэги")
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_updated = models.DateTimeField(auto_now=True)
    main_image = FileBrowseField("Главное изображение", max_length=200, directory="images/", blank=True, null=True)
    post_in_vk = models.BooleanField(verbose_name="Постить в вк?", default=False)
    post_in_twitter = models.BooleanField(verbose_name="Постить в твиттер?", default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    metadata = {
        'title': 'name',
        'description': 'abstract',
    }


class Tag(models.Model):
    name = models.CharField(max_length=300, verbose_name="Название")
    color = ColorField(default='#FF0000')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


from event.models import Event


class SEO(models.Model):
    soe_description = models.TextField(verbose_name="Seo Описание")
    key_words = models.TextField(verbose_name="Ключ слова")
    article = models.OneToOneField(Article, related_name='articles', null=True, blank=True)
    event = models.OneToOneField(Event, related_name="events", null=True, blank=True)

    def __str__(self):
        if self.article:
            return "SEO для статьи " + self.article.title
        else:
            return "SEO для мероприятия" + self.event.title

    class Meta:
        verbose_name = "SEO"
        verbose_name_plural = "SEO"
