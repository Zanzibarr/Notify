import subprocess, shlex, sys, os

command_error = "Command not recognised.\n"
setup_error = f"{command_error}Exiting setup."

home = os.path.expanduser('~')
base_path = os.path.dirname(os.path.abspath(__file__))
std_config_path = f"{home}/.zanz_notify_config"
dest_path = f"{home}/.notify_zanz"

bashrc_edit = """#notify - zanzi
alias notify='python3 $HOME/.notify_zanz/notify_app.py'
export PYTHONPATH=$HOME/.notify_zanz/python_module
"""

# CHECK IF IT'S A SETUP OR AN UPDATE
update = len(sys.argv) == 2 and sys.argv[1] == "-update"

if not update:
    print("\nThanks for downloading notify!\n\nBase repo: https://github.com/Zanzibarr/Telegram_Python_Notifier\nScript made by @Zanzibarr and @RickSrick.")

print("\nBeginning setup...\n")

# LOAD PREVIOUS CONFIGURATION IF FOUND
check = False
if os.path.exists(std_config_path):
    choice = input(f"Found config file inside {std_config_path}.\nIf the config file contains 'none', you will be asked the credentials each time you use notify.\nUSE THIS CONFIGURATION? [y/n /q to quit]: ")
    while choice not in ("y", "n", "q"):
        choice = input(f"{command_error}USE THIS CONFIGURATION? [y/n /q to quit]: ")
        
    if choice == "q":
        print("notify not installed/updated.\nExiting setup.")
        exit(0)

    elif choice == "y":
        check = True

# IF CONFIGURATION WASNT LOADED
if not check:
    choice = input(f"Wish to store the credentials?\nStoring the credentials writes them on plain text inside the config file ({std_config_path}).\nIf you choose not to store them you will be asked the credentials each time you use notify.\nSTORE THE CREDENTIALS? [y/n /q to quit]: ")
    while choice not in ("y", "n", "q"):
        choice = input(f"{command_error}STORE THE CREDENTIALS? [y/n /q to quit]: ")
    
    if choice == "q":
        print("notify not installed/updated.\nExiting setup.")
        exit(0)

    elif choice == "y":
        token = input("Insert the token for the bot you want to use: ")
        chat_id = input("Insert the your chat id: ")
        print(f"Storing credentials inside {std_config_path}...")
        json_cred = '{"token":"'+token+'","chatid":"'+chat_id+'"}'
        conf_file = open(std_config_path, "w")
        conf_file.write(json_cred)
        conf_file.close()

    else:
        conf_file = open(std_config_path, "w")
        conf_file.write("none")
        conf_file.close()

# CREATE DESTINATION PATH
if not os.path.isdir(f"{dest_path}"):
    os.mkdir(f"{dest_path}")
if not os.path.isdir(f"{dest_path}/python_module"):
    os.mkdir(f"{dest_path}/python_module")

# MOVING FILES TO DESTINATION PATH
print(f"Moving files to base path ({dest_path})")
subprocess.run(shlex.split(f"cp {base_path}/notify.py {dest_path}/python_module/notify.py"))
subprocess.run(shlex.split(f"cp {base_path}/notify_app.py {dest_path}/notify_app.py"))
subprocess.run(shlex.split(f"cp {base_path}/change_log.md {dest_path}/change_log.md"))
subprocess.run(shlex.split(f"cp {base_path}/readme.md {dest_path}/readme.md"))

#EDITING BASHRC AND/OR ZSHRC
if not os.path.exists(f"{home}/.bashrc") and not os.path.exists(f"{home}/.zshrc"):
    print(f"Couldnt find {home}/.bashrc nor {home}/.zshrc.\nnotify files can still be used manually.\nLocation: {dest_path}")

check_bashrc = False
check_zshrc = False

if os.path.exists(f"{home}/.bashrc"):
    with open(f"{home}/.bashrc", "r") as f:
        if bashrc_edit in f.read():
            check_bashrc = True
    if not check_bashrc:
        print(f"Writing on {home}/.bashrc file (append)...")
        with open(f"{home}/.bashrc", "a") as f:
            f.write(bashrc_edit)
else:
    check_bashrc = True

if os.path.exists(f"{home}/.zshrc"):
    with open(f"{home}/.zshrc", "r") as f:
        if bashrc_edit in f.read():
            check_zshrc = True
    if not check_zshrc:
        print(f"Writing on {home}/.zshrc file (append)...")
        with open(f"{home}/.zshrc", "a") as f:
            f.write(bashrc_edit)
else:
    check_zshrc = True

if not check_zshrc or not check_bashrc:
    print(f"[ATTENTION]: To use notify now, you will have to open a NEW terminal and use it there.")

if not update:
    choice = input(f"To remove the folder {base_path}, the setup will need to have root permission. Continue anyway? [y/n]: ")
    while choice not in ("y", "n"):
        choice = input(f"{command_error}Continue anyway? [y/n]: ")
    if choice == "y":
        print("Removing temporary files...")
        subprocess.run(shlex.split(f"sudo rm -r {base_path}"))

print("Setup completed.")
