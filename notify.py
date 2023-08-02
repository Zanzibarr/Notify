import requests
 
def send(message):

    TOKEN = "your_bot_token"
    chat_id = "your_chat_id"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

    requests.get(url)