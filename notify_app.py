import subprocess, notify, shlex, json, sys, os

version = "notify version: 1.4"

command_error = "Command not recognised.\n"
error = """
Notify error: wrong arguments.
Use notify -h or notify -help to get instructions.
"""

bashrc_edit = """alias notify='python3 $HOME/.notify/notify_app.py'
export PYTHONPATH=$HOME/.notify/python_module
"""

map = {"-p":"photo", "-d":"document", "-a":"audio", "-v":"video"}

home = os.path.expanduser('~')
base_path = os.path.dirname(__file__)
std_config_path = f"{home}/.zanz_notify_config"

def help():
    print(f"""
Commands accepted: > notify <type> <content>
The content could be missing in some cases.

> notify -h / > notify -help
    Prints the instructions
> notify -version
    See the current notify version
> notify -update / > notify -u
    Download the latest version of notify
> notify -credentials / > notify -c
    Print the credentials location and asks if you wish to update them.
> notify -uninstall
    Uninstall all the files associated to the notify app except, eventually, the credentials that have been stored in {std_config_path}

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

Base folder: {base_path}
Credentials folder: {std_config_path}
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
        
        choice = input("Proceeding to uninstall notify? [y/n]: ")
        while choice not in ("y", "n"):
            choice = input(f"{command_error}Proceeding to uninstall notify? [y/n]: ")

        if choice == "n":
            print("Uninstall aborted.")
            exit(0)
        
        print("Uninstalling...")
        subprocess.run(shlex.split(f"rm -r {os.path.expanduser('~')}/.notify"))
        
        bashrc = ""
        with open(f"{os.path.expanduser('~')}/.bashrc", "r") as f:
            bashrc = f.read()
        bashrc = bashrc.replace(bashrc_edit, "")
        with open(f"{os.path.expanduser('~')}/.bashrc", "w") as f:
            f.write(bashrc)
        print("notify has been succesfully uninstalled.")

        exit(0)

    elif sys.argv[1] == "-version":
        if len(sys.argv) != 2:
            print(error)
            exit(1)

        print(version)
        
        exit(0)

    elif sys.argv[1] in ("-credentials", "-c"):
        if len(sys.argv) != 2:
            print(error)
            exit(1)

        print(f"Credentials location: {std_config_path}")
        choice = input("Continue using the previously stored credenials? [y/n]: ")
        while choice not in ("y", "n"):
            choice = input(f"{command_error}Change the credenials? [y/n]: ")

        if choice == "n":
            choice = input(f"Continue storing credentials? [y to change the stored credentials /n to not have credentials saved /q to quit]: ")
            while choice not in ("y", "n", "q"):
                choice = input(f"{command_error}Continue storing credentials? [y/n/q]: ")
            
            if choice == "y":
                token = input("Insert the token for the bot you want to use: ")
                chat_id = input("Insert the your chat id: ")
                print(f"Storing credentials inside {std_config_path}...")
                json_cred = '{"token":"'+token+'","chatid":"'+chat_id+'"}'
                conf_file = open(std_config_path, "w")
                conf_file.write(json_cred)
                conf_file.close()
            elif choice == "n":
                conf_file = open(std_config_path, "w")
                conf_file.write("none")
                conf_file.close()
            else:
                print("No change has been done.")

        exit(0)

    credentials = ""
    with open(std_config_path, "r") as f:
        credentials = f.read()

    if credentials == "none":
        notify.set_env(input("Insert the token for the bot you want to use: "), input("Insert your chat id: "))
    else:
        credentials = json.loads(credentials)
        notify.set_env(credentials["token"], credentials["chatid"])


    if sys.argv[1] == "-t":
        notify.send_text(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "-md":
        notify.send_markdown_text(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "-m" and len(sys.argv)>=4:
        if (sys.argv[2] not in ("photo", "document", "audio", "video")):
            print(error)
            exit(1)

        notify.send_media(sys.argv[2], " ".join(sys.argv[3:]))
    elif sys.argv[1] in ("-p", "-d", "-a", "-v") and len(sys.argv)>=3:
        notify.send_media(map[sys.argv[1]], " ".join(sys.argv[2:]))
    else:
        print(error)
        exit(1)

if __name__ == "__main__":
    main()
