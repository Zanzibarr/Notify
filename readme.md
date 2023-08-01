# Configuration
Clone this repo into a folder of your choice.  
Make sure to fill your info about your telegram bot and chat id into the notifier.py file.  
To create your bot and view his token you can use the @BotFather; to see your chat id you can use the @RawDataBot (follow this <a href="https://www.youtube.com/watch?v=UPC5Ck1oU6k">tutorial</a>).  
Open a terminal inside the cloned folder and run the command  
```shell
sudo python3 setup.py develop
```
After running this command, you should be ready to use the Notify command everywhere on your computer.

# Use
After the configuration, you can call from command line the notify app using 1+ argumends as the text to be sent.  
Es:
```shell
notify Hello, this is an automated message
```
The message recieved on telegram shall be "Hello, this is an automated message"
