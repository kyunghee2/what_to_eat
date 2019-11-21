from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    
    comp_addr = models.TextField(blank=True) #회사주소
    lunch_noti_enable = models.BooleanField(default=True) #점심알림여부
    schedule_noti_enable = models.BooleanField(default=True) #스케줄알림여부
    chat_id =  models.CharField(max_length=20, blank=True) #user telegram chatid
        

class Telegram(models.Model):
    chat_id =  models.CharField(max_length=20)

        #객체 표시 형식 수정
    def __str__(self):
        return f'[{self.pk}] {self.chat_id}'