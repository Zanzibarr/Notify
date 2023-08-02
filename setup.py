#!/usr/bin/python3

import setuptools

token = input("Insert the token for the bot you want to use: ")
chat_id = input("Insert the your chat id: ")

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