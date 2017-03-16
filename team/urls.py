import team.views
from django.conf.urls import include, url

urlpatterns = [
    url(r'^team/(?P<slug>[\w-]+)$', team.views.TeamView.as_view(), name='team'),
    url(r'^partner/(?P<slug>[\w-]+)$', team.views.PartnerView.as_view(), name='partner'),
    url(r'^project/(?P<slug>[\w-]+)$', team.views.ProjectView.as_view(), name='project'),
]
