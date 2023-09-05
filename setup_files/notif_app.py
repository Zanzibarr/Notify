import subprocess, notify, shlex, json, sys, os

version = "notify version: 1.2.1"

error = """
Notify error: wrong arguments.
Use notify -h or notify -help to get instructions.
"""
map = {"-p":"photo", "-d":"document", "-a":"audio", "-v":"video"}
base_path = os.path.dirname(__file__)

def help():
    print(f"""
Commands accepted: > notify <type> <content>
The content could be missing in some cases.

> notify -h / > notify -help
    Prints the instructions
> notify -version / > notify -v
    See the current notify version
> notify -update / > notify -u
    Download the latest version of notify
> notify -uninstall
    Uninstall all the files associated to the notify app except, eventually, the credentials that have been stored in /etc/zanz_notify_config 

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


If you wish to change the token or chat_id associated to this application (for command line use), you will need to follow the 'Edit build' procedure in the readme.md, located at {base_path}/readme.md

Base folder: {base_path}
Credentials folder: /etc/zanz_notify_config
Base repository: https://github.com/Zanzibarr/Telegram_Python_Notifier
""")

def main():
    
    global error, map
    
    if len(sys.argv)==1:
        print(error)
        exit(1)
    elif sys.argv[1] in ("-h", "-help"):
        if len(sys.argv) != 2:
            print(error)
            exit(1)
        help()
        exit(0)
    elif sys.argv[1] in ("-update", "-u"):
        if len(sys.argv) != 2:
            print(error)
            exit(1)

        print("Downloading latest version...")
        os.mkdir(f"{base_path}/git")
        subprocess.run(shlex.split(f"git clone --quiet https://github.com/Zanzibarr/Telegram_Python_Notifier {base_path}/git"))
        subprocess.run(shlex.split(f"python3 {base_path}/git/setup.py -update"))
        print("Removing temporary files...")
        subprocess.run(shlex.split(f"sudo rm -r {base_path}/git"))
        print("Update completed.")
        
        exit(0)
    elif sys.argv[1] == "-uninstall":
        if len(sys.argv) != 2:
            print(error)
            exit(1)
        res = ""
        while res not in ("y", "n"):
            res = input("Proceeding to uninstall notify? [y/n]: ")
            if res not in ("y", "n"):
                print("Command not recognised")
        if res == "n":
            print("Uninstall aborted.")
            exit(0)
        
        print("Uninstalling...")
        subprocess.run(shlex.split(f"rm -r {os.path.expanduser('~')}/.notify"))
        print("notify has been succesfully uninstalled.")
        exit(0)
    elif sys.argv[1] in ("-version", "-v"):
        if len(sys.argv) != 2:
            print(error)
            exit(1)
        print(version)
        exit(0)

    '''>>__EDIT__>> credentials = your_json_credentials <<__EDIT__<<'''

    if credentials != 0:
        notify.set_env(credentials["token"], credentials["chatid"])
    else:
        notify.set_env(input("Insert the token for the bot you want to use: "), input("Insert your chat id: "))

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

if __name__ == "__main__":
    main()
