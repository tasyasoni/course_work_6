from django.shortcuts import render
from django.urls import reverse, reverse_lazy

from mailier.forms import ClientForm, MailingForm
from mailier.models import Client, Mailing
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


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('mailier:clients_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm

    def get_success_url(self):
        return reverse('mailier:clients_list')


class MailingListView(ListView):
    model = Mailing

    def get_success_url(self):
        return reverse('mailier:home')



class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailier:mailing_list')


def home(request):
    context = {
        'title': 'Mailier_store'
    }
    return render(request, 'mailier/home.html', context)