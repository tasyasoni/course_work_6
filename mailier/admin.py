from django.contrib import admin
from mailier.models import Client, Mailing, Msg, Logfile


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment',)
    list_filter = ('email',)
    search_fields = ('email',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('time_mail', 'period_mail', 'status_mail',)
    list_filter = ('status_mail',)
    search_fields = ('status_mail',)


@admin.register(Msg)
class MsgAdmin(admin.ModelAdmin):
    list_display = ('header_mail', 'body_mail', 'mailing_list',)
    list_filter = ('header_mail',)
    search_fields = ('header_mail',)



@admin.register(Logfile)
class LogfileAdmin(admin.ModelAdmin):
    list_display = ('time_log_send', 'status_log', 'server_response', 'mailing_list')
    list_filter = ('status_log',)
    search_fields = ('status_log',)
