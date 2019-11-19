from django.shortcuts import render,redirect
from decouple import config
import requests
import random
import telegram
import json

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN') #프로젝트내에 .env에서 정보를 가져옴
chat_id = config('CHAT_ID')
bot = telegram.Bot(token=token)

def index(request):
    return render(request, 'chatbot/index.html' )

def telegram_chatbot(request):
   
    body = request.body
    body = body.decode('utf-8')
    jsonbody = json.loads(body)

    #print(type(json.loads(body)))
    chat_id = jsonbody.get('message').get('from').get('id')
    text = jsonbody.get('message').get('text')
    
    if '/start' in text:
        pass
    else:
        pass
        # bot.send_photo(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')
        #sendtext="test33"
        # bot.send_message(chat_id=chat_id, text=sendtext)
   
    return render(request, 'chatbot/index.html' )
