import logging
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.utils import timezone
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJob, DjangoJobExecution
from django_apscheduler import util
from mailier.models import Mailing, Msg, Client


logger = logging.getLogger(__name__)


@util.close_old_connections
def my_job():
    mailings = Mailing.objects.filter(period_mail = 'Ежедневная')
    print(mailings)
    if not mailings.exists():
        return
    for mailing in mailings:
        print(mailing)
        try:
            send_mail(
                subject=mailing.message.header_mail,
                message=mailing.message.body_mail,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=mailing.clients.values_list('email', flat=True),
                fail_silently=False,
            )
            print("ушла рассылка")
        except Exception as error:
            mailing.logfile_set.create(time_log_send=timezone.now(),
                                        status_log=False,
                                        server_response=str(error))
        else:
            mailing.logfile_set.create(time_log_send=timezone.now(),
                                        status_log=True,
                                        server_response='OK')



class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(minute="*/1"),
            id="daily_job",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'daily_job'.")


            # scheduler.add_job(
            #     weekly_tasks,
            #     weekly_tasks,
            #     weekly_tasks,
            #     weekly_tasks,
            #     trigger=CronTrigger(day_of_week="*/1"),
            #     id="weekly_job",
            #     max_instances=1,
            #     replace_existing=True,
            # )
            # logger.info("Added job 'weekly_job'.")
            #
            # scheduler.add_job(
            #     monthly_tasks,
            #     trigger=CronTrigger(day="*/30"),
            #     id="monthly_job",
            #     max_instances=1,
            #     replace_existing=True,
            # )
            # logger.info("Added job 'monthly_job'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
