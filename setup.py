#!/usr/bin/python3

import setuptools, json

print("Thanks for installing notify!\nBase repo: https://github.com/Zanzibarr/Telegram_Python_Notifier\nScript made by @Zanzibarr and @RickSrick.")
print("\nBeginning setup...")

setup_mode = ""

while setup_mode not in ("y", "n", "q"):
    setup_mode = input("Wish to store the credentials?\nStoring the credentials writes them on plain text inside the notify_app.py file.\nIf you choose not to store them you will be asked to insert the credentials each time.\nSTORE THE CREDENTIALS? [y/n /q to exit]: ")

if setup_mode == "q":
    print("Exiting setup.")
    exit(0)
elif setup_mode == "y":
    js_choice = input("""
If you have a file with the credentials stored as a json you can specify the path to that file and read the credentials from that file.
IF YOU DONT HAVE ONE, select no and input the credentials manually in the next steps.
Accepted json format:
{'token':'your_token', 'chatid':'your_chat_id'}
USE A JSON FILE? [y/n]: """)
    if js_choice not in ("y", "n"):
        print("Command not recognised.\nExiting setup.")
        exit(0)
    if js_choice == "y":
        path = input("Please give us the absolute path to the json file with the credentials: ")
        file = open(path, "r")
        credentials = json.load(file)
        token = credentials["token"]
        chat_id = credentials["chatid"]
    else:
        token = input("Insert the token for the bot you want to use: ")
        chat_id = input("Insert the your chat id: ")
else:
    token = "{input('Insert the token for the bot you want to use: ')}"
    chat_id = "{input('Insert the your chat id: ')}"

with open("setup_files/notif_app.py", "r") as f:
    script = f.read()
    
START_IN = ">>__EDIT__>>"
END_IN = "<<__EDIT__<<"
        
p1, _, r= script.partition(START_IN)
r = r.partition(END_IN)[2]
p2, _, r = r.partition(START_IN)
r = r.partition(END_IN)[2]

script = p1+token+p2+chat_id+r

with open("notify_app.py", "w") as f:
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