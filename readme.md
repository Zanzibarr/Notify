
## Telegram Python Notifier
This python application, will send messages on telegram, to the chat id specified, from the bot specified by the token.  
Currently it is configured to send text messages, markdown text messages, documents, photos, video and audio.  

Current version: 2.4  

Feel free to suggest us new improvements or to report some bugs/problems by opening an <a target="_blank" href="https://github.com/Zanzibarr/Telegram_Python_Notifier/issues">Issue</a>.  

### WORKS FOR LINUX AND MACOS

## Configuration
To create your bot and view his token you can use the @BotFather (follow this <a target="_blank" href="https://www.youtube.com/watch?v=aNmRNjME6mE">tutorial</a>); to see your chat id you can use the @RawDataBot (follow this <a target="_blank" href="https://www.youtube.com/watch?v=UPC5Ck1oU6k">tutorial</a>).  
Once you created your bot, start a chat with it (without this step, the application will run, but you won't recieve any message).  

Make sure you have already installed the requests module:
```shell
> python3 pip -m install requests
```
To download and install properly notify, open a terminal and run the following commands  
```shell
> git clone https://github.com/Zanzibarr/Telegram_Python_Notifier temp_notify_zanz/
> python3 temp_notify_zanz/setup.py
```

Once you're done you will be ready to go (on a freshly opened terminal)  

This setup works by editing the ~/.bashrc (or ~/.zshrc) file.  

Please note that notify will work only on python3, if you wish you can change the setup.py and notify_app.py by replacing all python3 commands with python commands.  

If any problems occur, let me know by opening an <a target="_blank" href="https://github.com/Zanzibarr/Telegram_Python_Notifier/issues">Issue</a>.  

## Update build
We suggest you to read the <a target="_blank" href="https://github.com/Zanzibarr/Telegram_Python_Notifier/blob/main/change_log.md">change_log</a> before updating!  
To get the latest version of notify:
```shell
> notify -update
```

## Python lib use
[Python lib use](docs/python_use.md)

## Command line use
[Command line use](docs/cmd_use.md)

## Uninstall
To uninstall just run the command
```shell
> notify -uninstall
```
Uninstalling notify won't remove the configuration file located at
```shell
~/.zanz_notify_profiles
```
To remove those too just write
```shell
> rm ~/.zanz_notify_profiles
```

## Credits
Authors: <a target="_blank" href="https://github.com/Zanzibarr">@Zanzibarr</a> <a target="_blank" href="https://github.com/RickSrick">@RickSrick</a>
