from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy
# Create your views here.

class SnacksListView(ListView):
    template_name = 'snack_list.html'
    model = Snack
    context_object_name = "data"

class SnackDetailsView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'snacks_create.html'
    model = Snack
    fields=['title','purchaser','description']


class SnackUpdateView(UpdateView):    
    template_name = 'snacks_update.html'
    model = Snack
    fields=['title','purchaser','description']
    # success_url = reverse_lazy('snacks')

class SnackDeleteView(DeleteView):
    template_name = 'snacks_delete.html'
    model = Snack
    success_url = reverse_lazy('snacks')