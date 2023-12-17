import logging
from django.conf import settings
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from mailier.services import daily_mail, weekly_mail, mounthly_mail

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            daily_mail,
            trigger=CronTrigger(day="*/1"),
            id="daily_job",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'daily_job'.")


        scheduler.add_job(
            weekly_mail,
            trigger=CronTrigger(day_of_week="*/1"),
            id="weekly_job",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'weekly_job'.")

        scheduler.add_job(
            mounthly_mail,
            trigger=CronTrigger(day="*/30"),
            id="monthly_job",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'monthly_job'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
