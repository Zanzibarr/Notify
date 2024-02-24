import subprocess, notify, json, utilities, requests, os

print("\nThanks for downloading notify!\n\nBase repo: https://github.com/Zanzibarr/Telegram_Python_Notifier\nScript made by @Zanzibarr and @RickSrick.\nBeginning setup...\n")


# --- CONFIGURATION FILES ---

if os.path.exists(utilities.std_config_path):

    try:
        with open(utilities.std_config_path, "r") as f:
            profiles = json.loads(f.read())
        names = [name for name in profiles["profiles"].keys()]

        print(f"Found a configuration file.\nList of profiles available: {names}.")
        choice = input("Insert the name of the profile to load or '-new' if you wish to create a new one: ")

        while choice not in names and choice != "-new":
            choice = input("Command not recognised.\nInsert the name of the profile to load, '-none' if you wish to not load any profile or '-new' if you wish to create a new one: ")

        if choice == "-new":
            print("Creating a new profile.")
            name = input("Insert the name of the profile to create: ")
            token = input("Insert the token of the profile to create: ")
            while not requests.post(f"https://api.telegram.org/bot{token}/getMe").json()["ok"]:
                print("The token specified isn't associated to a telegram bot.\nPlease use a valid token.")
                token=input("Insert the token of the profile to create (or q to quit): ")

                if token == "q":
                    print("notify not installed.\nExiting setup.")
                    exit(0)

            notify.write_conf_profile(name=name, token=token)
            print("Profile created.\nYou can edit configuration parameters later on using notify (use the help function).")
        
        else:
            name = choice

        profiles["def"] = name

        with open(utilities.std_config_path, "w") as f:
            f.write(json.dumps(profiles, indent=4))

    except Exception:

        print(f"Configuration file has been corrupted.\nCannot proceed to install notify.\nDelete the configuration file {utilities.std_config_path} and run again the setup. (Consider saving somewhere the info in the configuration file if some info are still valuable).")
        exit(1)

else:

    choice = "n"
    if os.path.exists(utilities.old_config_path):

        choice = input(f"Found a configuration file ({utilities.old_config_path}) from a past version.\nUse that configuration to create a default profile? [y/n/q to quit]: ")
        while choice not in ("y", "n", "q"):
            choice = input("Command not recognised.\nUse that configuration to create a default profile? [y/n/q to quit]: ")

        if choice == "q":
            print("notify not installed.\nExiting setup.")
            exit(0)

        if choice == "y":
            with open(utilities.old_config_path, "r") as f:
                conf = json.loads(f.read())
                try:
                    notify.write_conf_profile(name="default", token=conf["token"], to_chat_id=conf["chatid"])
                except Exception as e:
                    print("The token found in the old configuration file isn't associated to a telegram bot. You will need to create manually a new profile.")
                    choice = "n"

    if choice == "n":
            
        print("Creating a new profile.")
        name = input("Insert the name of the profile to create: ")
        token=input("Insert the token of the profile to create: ")
        while not requests.post(f"https://api.telegram.org/bot{token}/getMe").json()["ok"]:
            print("The token specified isn't associated to a telegram bot.\nPlease use a valid token.")
            token=input("Insert the token of the profile to create (or q to quit): ")

            if token == "q":
                print("notify not installed.\nExiting setup.")
                exit(0)

        notify.write_conf_profile(name=name, token=token)

        with open(utilities.std_config_path, "r") as f:
            profiles = json.loads(f.read())
        profiles["def"] = name
        with open(utilities.std_config_path, "w") as f:
            f.write(json.dumps(profiles, indent=4))

    print("Profile created.\nYou can edit configuration parameters later on using notify (use the help function).")

    choice = input(f"Removing old credentials file ({utilities.old_config_path})? [y/n]: ")
    while choice not in ("y", "n"):
        choice = input(f"Command not recognised.\nRemoving old credentials file ({utilities.old_config_path})? [y/n]: ")

    if choice == "y":
        subprocess.run(["rm", utilities.old_config_path])


# --- MOVING FILES ---

if not os.path.exists(utilities.dest_path):
    print(f"Folder {utilities.dest_path} not found, creating one.")
    os.mkdir(utilities.dest_path)

print(f"Moving files to base path {utilities.dest_path}")
for file in utilities.files:
    subprocess.run(["cp", f"{utilities.base_path}/{file}", f"{utilities.dest_path}/{file}"])

if not os.path.exists(f"{utilities.dest_path}/python_module"):
    print(f"Folder {utilities.dest_path}/python_module not found, creating one.")
    os.mkdir(f"{utilities.dest_path}/python_module")

subprocess.run(["mv", f"{utilities.dest_path}/notify.py", f"{utilities.dest_path}/python_module/notify.py"])


# --- BASHRC AND ZSHRC EDITS ---

if not os.path.exists(f"{utilities.home}/.bashrc") and not os.path.exists(f"{utilities.home}/.zshrc"):
    print(f"Couldnt find {utilities.home}/.bashrc nor {utilities.home}/.zshrc.\nTo use notify as a python module: use the module {utilities.dest_path}/python_module/notify.py\nTo use notify as a shell command: python3 {utilities.dest_path}/notify_app.py ...")

check_bashrc = False
check_zshrc = False

if os.path.exists(f"{utilities.home}/.bashrc"):
    with open(f"{utilities.home}/.bashrc", "r") as f:
        if utilities.bashrc_edit in f.read():
            check_bashrc = True
    if not check_bashrc:
        print(f"Writing on {utilities.home}/.bashrc file (append)...")
        with open(f"{utilities.home}/.bashrc", "a") as f:
            f.write(utilities.bashrc_edit)
else:
    check_bashrc = True

if os.path.exists(f"{utilities.home}/.zshrc"):
    with open(f"{utilities.home}/.zshrc", "r") as f:
        if utilities.bashrc_edit in f.read():
            check_zshrc = True
    if not check_zshrc:
        print(f"Writing on {utilities.home}/.zshrc file (append)...")
        with open(f"{utilities.home}/.zshrc", "a") as f:
            f.write(utilities.bashrc_edit)
else:
    check_zshrc = True

if not check_zshrc or not check_bashrc:
    print(f"[ATTENTION]: To use the application now, you will have to open a NEW terminal and use it there.")


# --- REMOVING TEMPORARY FILES ---

choice = input(f"To remove the temporary folder {utilities.base_path}, the setup will need to have root permission.\nWish to remove automatically this folder? [y/n]: ")
while choice not in ("y", "n"):
    choice = input("Input not recognised.\nWish to automatically remove the folder? [y/n]: ")
if choice == "y":
    print("Removing temporary files...")
    subprocess.run(["sudo"], ["rm"], ["-r"], utilities.base_path)

print("Setup completed.")