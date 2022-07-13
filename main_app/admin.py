from mailbox import Mailbox
from django.contrib import admin
from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'time_zone', 'mobile_code', 'mobile_number', 'tag',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Mailing)
admin.site.register(Message)


