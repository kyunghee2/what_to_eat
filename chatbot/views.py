import requests
import random
import telegram
import json
from django.shortcuts import render,redirect
from decouple import config
from restaurant.models import Restaurant
from accounts.models import Telegram
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db.models import Q

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN') #프로젝트내에 .env에서 정보를 가져옴
chat_id = config('CHAT_ID')
bot = telegram.Bot(token=token)

def index(request):
    return render(request, 'chatbot/index.html' )

def telegram_chat_schedule(request):
    #telegram chat_id 등록된 모든 사용자에게 추천 메시지 발송
    status=1
    error_msg=''
    try :
        telegram_users = Telegram.objects.all()
        print('>>>>>>>>>>>>>')
        print(telegram_users)
        restaurants = Restaurant.objects.filter(r_type='한식')
        sel_obj = random.choice(restaurants)

        for user in telegram_users:     
            sendtext = "오늘 점심 [{0}] 음식점 추천해드립니다.♡ \n\n"
            sendtext += "메인메뉴: {1} \n"
            sendtext += "주소: {2} "
            sendtext += "(<a href='https://map.kakao.com/?q={3}'>길찾기 바로가기</a>)\n"
            sendtext += "그외 메뉴(가격):\n"
            sendtext += "<pre>{4}</pre>"
            sendtext = sendtext.format(sel_obj.name,sel_obj.main_menu, sel_obj.addr, sel_obj.addr, sel_obj.content)

            bot.send_message(chat_id=user.chat_id, text=sendtext,parse_mode='HTML')

    except Exception as e:
        print('error!!!')
        status = 0
        error_msg = str(e)
        
    context = {
        'status': status,
        'msg':error_msg
    }
    return JsonResponse(context)


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
            sendtext += "뭐먹을까 ChatBot 입니다\n"
            sendtext += "점심시간에 맛집 정보를 추천하고 맛집 검색 서비스를 해드립니다.\n"
            sendtext += "(현재 역삼동만 서비스하고 있습니다)\n"
            bot.send_message(chat_id=chat_id, text=sendtext,parse_mode='HTML')

            sendtext = message_create('help')
            bot.send_message(chat_id=chat_id, text=sendtext,parse_mode='HTML')

            #알림 사용자 정보 없는 경우만 저장
            telegrams = Telegram.objects.filter(chat_id=chat_id)                     
            if telegrams.count() == 0 :
                telegram = Telegram(chat_id=chat_id)
                telegram.save()

        elif '/help' in text:
            sendtext = message_create('help')
            bot.send_message(chat_id=chat_id, text=sendtext,parse_mode='HTML')

        elif '/맛집' in text:
            arr = text.split(' ')
            if len(arr) >= 1:
                r_type = arr[1]
                #restaurants = Restaurant.objects.filter(r_type=r_type)
                restaurants = Restaurant.objects.filter(Q(name__contains=r_type) | Q(r_type__contains=r_type) | Q(addr__contains=r_type))
                sel_obj = random.choice(restaurants)

                sendtext = " [{0}] 음식점 추천해드립니다.♡ \n\n"
                sendtext += "메인메뉴: {1} \n"
                sendtext += "주소: {2} "
                sendtext += "(<a href='https://map.kakao.com/?q={3}'>길찾기 바로가기</a>)\n"
                sendtext += "그외 메뉴(가격):\n"
                sendtext += "<pre>{4}</pre>"
                sendtext = sendtext.format(sel_obj.name,sel_obj.main_menu, sel_obj.addr, sel_obj.addr, sel_obj.content)

                bot.send_message(chat_id=chat_id, text=sendtext,parse_mode='HTML')
        elif '/알림설정' in text:
            telegrams = Telegram.objects.filter(chat_id=chat_id)                     
            if telegrams.count() == 0 :
                telegram = Telegram(chat_id=chat_id)
                telegram.save()

                sendtext ="알림이 설정되었습니다"
                bot.send_message(chat_id=chat_id, text=sendtext,parse_mode='HTML')

        elif '/알림해제' in text:
            telegrams = Telegram.objects.filter(chat_id=chat_id)                     
            if telegrams.count() > 0 :
                telegram = Telegram.objects.get(chat_id=chat_id)
                telegram.delete()

                sendtext ="알림이 해제되었습니다"
                bot.send_message(chat_id=chat_id, text=sendtext,parse_mode='HTML')
        else:
            pass
            # bot.send_photo(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')
            #sendtext="test33"
            # bot.send_message(chat_id=chat_id, text=sendtext)
    except:
        pass
  
   
    return render(request, 'chatbot/index.html' )

def message_create(msg_type):
    result = ''
    if msg_type == 'help':
        result ="* 맛집검색 방법은? /맛집 한식 \n"
        result +="  (종류:한식,양식,중식,일식,분식)\n"
        result +="* 알림해제 방법은? /알림해제 \n"
        result +="* 알림설정 방법은? /알림설정 \n"

    return result

