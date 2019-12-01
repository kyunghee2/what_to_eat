import requests 
import datetime
from decouple import config

schedule_url = config('SCHEDULE_URL')

t = ['월','화','수','목','금','토','일']
r = datetime.datetime.today().weekday()
week = t[r]
print(week)
if week != "일" and week != "토":    
    PARAMS = {}    
    r = requests.get(url = schedule_url, params = PARAMS) 
    print(">>>>")
    print(r)
else:
    print("주말실행안함")
    