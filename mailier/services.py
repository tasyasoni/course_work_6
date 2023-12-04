from django.utils import timezone
from django.conf import settings
from mailier.models import Mailing, Client, Msg
from django.core.mail import send_mail

def run_daily_mailing():
    now = timezone.localtime(timezone.now())
    mailings = Mailing.objects.filter(periodicity="Раз в день", status="Создана")
    print(mailings)
    if mailings.start_time <= now <= mailings.end_time:
         if mailings.exists():
             for mailing in mailings:
                 print(mailing)
                 send_mail(
                     subject=Msg.header_mail,
                     message=Msg.body_mail,
                     from_email=settings.EMAIL_HOST_USER,
                     recipient_list=[Client.email],
                     )
         else:
            print('что-то пошло не так')
    else:
        print('совсем плохо')


