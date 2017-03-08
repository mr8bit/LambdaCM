from django.contrib import admin
from .models import *


class SEO(admin.StackedInline):
    model = SEO
    extra = 0
    fields = (
        'soe_description',
        'key_words',
    )
    show_change_link = True


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    fields = (
        'title', 'sub_title', 'post_in_vk', 'main_image', 'post_in_twitter', 'short_description', 'description', 'tags')
    inlines = (SEO,)

    class Media:
        js = ['js/FB_CKEditor.js',
              'js/ckeditor.js']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Article, ArticleAdmin)

admin.site.register(Tag)
