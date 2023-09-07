import requests

def set_env(token, i_chat_id):
    global def_url,chat_id
    def_url = f"https://api.telegram.org/bot{token}"
    chat_id= i_chat_id
    on()
    
def on():
    global send
    send = True
    
def off():
    global send
    send = False

def send_text(message, silent= False):
    if not send: return
    url = def_url + f'''/sendMessage?chat_id={chat_id}{"&disable_notification=true" if silent is True else ""}&text={message}'''
    requests.get(url)  

def send_markdown_text(message, silent = False):
    if not send: return
    url = def_url + f'''/sendMessage?chat_id={chat_id}{"&disable_notification=true" if silent is True else ""}&text={message}&parse_mode=MarkdownV2'''
    requests.get(url)

def send_media(type, file_url, caption = "", silent = False):
    if not send: return
    type = type.lower()
    files = {
        type : open(file_url, "rb")
    }
    url = def_url + f'''/send{type[0].upper()+type[1:]}?chat_id={chat_id}{"&disable_notification=true" if silent is True else ""}&caption={caption}'''
    requests.post(url, files=files)

def send_photo(file_url,caption = " ", silent = False):
    send_media("photo", file_url, caption, silent)

def send_document(file_url,caption = " ", silent = False):
    send_media("document", file_url, caption, silent)

def send_audio(file_url, caption = " ", silent = False):
    send_media("audio", file_url, caption, silent)

def send_video(file_url, caption = " ", silent = False):
    send_media("video", file_url, caption, silent)
