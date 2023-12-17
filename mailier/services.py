from django.utils import timezone
from django.conf import settings
from mailier.models import Mailing, Client, Msg
from django.core.mail import send_mail
from django_apscheduler import util


@util.close_old_connections
def daily_mail():
    mailings = Mailing.objects.filter(period_mail='Ежедневная').exclude(status_mail=Mailing.STARTED)
    if not mailings.exists():
        return
    for mailing in mailings:
        now = timezone.localtime(timezone.now())
        if mailing.start_mail <= now <= mailing.end_mail:
            mailing.status_mail = Mailing.STARTED
            mailing.save()

            try:
                send_mail(
                    subject=mailing.message.header_mail,
                    message=mailing.message.body_mail,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=mailing.clients.values_list('email', flat=True),
                    fail_silently=False,
                )

            except Exception as error:
                mailing.logfile_set.create(time_log_send=timezone.now(),
                                           status_log=False,
                                           server_response=str(error))
            else:
                mailing.logfile_set.create(time_log_send=timezone.now(),
                                           status_log=True,
                                           server_response='OK')
                mailing.status_mail = Mailing.COMPLETED
                mailing.save()


@util.close_old_connections
def weekly_mail():
    mailings = Mailing.objects.filter(period_mail='Еженедельная').exclude(status_mail=Mailing.STARTED)
    if not mailings.exists():
        return
    for mailing in mailings:
        now = timezone.localtime(timezone.now())
        if mailing.start_mail <= now <= mailing.end_mail:
            try:
                send_mail(
                    subject=mailing.message.header_mail,
                    message=mailing.message.body_mail,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=mailing.clients.values_list('email', flat=True),
                    fail_silently=False,
                )
                mailing.status_mail = Mailing.STARTED
                mailing.save()

            except Exception as error:
                mailing.logfile_set.create(time_log_send=timezone.now(),
                                           status_log=False,
                                           server_response=str(error))
            else:
                mailing.logfile_set.create(time_log_send=timezone.now(),
                                           status_log=True,
                                           server_response='OK')
                mailing.status_mail = Mailing.COMPLETED
                mailing.save()



@util.close_old_connections
def mounthly_mail():
    mailings = Mailing.objects.filter(period_mail='Ежемесячная').exclude(status_mail=Mailing.STARTED)
    if not mailings.exists():
        return
    for mailing in mailings:
        now = timezone.localtime(timezone.now())
        if mailing.start_mail <= now <= mailing.end_mail:
            try:
                send_mail(
                    subject=mailing.message.header_mail,
                    message=mailing.message.body_mail,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=mailing.clients.values_list('email', flat=True),
                    fail_silently=False,
                )
                mailing.status_mail = Mailing.STARTED
                mailing.save()

            except Exception as error:
                mailing.logfile_set.create(time_log_send=timezone.now(),
                                           status_log=False,
                                           server_response=str(error))
            else:
                mailing.logfile_set.create(time_log_send=timezone.now(),
                                           status_log=True,
                                           server_response='OK')
                mailing.status_mail = Mailing.COMPLETED
                mailing.save()
