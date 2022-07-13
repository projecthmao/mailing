from django.db import models

class Client(models.Model):
    time_zone = models.IntegerField()
    mobile_number = models.IntegerField()
    mobile_code = models.IntegerField()
    tag = models.CharField(max_length=255, default='')

class Mailing(models.Model):
    start_dt = models.DateTimeField()
    finish_dt = models.DateTimeField()
    text = models.CharField(max_length=255, default='')
    tag = models.CharField(max_length=255, default='')

class Message(models.Model):
    mailing_dt = models.DateTimeField()
    status = models.CharField(max_length=255, choices=[('MAILED', 'Доставлено успешно'),('LOST','Потеряно'),])
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)