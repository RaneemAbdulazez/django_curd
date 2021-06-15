from django.contrib import admin
from django.db import models
from django.shortcuts import render
from django.urls import path
from django.views.generic import ListView ,TemplateView ,DeleteView ,DetailView ,CreateView
from django.views.generic.edit import UpdateView
from .models import Snack
# Create SnackListView that extends appropriate generic view
# associated url path is an empty string

class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack

# # Create SnackDetailView that extends appropriate generic view
# # associated url path is <int:pk>/
class SnackDetailView(DetailView):
    template_name='snack_detail.html'
    model=Snack

# # Create SnackCreateView that extends appropriate generic view
# # associated url path is create/

# class SnackCreateView(CreateView):
#     template_name=''
#     model='Snack'

# # Create SnackUpdateView that extends appropriate generic view
# # associated url path is <int:pk>/update/
# class SnackUpdateView(UpdateView):
#     template_name=''
#     model='Snack'

# # Create SnackDeleteView that extends appropriate generic view
# # associated url path is <int:pk>/delete/

# class SnackUpdateView(DeleteView):
#     template_name=''
#     model='Snack'
