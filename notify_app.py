import subprocess, requests, notify, shlex, json, sys, os

def main():
    
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
        if len(sys.argv) not in (2, 3):
            print(error)
            exit(1)

        ntf_update()
        exit(0)

    elif sys.argv[1] == "-uninstall":
        if len(sys.argv) != 2:
            print(error)
            exit(1)

        ntf_uninstall()
        exit(0)

    elif sys.argv[1] == "-version":
        if len(sys.argv) != 2:
            print(error)
            exit(1)

        print(version)
        exit(0)

    elif sys.argv[1] in ("-cred", "-c"):
        if len(sys.argv) != 2:
            print(error)
            exit(1)

        ntf_credentials()
        exit(0)

    credentials = ""
    with open(std_config_path, "r") as f:
        credentials = f.read()

    if credentials == "none":
        notify.set_env(input("Insert the token for the bot you want to use: "), input("Insert your chat id: "))
    else:
        credentials = json.loads(credentials)
        notify.set_env(credentials["token"], credentials["chatid"])

    send()



def send():

    command = " ".join(sys.argv)

    silent = False
    caption = " "
    
    if "--silent" in command:
        silent = True
        command = command.replace(" --silent", "")

    if "--caption" in command:
        caption = command.partition("--caption ")[2].partition(" -")[0]
        command = command.replace(f" --caption {caption}", "")
        
    lst = command.split(" ")

    if lst[1] == "-t":
        notify.send_text(" ".join(lst[2:]), silent=silent)

    elif lst[1] == "-md":
        notify.send_markdown_text(" ".join(lst[2:]), silent=silent)

    elif lst[1] == "-m" and len(sys.argv)>=4:
        if (lst[2] not in ("photo", "document", "audio", "video")):
            print(error)
            exit(1)

        notify.send_media(lst[2], " ".join(lst[3:]), caption=caption, silent=silent)

    elif lst[1] in ("-p", "-d", "-a", "-v") and len(sys.argv)>=3:
        notify.send_media(map[lst[1]], " ".join(lst[2:]), caption=caption, silent=silent)

    else:
        print(error)
        exit(1)


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
    > notify -update force / > notify -u force
        To force the download of the new version (without checking current version)
> notify -cred / > notify -c
    Print the credentials location and asks if you wish to update them.
> notify -uninstall
    Uninstall all the files associated to the notify app except, eventually, the credentials that have been stored in {std_config_path}

For all the type of messages you want to send, you can use these modes:
    --silent

Examples:
    > notify --silent -t This is a silent text message
    > notify -p path/to/img.png --silent
        
> notify -t This is a text message
    Sends the full message followed by '-t' (message -> This is a text message)
> notify -md #This is a markdown text
    Sends the full markdown text followed by '-md' (message -> #This is a markdown text)

For all the media type of messages you want to send, you can use also the --caption parameter to specify the caption.
The caption to use must not contain '-' and must be right after the --caption command.
The caption must not be specified between the media type and the media url

Example:
    > notify -p path/to/img.png --caption This is a caption
    > notify --silent --caption Silent media with caption -p path/to/doc.txt

Wrong:
    > notify -p --caption Wrong caption path/to/img.png

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

{version}
""")
    
def ntf_update():

    if len(sys.argv) == 3 and sys.argv[2] != "force":
        print(error)
        exit(1)

    r = requests.get('https://raw.githubusercontent.com/Zanzibarr/Telegram_Python_Notifier/main/change_log.md')
    new_version = r.text.partition("Version ")[2].partition("\n")[0]

    if len(sys.argv) == 2:

        if "200" in str(r):
            if version.partition(": ")[2] == new_version:
                print("notify is already up-to-date")
                exit(0)

        else:
            print(f"Request to find latest version had as response: {r}.\nUpdate failed")
            exit(1)

    print("Downloading latest version...")
    for file in files:
        with open(f"{base_path}/{file}", "w") as f:
            f.write(download_file_content(file))
    subprocess.run(shlex.split(f"mv notify.py python_module/"))
    print(f"Update completed.\nnotify version: {new_version}")

def download_file_content(name):

    r = requests.get(f'https://raw.githubusercontent.com/Zanzibarr/Telegram_Python_Notifier/main/{name}')

    if "200" not in str(r):
        raise Exception(f"Request to download updated files had as response: {r}.Request failed.")
    
    return r.text

def ntf_uninstall():
        
    choice = input("Proceeding to uninstall notify? [y/n]: ")
    while choice not in ("y", "n"):
        choice = input(f"{command_error}Proceeding to uninstall notify? [y/n]: ")

    if choice == "n":
        print("Uninstall aborted.")
        exit(0)
    
    print("Uninstalling...")
    subprocess.run(shlex.split(f"rm -r {home}/.notify_zanz"))
    
    if os.path.exists(f"{home}/.bashrc"):
        bashrc = ""
        with open(f"{home}/.bashrc", "r") as f:
            bashrc = f.read()
        bashrc = bashrc.replace(bashrc_edit_title, "")
        bashrc = bashrc.replace(bashrc_edit_content, "")
        with open(f"{home}/.bashrc", "w") as f:
            f.write(bashrc)
    if os.path.exists(f"{home}/.zshrc"):
        zshrc = ""
        with open(f"{home}/.zshrc", "r") as f:
            zshrc = f.read()
        zshrc = zshrc.replace(bashrc_edit_title, "")
        zshrc = zshrc.replace(bashrc_edit_content, "")
        with open(f"{home}/.zshrc", "w") as f:
            f.write(zshrc)
    print("notify has been succesfully uninstalled.")

def ntf_credentials():
        
    prev_not_saved = False
    with open(std_config_path, "r") as f:
        prev_not_saved = f.read() == "none"
    print(f"Credentials location: {std_config_path}")
    if prev_not_saved:
        print("No credentials saved.")
    choice = input("Continue using this configuration? [y/n]: ")
    while choice not in ("y", "n"):
        choice = input(f"{command_error}Continue using this configuration? [y/n]: ")

    if choice == "n":
        if prev_not_saved:
            choice = input(f"Store credentials? [y to store the credentials /n to not store credentials /q to quit]: ")
        else:
            choice = input(f"Change credentials? [y to change credentials /n to not have credentials saved /q to quit]: ")
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
            if not prev_not_saved:
                print(f"Removing credentials from {std_config_path}...")
            conf_file = open(std_config_path, "w")
            conf_file.write("none")
            conf_file.close()
        else:
            print("No change has been done.")


version = "notify version: 1.7.1"

command_error = "Command not recognised.\n"
error = """
Notify error: wrong arguments.
Use notify -h or notify -help to get instructions.
"""

bashrc_edit_title = "#notify - zanzi"
bashrc_edit_content = """alias notify='python3 $HOME/.notify_zanz/notify_app.py'
export PYTHONPATH=$HOME/.notify_zanz/python_module
"""

map = {"-p":"photo", "-d":"document", "-a":"audio", "-v":"video"}

home = os.path.expanduser('~')
base_path = os.path.dirname(os.path.abspath(__file__))
std_config_path = f"{home}/.zanz_notify_config"
files = ["notify.py", "notify_app.py", "change_log.md", "readme.md"]


if __name__ == "__main__":
    main()