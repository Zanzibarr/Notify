#!/usr/bin/python3

import setuptools, os

setup_error = "Command not recognised.\nExiting setup."
std_config_path = "/etc/zanz_notify_config"
base_path = os.path.dirname(__file__)

credentials = "credentials = 0"
done = False

print("\nThanks for installing notify!\n\nBase repo: https://github.com/Zanzibarr/Telegram_Python_Notifier\nScript made by @Zanzibarr and @RickSrick.")
print("\nBeginning setup...\n")

if os.path.exists(std_config_path):
    load_conf_in = input(f"Found config file ({std_config_path}).\nLOAD THIS CONFIGURATION? [y/n /q to quit]: ")
    while load_conf_in not in ("y", "n", "q"):
        load_conf_in = input("Command not recognised.\nLOAD THIS CONFIGURATION? [y/n /q to quit]: ")
        
    if load_conf_in == "q":
        print("Exiting setup.")
        exit(0)
    elif load_conf_in == "y":
        credentials = "credentials = json.load(open('"+std_config_path+"', 'r'))"
        done = True

if not done:
    setup_mode = input(f"Wish to store the credentials?\nStoring the credentials writes them on plain text inside the config file ({std_config_path}).\nIf you choose not to store them you will be asked to insert the credentials each time.\nSTORE THE CREDENTIALS? [y/n /q to quit]: ")

    while setup_mode not in ("y", "n", "q"):
        setup_mode = input("Command not recognised.\nLOAD THIS CONFIGURATION? [y/n /q to quit]: ")
    
    if setup_mode == "q":
        print("Exiting setup.")
        exit(0)
    elif setup_mode == "y":
        token = input("Insert the token for the bot you want to use: ")
        chat_id = input("Insert the your chat id: ")
        json_cred = '{"token":"'+token+'","chatid":"'+chat_id+'"}'
        conf_file = open(std_config_path, "w")
        conf_file.write(json_cred)
        conf_file.close()
        credentials = "credentials = json.load(open('"+std_config_path+"', 'r'))"
        

with open(f"{base_path}/setup_files/notif_app.py", "r") as f:
    script = f.read()
    
START_IN = "'''>>__EDIT__>>"
END_IN = "<<__EDIT__<<'''"
        
p1, _, r= script.partition(START_IN)
r = r.partition(END_IN)[2]

script = p1+credentials+r

with open(f"{base_path}/notify_app.py", "w") as f:
    f.write(script)

setuptools.setup(
    name="notifier",
    version="1.1",
    packages=setuptools.find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'notify = notify_app:main',
        ],
    },
    include_package_data=True,
)