from django.shortcuts import render
from django.views.generic import (View, TemplateView, ListView, DetailView,
                                    CreateView, UpdateView, DeleteView)
from simple_app import models
from django.core.urlresolvers import reverse_lazy

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


class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name','principal')  #Location may not be updated
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("simple_app:list")