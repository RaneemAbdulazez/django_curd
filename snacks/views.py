from django.db import models
from django.shortcuts import render
from django.views.generic import ListView ,TemplateView ,DeleteView ,DetailView ,CreateView
from django.views.generic.edit import UpdateView
from .models import Snack
from django.urls import reverse_lazy
# Create SnackListView that extends appropriate generic view
# associated url path is an empty string

class SnackListView(ListView):
    template_name='snack_list.html'
    # queryset=Snack.objects.all()
    model=Snack

# # Create SnackDetailView that extends appropriate generic view
# # associated url path is <int:pk>/
class SnackDetailView(DetailView):
    template_name='snack_detail.html'
    model=Snack

# # Create SnackCreateView that extends appropriate generic view
# # associated url path is create/

class SnackCreateView(CreateView):
    template_name='snack_create.html'
    model=Snack
    fields=['title']

# Create SnackUpdateView that extends appropriate generic view
# associated url path is <int:pk>/update/
class SnackUpdateView(UpdateView):
    template_name='snack_update.html'
    model=Snack
    fields=["title","purchaser","describtion"]

# # Create SnackDeleteView that extends appropriate generic view
# # associated url path is <int:pk>/delete/

class SnackDeleteView(DeleteView):
    template_name='snack_delete.html'
    model=Snack
    success_url = reverse_lazy("list_view")

