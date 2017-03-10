from django.contrib import admin
from .models import *
# Register your models here.
from blog.models import SEO


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
    inlines = ( SEO,)
    fieldsets = (
        ('Основное', {'fields': ('title', 'start','end','tags','featured_image','profile_image','location')}),
        ('Описание', {'fields': ('allow_comments', 'description')}),
        ('Дополнительная информация', {'fields': ('internet_available', 'take_computer', 'site','value')}),
    )


    class Media:
        js = ['js/FB_CKEditor.js',
              'js/ckeditor.js']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Event, EventAdmin)
admin.site.register(EventLocation)
