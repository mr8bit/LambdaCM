from django.template import RequestContext
from django.shortcuts import render_to_response
from blog.models import Article
from event.models import Event


def index(request):
    events_list = Event.objects.all()
    articles = Article.objects.all()
    return render_to_response('frontend/index.html', {'events_list': events_list,
                                                      'articles': articles})


def events(request):
    events_list = Event.objects.all()
    return render_to_response('frontend/event/list.html', {'events_list': events_list})


def blog(request):
    articles = Article.objects.all()
    return render_to_response('frontend/blog/list.html', {'articles': articles})