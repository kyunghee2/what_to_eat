import requests 
  
URL = "https://sleepy-thicket-13178.herokuapp.com/chatbot/telegram_chat_schedule/"
  
PARAMS = {}    
r = requests.get(url = URL, params = PARAMS) 

print(r)