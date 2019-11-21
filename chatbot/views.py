from django.shortcuts import render,redirect
from decouple import config
import requests
import random
import telegram
import json
from restaurant.models import Restaurant
from django.views.decorators.http import require_POST

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN') #프로젝트내에 .env에서 정보를 가져옴
chat_id = config('CHAT_ID')
bot = telegram.Bot(token=token)

def index(request):
    return render(request, 'chatbot/index.html' )

@require_POST
def telegram_chatbot(request,token_in):
    print(request.body)
    body = request.body
    body = body.decode('utf-8')
    jsonbody = json.loads(body)

    # print(type(json.loads(body)))
    chat_id=''
    text=''
    try:
        chat_id = jsonbody.get('message').get('from').get('id')
        text = jsonbody.get('message').get('text')

        if '/start' in text:
            print('start')
            sendtext = "환영합니다 !\n"
            sendtext += "뭐먹을까 봇 입니다\n"
            sendtext += "점심에 맛집 정보를 추천해드립니다.\n"
            sendtext += "(현재 역삼동만 서비스하고 있습니다.)\n"
            #sendtext += " <a href=''>가입하기</a> "
            bot.send_message(chat_id=chat_id, text=sendtext,parse_mode='HTML')

            sendtext ="* 맛집검색 방법은? /맛집 한식 \n"
            sendtext +="* 알림해제 방법은? /알림해제 \n"
            sendtext +="* 도움말? /help"
            bot.send_message(chat_id=chat_id, text=sendtext,parse_mode='HTML')
        elif '/help' in text:
            sendtext ="* 맛집검색 방법은? /맛집 한식 \n"
            sendtext +="  (종류:한식,양식,중식,일식,분식)\n"
            sendtext +="* 알림해제 방법은? /알림해제 \n"
            bot.send_message(chat_id=chat_id, text=sendtext,parse_mode='HTML')
        elif '/맛집' in text:
            print('search')
            arr = text.split(' ')
            if len(arr) >= 1:
                r_type = arr[1]
                restaurants = Restaurant.objects.filter(r_type=r_type)
                sel_obj = random.choice(restaurants)

                sendtext = " [{0}] 음식점 추천해드립니다.♡ \n\n"
                sendtext += "메인메뉴: {1} \n"
                sendtext += "주소: {2} "
                sendtext += "(<a href='https://map.kakao.com/?q={3}'>길찾기 바로가기</a>)\n"
                sendtext += "그외 메뉴(가격):\n"
                sendtext += "<pre>{4}</pre>"
                sendtext = sendtext.format(sel_obj.name,sel_obj.main_menu, sel_obj.addr, sel_obj.addr, sel_obj.content)

                bot.send_message(chat_id=chat_id, text=sendtext,parse_mode='HTML')

        else:
            pass
            # bot.send_photo(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')
            #sendtext="test33"
            # bot.send_message(chat_id=chat_id, text=sendtext)
    except:
        pass
  
   
    return render(request, 'chatbot/index.html' )
