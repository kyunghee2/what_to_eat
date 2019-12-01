import requests 
import datetime

URL = "https://sleepy-thicket-13178.herokuapp.com/chatbot/telegram_chat_schedule/"

t = ['월','화','수','목','금','토','일']
r = datetime.datetime.today().weekday()
print(t[r])
# PARAMS = {}    
# r = requests.get(url = URL, params = PARAMS) 

# print(r)