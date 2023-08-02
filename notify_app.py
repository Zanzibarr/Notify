import sys, notify

def main():
    
    if (len(sys.argv)<2):
        print("Notify error: wrong arguments.\nExpected command: > notify This is the message")
        exit(0)
        
    l = len(sys.argv)
    
    message = ""
        
    for i in range(1, l):
        message += sys.argv[i]+" "
        
    notify.set_env("your_bot_token", "your_chat_id")
    notify.send_text(message=message)
