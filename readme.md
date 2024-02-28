
## Telegram Python Notifier
This python application, will send messages on telegram, to the chat id specified, from the bot specified by the token.  
Currently it is configured to send text messages, markdown text messages, documents, photos, video and audio.  

Current version: 2.0.1  

Feel free to suggest us new improvements or to report some bugs/problems by opening an <a target="_blank" href="https://github.com/Zanzibarr/Telegram_Python_Notifier/issues">Issue</a>.  

## Configuration
To create your bot and view his token you can use the @BotFather (follow this <a target="_blank" href="https://www.youtube.com/watch?v=aNmRNjME6mE">tutorial</a>); to see your chat id you can use the @RawDataBot (follow this <a target="_blank" href="https://www.youtube.com/watch?v=UPC5Ck1oU6k">tutorial</a>).  
Once you created your bot, start a chat with it (without this step, the application will run, but you won't recieve any message).  

Make sure you have already installed the requests module:
```shell
python3 pip -m install requests
```
To download and install properly notify, open a terminal and run the command  
```shell
git clone https://github.com/Zanzibarr/Telegram_Python_Notifier temp_notify_zanz/ && python3 temp_notify_zanz/setup.py
```

Once you're done you will be ready to go (on a freshly opened terminal)  

This setup works by editing the ~/.bashrc (or ~/.zshrc) file.  

Please note that notify will work only on python3, if you wish you can change the setup.py and notify_app.py by replacing all python3 commands with python commands.  

If any problems occur, let me know by opening an <a target="_blank" href="https://github.com/Zanzibarr/Telegram_Python_Notifier/issues">Issue</a>.  

## Update build
We suggest you to read the <a target="_blank" href="https://github.com/Zanzibarr/Telegram_Python_Notifier/blob/main/change_log.md">change_log</a> before updating!  
To get the latest version of notify:
```shell
notify -update
```

## Python lib use
You can use the application as a python library:
```python
import notify
```

First of all, you must setup the bot token and chat id:
```python
bot = notify(token="your_bot_token")
```

Then you can use all the methods from the library.  

You can now create new profiles and use the to re-use bot configurations and parameters.  

## Command line use
Open a terminal and write:
```shell
notify -h
```
to get the list of commands.

## Uninstall
To uninstall just run the command
```shell
notify -uninstall
```

## Credits
Authors: <a target="_blank" href="https://github.com/Zanzibarr">@Zanzibarr</a> <a target="_blank" href="https://github.com/RickSrick">@RickSrick</a>
