from django.http import HttpResponse
from django.shortcuts import render
import random

from .models import Client

# сделаем случайный образом клиентов в тестовой базе
def create_clients(request):
    tags = ['sport','family','hobby','vacation',]
    Client.objects.all().delete()
    code_list=[922, 958, 919, 927, 950]
    for y in range(40):
        c = Client()

        code = code_list[random.randint(0,len(code_list)-1)]
        number = code * 1_000_00_00 + random.randint(1,9) * 1_00_00_00 +random.randint(0,999999)
        c.mobile_number = number
        c.mobile_code = code
        c.time_zone = random.randint(-4,5)
        c.tag = tags[random.randint(0,len(tags)-1)]
        c.save()
    return HttpResponse('Hello,words')