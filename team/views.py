from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from team.models import Partner, Project, Member
from django.views import generic


# Create your views here.

class PartnerView(generic.DetailView):
    model = Partner
    template_name = 'frontend/partner/partner.html'

class TeamView(generic.DetailView):
    pass

class ProjectView(generic.DetailView):
    pass