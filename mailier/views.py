from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.forms import inlineformset_factory
from mailier.forms import ClientForm, MailingForm, MsgForm
from mailier.models import Client, Mailing, Msg, Logfile
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('mailier:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm

    def get_success_url(self):
        return reverse('mailier:client_list')


class ClientListView(ListView):
    model = Client

    def get_success_url(self):
        return reverse('mailier:client_list')


class MailingCreateView(CreateView):
    model = Mailing
    form_class = MsgForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MsgFormset = inlineformset_factory(Msg, Mailing, extra=1, form=MailingForm)
        if self.request.method == 'POST':
            context_data['formset'] = MsgFormset(self.request.POST)
        else:
            context_data['formset'] = MsgFormset()
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mailier:mailing_list')




class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MsgForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        MsgFormset = inlineformset_factory(Msg, Mailing, extra=1, form=MailingForm)

        if self.request.method == 'POST':
            context_data['formset'] = MsgFormset(self.request.POST)
        else:
            context_data['formset'] = MsgFormset()

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('mailier:mailing_list')


class MailingListView(ListView):
    model = Mailing

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        context_data['all'] = context_data['object_list'].count()
        context_data['active'] = context_data['object_list'].filter(status_mail=Mailing.STARTED).count()

        mailing_list = context_data['object_list'].prefetch_related('clients')
        clients = set()
        [[clients.add(client.email) for client in mailing.clients.all()] for mailing in mailing_list]
        context_data['clients_count'] = len(clients)
        return context_data

    def get_success_url(self):
        return reverse('mailier:home')



class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailier:mailing_list')


class LogfileListView(ListView):
    model = Logfile

    def get_success_url(self):
        return reverse('mailier:mailing_list')

def home(request):
    context = {
        'title': 'Mailier_store'
    }
    return render(request, 'mailier/home.html', context)




