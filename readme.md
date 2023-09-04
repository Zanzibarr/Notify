# Telegram_Python_Notifier
This python application, will send messages on telegram, to the chat id specified, from the bot specified by the token.  
Currently it is configured to send text messages, markdown text messages, documents, photos, video and audio.  

Feel free to suggest us new improvements or to report some bugs/problems by opening an <a href="https://github.com/Zanzibarr/Telegram_Python_Notifier/issues">Issue</a>.  

#### STILL ADDING FEATURES

# Configuration
Clone this repo into a folder of your choice (the folder must be kept into the system for the app to work).  

To create your bot and view his token you can use the @BotFather (follow this <a href="https://www.youtube.com/watch?v=aNmRNjME6mE">tutorial</a>); to see your chat id you can use the @RawDataBot (follow this <a href="https://www.youtube.com/watch?v=UPC5Ck1oU6k">tutorial</a>).  
Once you created your bot, start a chat with it (without this step, the application will run, but you won't recieve any message).  

Firstly, open a terminal inside the cloned folder and run the command  
```shell
python3 setup.py
```

You will also need to add a line at the .bashrc file into you home directory:
```shell
sudo nano ~/.bashrc
```
At the end of the file you will need to add
```shell
alias notify='python3 path/to/file/notify_app.py
```
The path you will need to use is the location of the cloned repo.  

Once you're done, reboot and you will be ready to go!

# Update build
To get the latest version of notify, open a terminal inside a folder that's NOT INSIDE nor is the base_folder (u can see the base folder at the bottom of the -h response)
```shell
notify -update <update_type>
```
Please read the instructions to understand the <update_type> functionality:
```shell
notify -h
```

Remember to change the path into the ~/.bashrc file if you decide to move the notify_app.py file.  

# Python lib use
You can use the application as a python library:
```python
import notify
```

First of all, you must setup the bot token and chat id:
```python
notify.set_env(token="your_bot_token", i_chat_id="your_chat_id")
```

Then you can use all the methods from the library.  

# Command line use
Open a terminal and write:
```shell
notify -h
```
to get the list of commands.

# Uninstall
To uninstall just delete your repo and remove the line added to the ~/.bashrc file.  

# Credits
Authors: <a href="https://github.com/Zanzibarr">@Zanzibarr</a> <a href="https://github.com/RickSrick">@RickSrick</a>
