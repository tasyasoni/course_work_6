from django.forms import ModelForm

from mailier.models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email', 'comment',)
