from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Telegram
# Register your models here.
admin.site.register(User, UserAdmin)

class TelegramAdmin(admin.ModelAdmin):
     list_display = ('pk','chat_id')

admin.site.register(Telegram, TelegramAdmin)