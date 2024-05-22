from django.shortcuts import render
from django.views.generic import ListView, DetailView
from polls.models import Cigarette

class CigaretteListView(ListView):
    model = Cigarette
    template_name = 'cigarette_list.html'
    context_object_name = 'cigarette_list'

class CigaretteDetailView(DetailView):
    model = Cigarette
    template_name = 'cigarette_detail.html'
    context_object_name = 'cigarette_detail'
