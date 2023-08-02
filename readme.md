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

Once you've done this, you're ready to edit your files and build again.

# Python lib use
You can use the application as a python library:
```python
import notify

notify.set_env(token="your_bot_token", i_chat_id="your_chat_id") # Remember to use this method before calling any other method
notify.send_text("Hello, this is an automated message")
notify.send_document("url_to_doc")
```

# Command line use
Commands accepted:
```shell
notify <type> <content>
```
The content could be missing in some cases.

> notify -h / > notify -help
    Prints the instructions
> notify -t This is a text message
    Sends the full message followed by '-t' (message -> This is a text message)
> notify -m <media_type> url
    Sends a media located in the url specified.
    media_type:
        photo (> notify -m photo /path/to/photo.png)
        document (> notify -m document /path/to/document.txt)
        audio (> notify -m audio /path/to/audio.mp3)
        video (> notify -m video /path/to/video.mp4)
> notify -p url
    Sends a photo located in the url specified (is the same of > notify -m photo url)
> notify -d url
    Sends a document located in the url specified (is the same of > notify -m document url)
> notify -a url
    Sends an audio located in the url specified (is the same of > notify -m audio url)
> notify -v url
    Sends a video located in the url specified (is the same of > notify -m video url)


# Credits
Authors: <a href="https://github.com/Zanzibarr">@Zanzibarr</a> <a href="https://github.com/RickSrick">@RickSrick</a>
