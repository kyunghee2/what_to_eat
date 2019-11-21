
from django.urls import path
from . import views

app_name = 'chatbot'

urlpatterns = [
    path('', views.index, name='index'),
    path('telegram/<str:token_in>/', views.telegram_chatbot, name='telegram'),
    #path('telegram/', views.telegram_chatbot, name='telegram'),
]
