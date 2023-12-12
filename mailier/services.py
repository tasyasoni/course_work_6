from django.utils import timezone
from django.conf import settings
from mailier.models import Mailing, Client, Msg
from django.core.mail import send_mail

def run_daily_mailing():
    mailings = Mailing.objects.filter(period_mail="Раз в день", status_mail="Создана")
    if mailings.exists():
        for mailing in mailings:
               send_mail(
                     subject=Msg.header_mail,
                     message=Msg.body_mail,
                     from_email=settings.EMAIL_HOST_USER,
                     recipient_list=[Client.email]
                   )
    else:
        print('нет таких рассылок')


