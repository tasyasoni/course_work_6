from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.forms import inlineformset_factory
from mailier.forms import ClientForm, MailingForm, MsgForm
from mailier.models import Client, Mailing, Msg
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
    form_class = MailingForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Mailing, Msg, form=MsgForm, extra=0)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
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
    form_class = MailingForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Mailing, Msg, form=MsgForm, extra=0)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
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


