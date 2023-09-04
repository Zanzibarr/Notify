#!/usr/bin/python3

import setuptools

print("Thanks for installing notify!\nBase repo: https://github.com/Zanzibarr/Telegram_Python_Notifier\nScript made by @Zanzibarr and @RickSrick.")
print("\nBeginning setup...")

setup_mode = ""

while setup_mode not in ("y", "n", "q"):
    setup_mode = input("You wish to save the credentials?\nStoring the credentials writes them on plain text inside the notify_app.py file.\nIf you choose not to store them you will be asked to insert the credentials each time.\nStore the credentials? [y/n /q to exit]: ")

if setup_mode == "q":
    print("Exiting setup.")
    exit(0)
elif setup_mode == "y":
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