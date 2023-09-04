import sys, notify, os

error = "Notify error: wrong arguments.\\nUse notify -h or notify -help to get instructions."
map = {"-p":"photo", "-d":"document", "-a":"audio", "-v":"video"}

def help():
    print(f"""
Commands accepted: > notify <type> <content>
The content could be missing in some cases.

> notify -h / > notify -help
    Prints the instructions
> notify -t This is a text message
    Sends the full message followed by '-t' (message -> This is a text message)
> notify -md #This is a markdown text
    Sends the full markdown text followed by '-md' (message -> #This is a markdown text)
> notify -m <media_type> url
    Sends a media located in the url specified.
    media_type:
        photo (> notify -m photo /path/to/photo.png)
        document (> notify -m document /path/to/document.txt)
        audio (> notify -m audio /path/to/audio.mp3)
        video (> notify -m video /path/to/video.mp4)
> notify -p url
    Sends a photo located in the url specified (is the same of > notify -m photo url)
> notify -d url
    Sends a document located in the url specified (is the same of > notify -m document url)
> notify -a url
    Sends an audio located in the url specified (is the same of > notify -m audio url)
> notify -v url
    Sends a video located in the url specified (is the same of > notify -m video url)


If you wish to change the token or chat_id associated to this application (for command line use), you will need to follow the 'Edit build' procedure in the readme.md, located at {os.path.dirname(__file__)}/readme.md

Base repo: https://github.com/Zanzibarr/Telegram_Python_Notifier
""")

def main():
    
    global error, map
    
    notify.set_env(f">>__EDIT__>>your_bot_token<<__EDIT__<<", f">>__EDIT__>>your_chat_id<<__EDIT__<<")
    
    if (len(sys.argv)==1):
        print(error)
        exit(0)
        
    if (sys.argv[1] in ("-h", "-help")):
        help()
        exit(0)
    elif (sys.argv[1] == "-t"):
        notify.send_text(" ".join(sys.argv[2:]))
        exit(0)
    elif (sys.argv[1] == "-md"):
        notify.send_markdown_text(" ".join(sys.argv[2:]))
        exit(0)
    elif (sys.argv[1] == "-m"):
        if (sys.argv[2] not in ("photo", "document", "audio", "video")):
            print(error)
            exit(0)
        notify.send_media(sys.argv[2], " ".join(sys.argv[3:]))
        exit(0)
    elif (sys.argv[1] in ("-p", "-d", "-a", "-v")):
        notify.send_media(map[sys.argv[1]], " ".join(sys.argv[2:]))
        exit(0)
    else:
        print(error)
        exit(0)