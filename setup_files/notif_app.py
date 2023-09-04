import subprocess, shlex, sys, notify, os

error = """
Notify error: wrong arguments.
Use notify -h or notify -help to get instructions.
"""
map = {"-p":"photo", "-d":"document", "-a":"audio", "-v":"video"}

def help():
    print(f"""
Commands accepted: > notify <type> <content>
The content could be missing in some cases.

> notify -h / > notify -help
    Prints the instructions
> notify -update <update_type>
    Download the latest version of notify
    update_type:
        -reset : uninstalls notify and clones it back in the same place (you will need to go through the setup)
        -copy : creates a folder named __update (inside the base folder) with the new version, doesn't remove anything from the original folder (except the content of the __update folder, if there was one)
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
    
    if len(sys.argv)==1:
        print(error)
        exit(0)
    elif sys.argv[1] in ("-h", "-help"):
        help()
        exit(0)
    elif sys.argv[1] == "-update":
        if len(sys.argv) != 3:
            print(error)
            exit(0)
        if sys.argv[2] == "-reset":
            check = input(f"The folder {os.path.dirname(__file__)} and all of it's files are gonna be removed and replaced with the new version of the notify.\nIf you proceed you will also need to run the setup procedure.\nContinue? [y/n]: ")
            if check not in ("y", "n"):
                print("Input non recognised: stopping the update.") 
                exit(0)
            if check == "y":
                subprocess.run(shlex.split(f"sudo rm -r {os.path.dirname(__file__)}"))
                subprocess.run(shlex.split(f"git clone https://github.com/Zanzibarr/Telegram_Python_Notifier {os.path.dirname(__file__)}"))
            else:
                print("Cancelling the update.")
        elif sys.argv[2] == "-copy":
            check = input(f"The folder {os.path.dirname(__file__)}/__update and all of it's files are gonna be removed and replaced with the new version of the notify.\nTo use it as the new notify, you will have to run the setup procedure.\nContinue? [y/n]: ")
            if check not in ("y", "n"):
                print("Input non recognised: stopping the update.") 
                exit(0)
            if check == "y":
                subprocess.run(shlex.split(f"sudo rm -r {os.path.dirname(__file__)}/__update"))
                subprocess.run(shlex.split(f"mkdir {os.path.dirname(__file__)}/__update"))
                subprocess.run(shlex.split(f"git clone https://github.com/Zanzibarr/Telegram_Python_Notifier {os.path.dirname(__file__)}/__update"))
            else:
                print("Cancelling the update.")
        else:
            print("Input non recognised: stopping the update.")
        exit(0)
    
    notify.set_env(f">>__EDIT__>>your_bot_token<<__EDIT__<<", f">>__EDIT__>>your_chat_id<<__EDIT__<<")

    if sys.argv[1] == "-t":
        notify.send_text(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "-md":
        notify.send_markdown_text(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "-m" and len(sys.argv)>=4:
        if (sys.argv[2] not in ("photo", "document", "audio", "video")):
            print(error)
            exit(0)
        notify.send_media(sys.argv[2], " ".join(sys.argv[3:]))
    elif sys.argv[1] in ("-p", "-d", "-a", "-v") and len(sys.argv)>=3:
        notify.send_media(map[sys.argv[1]], " ".join(sys.argv[2:]))
    else:
        print(error)