import subprocess, notify, json, utilities, requests, os

print("\nThanks for downloading notify!\n\nBase repo: https://github.com/Zanzibarr/Notify\nScript made by @Zanzibarr and @RickSrick.\nBeginning setup...\n")

if utilities.home == "/var/root":
    utilities.print_exception("Run the setup in user mode.")

# --- CONFIGURATION FILES ---

if os.path.exists(utilities.std_config_path):

    try:
        with open(utilities.std_config_path, "r") as f:
            profiles = json.loads(f.read())
        names = [name for name in profiles["profiles"].keys()]

        utilities.print_info(f"Found a configuration file.\nList of profiles available: {names}.")
        choice = utilities.print_input(f"{utilities.cmd_input}Insert the name of the profile to load, '-new' if you wish to create a new one or '-q' to exit the installation:{utilities.cmd_end} ")

        while choice not in names and choice not in ("-new", "-q"):
            utilities.print_warning("Command not recognised.")
            choice = utilities.print_input(f"{utilities.cmd_input}Insert the name of the profile to load, '-new' if you wish to create a new one or '-q' to exit the installation:{utilities.cmd_end} ")

        if choice == "-q":
            utilities.print_warning("notify not installed.")
            utilities.print_info("Exiting setup.")
            exit(0)

        if choice == "-new":
            utilities.print_info("Creating a new profile.")
            name = utilities.print_input(f"{utilities.cmd_input}Insert the name of the profile to create:{utilities.cmd_end} ")
            token = utilities.print_input(f"{utilities.cmd_input}Insert the token of the profile to create:{utilities.cmd_end} ")
            chat = utilities.print_input(f"{utilities.cmd_input}Insert the default chat_id to send the message to:{utilities.cmd_end} (or -q to ignore for now) ")
            while not requests.post(f"https://api.telegram.org/bot{token}/getMe").json()["ok"]:
                utilities.print_warning("The token specified isn't associated to a telegram bot, please use a valid token.")
                token=utilities.print_input(f"{utilities.cmd_input}Insert the token of the profile to create (or -q to quit):{utilities.cmd_end} ")

                if token == "-q":
                    utilities.print_warning("notify not installed.")
                    utilities.print_info("Exiting setup.")
                    exit(0)

            chat = "" if chat == "-q" else chat
            notify.write_conf_profile(name=name, token=token, to_chat_id=chat)
        
        else:
            name = choice

        notify.set_default_profile(name=name)
            
        utilities.print_info("Profile created.\nYou can edit configuration parameters later using notify (see the help function).")

    except Exception:

        utilities.print_exception(f"Configuration file has been corrupted.\nCannot proceed to install notify.\nDelete the configuration file {utilities.std_config_path} and run again the setup. (Consider saving somewhere the info in the configuration file if some info are still valuable).")

else:

    choice = "n"
    if os.path.exists(utilities.old_config_path):

        choice = utilities.print_input(f"Found a configuration file ({utilities.old_config_path}) from a past version. {utilities.cmd_input}Use that configuration to create a default profile?{utilities.cmd_end} [y/n/-q to quit]: ")
        while choice not in ("y", "n", "-q"):
            utilities.print_warning("Command not recognised.")
            choice = utilities.print_input(f"{utilities.cmd_input}Use that configuration to create a default profile?{utilities.cmd_end} [y/n/-q to quit]: ")

        if choice == "-q":
            utilities.print_warning("notify not installed.")
            utilities.print_info("Exiting setup.")
            exit(0)

        if choice == "y":
            with open(utilities.old_config_path, "r") as f:
                conf = json.loads(f.read())
                try:
                    notify.write_conf_profile(name="default", token=conf["token"], to_chat_id=conf["chatid"])
                except Exception as e:
                    utilities.print_warning("The token found in the old configuration file isn't associated to a telegram bot. You will need to create manually a new profile.")
                    choice = "n"

    if choice == "n":
            
        utilities.print_info("Creating a new profile.")
        name = utilities.print_input(f"{utilities.cmd_input}Insert the name of the profile to create:{utilities.cmd_end} ")
        token=utilities.print_input(f"{utilities.cmd_input}Insert the token of the profile to create:{utilities.cmd_end} ")
        while not requests.post(f"https://api.telegram.org/bot{token}/getMe").json()["ok"]:
            utilities.print_warning("The token specified isn't associated to a telegram bot, please use a valid token.")
            token=utilities.print_input(f"{utilities.cmd_input}Insert the token of the profile to create (or -q to quit):{utilities.cmd_end} ")

            if token == "-q":
                utilities.print_warning("notify not installed.")
                utilities.print_info("Exiting setup.")
                exit(0)

        notify.write_conf_profile(name=name, token=token)

        with open(utilities.std_config_path, "r") as f:
            profiles = json.loads(f.read())
        profiles["def"] = name
        with open(utilities.std_config_path, "w") as f:
            f.write(json.dumps(profiles, indent=4))

    utilities.print_info("Profile created.\nYou can edit configuration parameters later on using notify (use the help function).")

    if os.path.exists(utilities.old_config_path):
        choice = utilities.print_input(f"{utilities.cmd_input}Removing old credentials file ({utilities.old_config_path})?{utilities.cmd_end} [y/n]: ")
        while choice not in ("y", "n"):
            utilities.print_warning("Command not recognised.")
            choice = utilities.print_input(f"{utilities.cmd_input}Removing old credentials file ({utilities.old_config_path})?{utilities.cmd_end} [y/n]: ")

        if choice == "y":
            subprocess.run(["rm", utilities.old_config_path])


# --- MOVING FILES ---

if not os.path.exists(utilities.dest_path):
    utilities.print_info(f"Folder {utilities.dest_path} not found, creating one.")
    os.mkdir(utilities.dest_path)

utilities.print_info(f"Moving files to base path: {utilities.dest_path}")
for file in utilities.files:
    subprocess.run(["cp", f"{utilities.base_path}/{file}", f"{utilities.dest_path}/{file}"])

if not os.path.exists(f"{utilities.dest_path}/python_module"):
    os.mkdir(f"{utilities.dest_path}/python_module")

subprocess.run(["mv", f"{utilities.dest_path}/notify.py", f"{utilities.dest_path}/python_module/notify.py"])


# --- BASHRC AND ZSHRC EDITS ---

if not os.path.exists(f"{utilities.home}/.bashrc") and not os.path.exists(f"{utilities.home}/.zshrc"):
    utilities.print_warning(f"Couldnt find {utilities.home}/.bashrc nor {utilities.home}/.zshrc.\nTo use notify as a python module: use the module {utilities.dest_path}/python_module/notify.py\n \u21b3 To use notify as a shell command: python3 {utilities.dest_path}/notify_app.py ...")

check_bashrc = False
check_zshrc = False

if os.path.exists(f"{utilities.home}/.bashrc"):
    with open(f"{utilities.home}/.bashrc", "r") as f:
        if utilities.bashrc_edit in f.read():
            check_bashrc = True
    if not check_bashrc:
        utilities.print_info(f"Writing on {utilities.home}/.bashrc file (append)...")
        with open(f"{utilities.home}/.bashrc", "a") as f:
            f.write(utilities.bashrc_edit)
else:
    check_bashrc = True

if os.path.exists(f"{utilities.home}/.zshrc"):
    with open(f"{utilities.home}/.zshrc", "r") as f:
        if utilities.bashrc_edit in f.read():
            check_zshrc = True
    if not check_zshrc:
        utilities.print_info(f"Writing on {utilities.home}/.zshrc file (append)...")
        with open(f"{utilities.home}/.zshrc", "a") as f:
            f.write(utilities.bashrc_edit)
else:
    check_zshrc = True

if not check_zshrc or not check_bashrc:
    utilities.print_warning(f"To use the application now, you will have to open a NEW terminal and use it there.")


# --- REMOVING TEMPORARY FILES ---

utilities.print_warning(f"To remove the temporary folder {utilities.base_path}, the setup will need to have root permission.")
choice = utilities.print_input(f"{utilities.cmd_input}Wish to remove automatically this folder?{utilities.cmd_end} [y/n]: ")
while choice not in ("y", "n"):
    utilities.print_warning("Command not recognised.")
    choice = utilities.print_input(f"{utilities.cmd_input}Wish to automatically remove the folder?{utilities.cmd_end} [y/n]: ")
if choice == "y":
    utilities.print_info("Removing temporary files...")
    subprocess.run(["sudo"], ["rm"], ["-r"], utilities.base_path)

utilities.print_info("Setup completed.")