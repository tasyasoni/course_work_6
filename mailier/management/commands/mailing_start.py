import logging
from django.conf import settings


from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from mailier.services import run_daily_mailing

logger = logging.getLogger(__name__)


@util. close_old_connections
def delete_old_job_executions(max_age=604_800):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)

    class Command(BaseCommand):
        help = "Runs APScheduler."

        def handle(self, *args, **options):
            scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
            scheduler.add_jobstore(DjangoJobStore(), "default")

            scheduler.add_job(
                run_daily_mailing,
                trigger=CronTrigger(minute="*/1"),
                id="daily_job",
                max_instances=1,
                replace_existing=True,
            )
            logger.info("Added job 'daily_job'.")

            scheduler.add_job(
                weekly_tasks,
                trigger=CronTrigger(day_of_week="*/1"),
                id="weekly_job",
                max_instances=1,
                replace_existing=True,
            )
            logger.info("Added job 'weekly_job'.")

            scheduler.add_job(
                monthly_tasks,
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