from django.forms import ModelForm
from django.urls import reverse_lazy
from mailier.models import Client, Mailing, Msg, Logfile

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'comment',)
        success_url = reverse_lazy('mailier:client_list')


class MailingForm(StyleFormMixin, ModelForm):
   class Meta:
        model = Mailing
        fields = ('start_mail', 'end_mail', 'period_mail', 'status_mail', 'clients', 'message',)


class ModeratorMailingForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Mailing
        fields = ('status_mail',)

class MsgForm(StyleFormMixin, ModelForm):
   class Meta:
        model = Msg
        fields = ('header_mail', 'body_mail',)


class LogfileForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Logfile
        fields = ('time_log_send', 'status_log', 'server_response',)