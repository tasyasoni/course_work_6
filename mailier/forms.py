from django import forms
from django.forms import ModelForm
from django.urls import reverse_lazy
from mailier.models import Client, Mailing, Msg


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'comment',)
        success_url = reverse_lazy('mailier:client_list')


class MailingForm(ModelForm):
   class Meta:
        model = Mailing
        fields = ('start_mail', 'end_mail', 'period_mail', 'status_mail', 'clients',)


class MsgForm(ModelForm):
   class Meta:
        model = Msg
        fields = ('header_mail', 'body_mail',)