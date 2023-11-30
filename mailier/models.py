from django.conf import settings
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Client(models.Model):
    name = models.CharField(max_length=150, verbose_name='фио_клиента')
    email = models.EmailField(max_length=50, verbose_name='почта', unique=True)
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f"{self.name} {self.email}"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class Mailing(models.Model):
    time_mail = models.DateTimeField(verbose_name='время_рассылки')
    period_mail = models.CharField(max_length=25, verbose_name='периодичность_рассылки')
    status_mail = models.CharField(max_length=25, verbose_name='статус_рассылки')
    clients = models.ManyToManyField(Client, verbose_name='клиенты_рассылки')

    def __str__(self):
        return f"{self.time_mail} {self.status_mail}"

    class Meta:
        verbose_name = "рассылка"
        verbose_name_plural = "рассылки"


class Msg(models.Model):
    header_mail = models.TextField(verbose_name='тема_письма')
    body_mail = models.TextField(verbose_name='тело_письма')
    mailing_list = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка', **NULLABLE)

    def __str__(self):
        return f"{self.header_mail} {self.body_mail}"

    class Meta:
        verbose_name = "сообщение"
        verbose_name_plural = "сообщения"


class Logfile(models.Model):
    time_log_send = models.DateTimeField(verbose_name='дата и время последней попытки')
    status_log = models.BooleanField(verbose_name='статус попытки')
    server_response = models.CharField(verbose_name='ответ почтового сервера', **NULLABLE)
    mailing_list = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='клиент рассылки')

    def __str__(self):
        return f"{self.time_log_send} {self.status_log}"

    class Meta:
        verbose_name = "лог"
        verbose_name_plural = "логи"