from django.shortcuts import render
from django.urls import reverse

from mailier.forms import ClientForm
from mailier.models import Client
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('mailier:clients_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('mailier:clients_list')


class ClientListView(ListView):
    model = Client


def home(request):
    context = {
        'title': 'Mailier_store'
    }
    return render(request, 'mailier/home.html', context)