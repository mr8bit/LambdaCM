from django.contrib import admin
from .models import *
# Register your models here.
from  blog.models import  SEO




class SEO(admin.StackedInline):
    model = SEO
    extra = 0
    fields = (
        'soe_description',
        'key_words',
    )
    show_change_link = True

class AdditionInfo(admin.StackedInline):
    model = AdditionInfo
    extra = 0
    show_change_link = True



class EventAdmin(admin.ModelAdmin):
    model = Event
    inlines = (AdditionInfo,SEO,)
    fields = (
        'title',
        'start',
        'end',
        'allow_comments',
        'location',
        'description',
        'featured_image',
        'profile_image',
        'tags',
    )

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()



admin.site.register(Event,EventAdmin)
admin.site.register(EventLocation)