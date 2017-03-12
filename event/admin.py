from django.contrib import admin
from .models import *
# Register your models here.
from blog.models import SEO
from django_ymap.admin import YmapAdmin


class SEO(admin.StackedInline):
    model = SEO
    extra = 0
    fields = (
        'soe_description',
        'key_words',
    )
    show_change_link = True


class EventAdmin(admin.ModelAdmin):
    model = Event
    inlines = (SEO,)
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Основное', {'fields': (
            'title', 'sub_title', 'slug', 'start', 'end', 'tags', 'type', 'featured_image', 'profile_image',
            'location')}),
        ('Описание', {'fields': ('allow_comments', 'description')}),
        ('Дополнительная информация', {'fields': ('internet_available', 'take_computer', 'site', 'value')}),
    )

    class Media:
        js = ['js/FB_CKEditor.js',
              'js/ckeditor.js']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Event, EventAdmin)


class RecordAdmin(YmapAdmin, admin.ModelAdmin):
    pass


admin.site.register(EventLocation, RecordAdmin)
