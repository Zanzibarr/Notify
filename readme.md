# Telegram_Python_Notifier
This python application, will send messages on telegram, to the chat id specified, from the bot specified by the token.  
Currently it is configured to send text messages, markdown text messages, documents, photos, video and audio.  

Feel free to suggest us new improvements or to report some bugs/problems by opening an <a href="https://github.com/Zanzibarr/Telegram_Python_Notifier/issues">Issue</a>.  

#### STILL ADDING FEATURES

# Configuration
Clone this repo into a folder of your choice (the folder must be kept into the system for the app to work).  

To create your bot and view his token you can use the @BotFather (follow this <a href="https://www.youtube.com/watch?v=aNmRNjME6mE">tutorial</a>); to see your chat id you can use the @RawDataBot (follow this <a href="https://www.youtube.com/watch?v=UPC5Ck1oU6k">tutorial</a>).  
Once you created your bot, start a chat with it (without this step, the application will run, but you won't recieve any message).  

If you dont have done it already, you will have to install pip:
```shell
sudo apt install python3-pip
```

You won't need to edit any file, just open a terminal inside the cloned folder and run the command  
```shell
sudo python3 setup.py develop
```

Follow the steps and then you're ready to go!

# Update build
To get the latest version of notify you can simply run the command
```shell
notify -update <type>
```
Please read the instructions to understand the <type> functionality:
```shell
notify -h
```
If you edit some files and want to build the application again, you just have to run the configuration again (you must be inside the cloned repo):
```shell
sudo python3 setup.py develop
```

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
To uninstall
```shell
sudo rm /usr/local/bin/notify
```
If the executable is not there, u can find it with
```shell
whereis notify
```
and remove it with the previous command (using the path returned by the whereis).

Then remove the cloned repo and you succesfully uninstalled the application.

# Credits
Authors: <a href="https://github.com/Zanzibarr">@Zanzibarr</a> <a href="https://github.com/RickSrick">@RickSrick</a>
