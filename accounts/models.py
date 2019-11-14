from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    
    lunch_noti_enable = models.BooleanField(default=True) #점심알림여부
    schedule_noti_enable = models.BooleanField(default=True) #스케줄알림여부
    comp_addr = models.TextField(blank=True) #회사주소
    chat_id =  models.CharField(max_length=100, blank=True) #user telegram chatid
        

