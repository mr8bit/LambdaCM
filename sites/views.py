from django.shortcuts import render
from blog.models import *
from event.models import *
# Create your views here.
from django.template.response import TemplateResponse


def article_list(request):
    context = {}
    context['articls'] = Article.objects.all()
    return TemplateResponse(request, "frontend/blog/list.html", context)


def event_list(request):
    context = {}
    context['events'] = Event.objects.all()
    return TemplateResponse(request, "frontend/event/list.html", context)


def event(request, slug):
    context = {}
    context['event'] = Event.objects.get(slug=slug)
    date = abs( context['event'].end - context['event'].start)
    context['time'] = date.seconds/60
    return TemplateResponse(request, "frontend/event/event.html", context)