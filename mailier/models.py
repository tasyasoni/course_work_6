from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='фио_клиента')
    email = models.EmailField(max_length=50, verbose_name='почта', unique=True)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Msg(models.Model):
    header_mail = models.CharField(max_length=25, verbose_name='Тема_рассылки')
    body_mail = models.TextField(verbose_name='Тело_рассылки')


    def __str__(self):
        return f"{self.header_mail} {self.body_mail}"

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"



class Mailing(models.Model):
    DAILY = "Ежедневная"
    WEEKLY = "Еженедельная"
    MONTHLY = "Ежемесячная"

    PERIODICITY_CHOICES = [
        (DAILY, "Раз в день"),
        (WEEKLY, "Раз в неделю"),
        (MONTHLY, "Раз в месяц"),
    ]

    CREATED = 'Создана'
    STARTED = 'Запущена'
    COMPLETED = 'Завершена'

    STATUS_CHOICES = [
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
        (COMPLETED, "Завершена"),
    ]
    period_mail = models.CharField(max_length=25, choices=PERIODICITY_CHOICES, verbose_name='периодичность_рассылки')
    status_mail = models.CharField(max_length=25, choices=STATUS_CHOICES, verbose_name='статус_рассылки') #создана, запущена, выполнена
    start_mail = models.DateTimeField(verbose_name='время начала рассылки', **NULLABLE)
    end_mail = models.DateTimeField(verbose_name='время окончания рассылки', **NULLABLE)
    clients = models.ManyToManyField(Client, verbose_name='клиенты_рассылки')
    message = models.ForeignKey(Msg, default=None, **NULLABLE, verbose_name='текст_рассылки', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.period_mail}"

    class Meta:
        verbose_name = "параметры_рассылка"
        verbose_name_plural = "параметры_рассылки"



class Logfile(models.Model):
    time_log_send = models.DateTimeField(verbose_name='дата и время последней попытки')
    status_log = models.BooleanField(verbose_name='статус попытки')
    server_response = models.CharField(verbose_name='ответ почтового сервера', **NULLABLE)
    mailing_list = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')


    def __str__(self):
        return f"{self.time_log_send} {self.status_log}"

    class Meta:
        verbose_name = "лог"
        verbose_name_plural = "логи"
