# Telegram_Python_Notifier
This python application, will send messages on telegram, to the chat id specified, from the bot specified by the token.  

# Configuration
Clone this repo into a folder of your choice (the folder must be kept into the system for the app to work).  

To create your bot and view his token you can use the @BotFather (follow this <a href="https://www.youtube.com/watch?v=aNmRNjME6mE">tutorial</a>); to see your chat id you can use the @RawDataBot (follow this <a href="https://www.youtube.com/watch?v=UPC5Ck1oU6k">tutorial</a>).  
Once you created your bot, start a chat with it.  

Make sure to fill your info about your telegram bot and chat id into the <a href="https://github.com/Zanzibarr/Telegram_Python_Notifier/blob/main/notify_app.py">notify_app.py</a> file.  

Open a terminal inside the cloned folder and run the command  
```shell
sudo python3 setup.py develop
```

Now you're ready to go!

# Edit build

If you edit some files and want to build the application again, you have to locate the build first and delete it.

To locate the current build you can use the command  
```shell
whereis notify
```
then  
```shell
sudo rm /path/to/file/notify
```

<<<<<<< HEAD
Once you've done this, you're ready to edit your files and build again.
=======
Once you've done this, you're ready to build again.  
>>>>>>> dcde0ff77c72ea3cf7cd021481a746b1d54c1d9e

# Python lib use
You can use the application as a python library:
```python
import notify

notify.set_env(token="your_bot_token", i_chat_id="your_chat_id") # Remember to use this method before calling any other method
notify.send_text("Hello, this is an automated message")
notify.send_document("url_to_doc")
```

# Command line use
After the configuration, you can call from command line the notify app using 1+ argumends as the text to be sent.  
Es:
```shell
notify Hello, this is an automated message
```
The message recieved on telegram shall be "Hello, this is an automated message"

# Credits
Authors: <a href="https://github.com/Zanzibarr">@Zanzibarr</a> <a href="https://github.com/RickSrick">@RickSrick</a>
