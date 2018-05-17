from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from simple_app import models

# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = "schools"
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = "school_detail"
    model = models.School
    template_name = 'simple_app/school_detail.html'
