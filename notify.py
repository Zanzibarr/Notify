import requests


def set_env(token, i_chat_id):
    global def_url,chat_id
    def_url = f"https://api.telegram.org/bot{token}"
    chat_id= i_chat_id
    

def send_text(message):
    url = def_url + f"/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url)

def send_media(type, file_url):
    type = type.lower()
    files = {
        type : open(file_url, "rb")
    }
    url = def_url + f"/send{type[0].upper()+type[1:]}?chat_id={chat_id}"
    requests.post(url, files=files)

def send_photo(file_url):
    send_media("photo", file_url=file_url)

def send_document(file_url):
    send_media("document", file_url=file_url)

def send_audio(file_url):
    send_media("audio", file_url=file_url)

def send_video(file_url):
    send_media("video", file_url=file_url)