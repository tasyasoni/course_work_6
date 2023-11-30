from django.forms import ModelForm

from mailier.models import Client, Mailing


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'comment',)


class MailingForm(ModelForm):
    class Meta:
        model = Mailing
        fields = ('time_mail', 'period_mail', 'status_mail','clients',)