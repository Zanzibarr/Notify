import requests
import sys

def main():
    
    if (len(sys.argv)<2):
        print("Notify error: wrong arguments.")
        exit(0)
        
    l = len(sys.argv)
    
    message = ""
        
    for i in range(1, l):
        message += sys.argv[i]+" "

    TOKEN = "YourTelegramBotToken"
    chat_id = "YourChatIdWithBot"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"

    requests.get(url)