from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.forms import inlineformset_factory
from blog.models import Blog
from mailier.forms import ClientForm, MailingForm, MsgForm, ModeratorMailingForm
from mailier.models import Client, Mailing, Msg, Logfile
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView


class ClientCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    permission_required = 'mailier.add_client'
    def get_success_url(self):
        return reverse('mailier:client_list')


class ClientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    permission_required = 'mailier.change_client'

    def get_success_url(self):
        return reverse('mailier:client_list')


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    permission_required = 'mailier.view_client'

    def get_success_url(self):
        return reverse('mailier:client_list')


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'mailier.add_mailing'


    def get_success_url(self):
        return reverse('mailier:mailing_list')




class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    permission_required = 'mailier.change_mailing'

    def get_form_class(self):
        user = self.request.user

        if user.is_staff:
            form_class = ModeratorMailingForm
        else:
            form_class = MailingForm
        return form_class

    def get_success_url(self):
        return reverse('mailier:mailing_list')


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    permission_required = 'mailier.view_mailing'


    def get_success_url(self):
        return reverse('mailier:home')



class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailier:mailing_list')
    permission_required = 'mailier.delete_mailing'


class MsgCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Msg
    form_class = MsgForm
    permission_required = 'mailier.add_msg'

    def get_success_url(self):
        return reverse('mailier:msg_list')


class MsgUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Msg
    form_class = MsgForm
    permission_required = 'mailier.change_msg'



    def get_success_url(self):
        return reverse('mailier:msg_list')


class MsgListView(LoginRequiredMixin, ListView):
    model = Msg
    permission_required = 'mailier.view_msg'

    def get_success_url(self):
        return reverse('mailier:home')


class MsgDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Msg
    success_url = reverse_lazy('mailier:Msg_list')
    permission_required = 'mailier.delete_msg'


class LogfileListView(ListView):
    model = Logfile

    def get_success_url(self):
        return reverse('mailier:mailing_list')

def home(request):
    qs = Mailing.objects.all()
    qc = Client.objects.all()
    bl = Blog.objects.all()



    context = {
        'title': 'Mailier_store',
        'all': qs.count(),
        'active': qs.filter(status_mail=Mailing.STARTED).count(),
        'unic_clients': qc.count(),
        'blog': bl.order_by('?')[:3]
    }

    return render(request, 'mailier/home.html', context)




