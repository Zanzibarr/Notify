import subprocess, shlex, json, os, notify

command_error = "Command not recognised.\n"
setup_error = f"{command_error}Exiting setup."

home = os.path.expanduser('~')
base_path = os.path.dirname(os.path.abspath(__file__))
std_config_path = f"{home}/.zanz_notify_profiles"
old_config_path = f"{home}/.zanz_notify_config"
dest_path = f"{home}/.notify_zanz"

bashrc_edit = """#notify - zanzi
alias notify='python3 $HOME/.notify_zanz/notify_app.py'
export PYTHONPATH=$HOME/.notify_zanz/python_module
"""

print("\nThanks for downloading notify!\n\nBase repo: https://github.com/Zanzibarr/Telegram_Python_Notifier\nScript made by @Zanzibarr and @RickSrick.\nBeginning setup...\n")

if os.path.exists(std_config_path):

    profiles = json.loads(open(std_config_path, "r").read())

    names = [i for i in profiles["profiles"].keys()]

    print(f"Found a configuration file.\nList of profiles available: {names}.")
    choice = input("Insert the name of the profile to load, '-none' if you wish to not load any profile or '-new' if you wish to create a new one: ")

    while choice not in names and choice != "-none" and choice != "-new":
        choice = input("Command not recognised.\nInsert the name of the profile to load, '-none' if you wish to not load any profile or '-new' if you wish to create a new one: ")

    if choice == "-none":
        print("No profile loaded, remember to specify the token or a profile each time (see the help function).")

    elif choice == "-new":
        print("Creating a new profile.")
        name = input("Insert the name of the profile to create: ")
        token = input("Insert the token of the profile to create: ")
        notify.write_conf_profile(name=name, token=token)
        print("Profile created.\nYou can edit configuration parameters later on using notify (use the help function).")
    
    else:
        name = choice

    profiles["def"] = name

    with open(std_config_path, "w") as f:
        f.write(json.dumps(profiles, indent=4))

else:
    
    choice = "n"
    if os.path.exists(old_config_path):

        choice = input(f"Found a configuration file ({old_config_path}) from a past version.\nUse that configuration to create a default profile? [y/n/q to quit]: ")
        while choice not in ("y", "n", "q"):
            choice = input("Command not recognised.\nUse that configuration to create a default profile? [y/n/q to quit]: ")

        if choice == "q":
            print("notify not installed.\nExiting setup.")
            exit(0)

        if choice == "y":
            with open(old_config_path, "r") as f:
                conf = json.loads(f.read())
                notify.write_conf_profile(name="default", token=conf["token"], to_chat_id=conf["chatid"])

    if choice == "n":

        choice = input("Do you wish to create a profile to store in the configuration file? [y/n/q to quit]: ")
        while choice not in ("y", "n", "q"):
            choice = input("Command not recognised.\nCreating a profile to store in the configuration file? [y/n/q to quit]: ")

        if choice == "q":
            print("notify not installed.\nExiting setup.")

        elif choice == "n":
            print("No profile loaded, remember to specify the token each time or create a new profile.")

        else:
            print("Creating a new profile.")
            name = input("Insert the name of the profile to create: ")
            token=input("Insert the token of the profile to create: ")
            notify.write_conf_profile(name=name, token=token)
            with open(std_config_path, "r") as f:
                profiles = json.loads(f.read())
            profiles["def"] = name
            with open(std_config_path, "w") as f:
                f.write(json.dumps(profiles, indent=4))

            print("Profile created.\nYou can edit configuration parameters later on using notify (use the help function).")

    choice = input(f"Removing old credentials file ({old_config_path})? [y/n]: ")
    while choice not in ("y", "n"):
        choice = input(f"Command not recognised.\nRemoving old credentials file ({old_config_path})? [y/n]: ")

    if choice == "y":
        subprocess.run(shlex.split(f"rm {old_config_path}"))

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

# EDITING BASHRC AND/OR ZSHRC
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

# REMOVING CLONED REPO
choice = input(f"To remove the temporary folder {base_path}, the setup will need to have root permission.\nWish to remove automatically this folder? [y/n]: ")
while choice not in ("y", "n"):
    choice = input(f"{command_error}Continue anyway? [y/n]: ")
if choice == "y":
    print("Removing temporary files...")
    subprocess.run(shlex.split(f"sudo rm -r {base_path}"))

print("Setup completed.")
