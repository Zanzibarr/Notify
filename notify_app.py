import subprocess, utilities, notify, shlex, json, sys, os

def main():

    global command

    try:
        
        if len(sys.argv)==1:
            print(utilities.error)
            exit(1)

        elif sys.argv[1] == utilities.HELP:
            if len(sys.argv) not in (2, 3):
                print(utilities.error)
                exit(1)

            help()
            exit(0)

        elif sys.argv[1] == utilities.UPDATE:
            if len(sys.argv) not in (2, 3):
                print(sys.argv)
                print(utilities.error)
                exit(1)

            ntf_update()
            exit(0)

        elif sys.argv[1] == utilities.UNINSTALL:
            if len(sys.argv) > 2:
                print(utilities.error)
                exit(1)

            ntf_uninstall()
            exit(0)

        elif sys.argv[1] == utilities.VERSION:
            if len(sys.argv) > 2:
                print(utilities.error)
                exit(1)

            print(utilities.version)
            exit(0)

        elif sys.argv[1] == utilities.CONF:
            
            command = " ".join(sys.argv[1:])
            ntf_config()

            if len(command.strip()) > 0:
                print(f"\nIgnored parts of the input: {command}\n{utilities.suggestion}\n")

            exit(0)

        command = " ".join(sys.argv[1:])

        if sys.argv[1] == utilities.PROFILE:

            ntf_profile()
            
        ntf_send()
        
        if len(command.strip()) > 0:
            print(f"\nMessage sent successfully.\nIgnored parts of the input: {command}\n{utilities.suggestion}\n")

    except Exception as e:
        print(e)

def ntf_config():

    global command
    
    command = command[6:]

    if command == "":
        print(utilities.conf_file_info)
        exit(0)

    type = command.partition(" ")[0]

    if type == utilities.ADD:

        name = get(utilities.ADD)
        token = get(utilities.TOKEN)

        if name == "" or token == "":
            print(utilities.add_conf_error)
            exit(1)

        notify.write_conf_profile(name=name, token=token, from_chat_id=get(utilities.FROM_CHAT_ID), to_chat_id=get(utilities.CHAT_ID), disable_web_page_preview=get(utilities.DISABLE_WEB_PAGE_PREVIEW), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), parse_mode=get(utilities.PARSE_MODE))
        
    elif type == utilities.REMOVE:

        name = get(utilities.REMOVE)

        notify.remove_profile(name)

    elif type == utilities.SET:

        name = get(utilities.SET)

        if name == "":
            print(utilities.set_conf_error)
            exit(1)

        with open(utilities.std_config_path, "r") as f:
            profiles = json.loads(f.read())
        
        if name not in [i for i in profiles["profiles"].keys()]:
            print("The name specified was not found in the profiles configuration file.\nNot changing the default profile.")
            exit(0)

        profiles["def"] = name

        with open(utilities.std_config_path, "w") as f:
            f.write(json.dumps(profiles, indent=4))

    elif type == utilities.SEE:

        get(utilities.SEE)

        print(json.dumps(notify.get_profiles(), indent=4))

    else:

        print(utilities.command_error)
        exit(1)

def ntf_profile():

    global command

    token = get(utilities.TOKEN)
    profile = get(utilities.PROFILE)

    if profile == "" and token == "":
        print(utilities.profile_error)
        exit(1)

    bot.load_profile(token=token, name=profile)

def ntf_send():

    type = command.partition(" ")[0]

    if type == utilities.TEXT:

        content = get(utilities.TEXT)

        if content == "":
            print(utilities.message_error)
            exit(1)

        if ispath(content):
            response = bot.send_message_by_file(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), parse_mode=get(utilities.PARSE_MODE), disable_web_page_preview=get(utilities.DISABLE_WEB_PAGE_PREVIEW), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY))
        else:
            response = bot.send_message_by_text(text=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), parse_mode=get(utilities.PARSE_MODE), disable_web_page_preview=get(utilities.DISABLE_WEB_PAGE_PREVIEW), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY))

    elif type == utilities.PHOTO:

        content = get(utilities.PHOTO)

        if content == "":
            print(utilities.photo_error)
            exit(1)

        response = bot.send_photo_by_path(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), has_spoiler=get(utilities.HAS_SPOILER), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY))
        
    elif type == utilities.AUDIO:

        content = get(utilities.AUDIO)

        if content == "":
            print(utilities.audio_error)
            exit(1)

        response = bot.send_audio_by_path(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), duration=get(utilities.DURATION), performer=get(utilities.PERFORMER), title=get(utilities.TITLE), thumbnail=get(utilities.THUMBNAIL), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY))

    elif type == utilities.DOCUMENT:

        content = get(utilities.DOCUMENT)

        if content == "":
            print(utilities.doc_error)
            exit(1)

        response = bot.send_document_by_path(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), thumbnail=get(utilities.THUMBNAIL), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), disable_content_type_detection=get(utilities.DISABLE_CONTENT_TYPE_DETECTION), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY))

    elif type == utilities.VIDEO:

        content = get(utilities.VIDEO)

        if content == "":
            print(utilities.video_error)
            exit(1)

        response = bot.send_video_by_path(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), duration=get(utilities.DURATION), width=get(utilities.WIDTH), height=get(utilities.HEIGHT), thumbnail=get(utilities.THUMBNAIL), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), has_spoiler=get(utilities.HAS_SPOILER), supports_streaming=get(utilities.SUPPORTS_STREAMING), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY))

    elif type in utilities.EXCEPTION:

        response = bot.send_exception(text=get(utilities.EXCEPTION), chat_id=get(utilities.CHAT_ID))

    else:
        print(utilities.command_error)
        exit(1)    

    if not response["ok"]:
        print(f"Something went wrong:\n{response}")

def ispath(content):
    return os.path.exists(content)

def get(type):

    global command

    index = command.find(f"-{type}")

    if index < 0:
            
        index = command.find(type)
        
        if index < 0: return ""
        c_len = command[index+1:].find("-")
        if c_len < 0:
            cut = len(command)
        else:
            cut = index + 1 + c_len

        content = command[index+1+len(type):cut]
        command = command[:index]+command[cut:]
        
        return content.strip()
    
    else:

        if type not in utilities.SHORTCUT_COMMANDS:
            print(utilities.error)
            exit(1)
            
        c_len = command[index+2:].find("-")
        if c_len < 0:
            cut = len(command)
        else:
            cut = index + 2 + c_len
        command = command[:index]+command[cut:]
        
        return True


def help():

    if len(sys.argv) == 2:
        message = f"""the list of commands allowed with their explaination.
          
CONFIGURATION COMMANDS:

> notify {utilities.HELP}
    Prints the instructions
    You can add at the end the type of notify command you need help with
    To see the description of ALL parameters that can be used, use {utilities.PARAMETERS}

    Es: notify {utilities.HELP} {utilities.TEXT}
    Es: notify {utilities.HELP} {utilities.VIDEO}

> notify {utilities.VERSION}
    See the current notify version

> notify {utilities.UPDATE}
    Download the latest version of notify (please note that after a new version gets published, even if the new version is found, for one or two minutes the updated version might not be downloaded correctly due to the time github needs to update the raw.githubusercontent.com version of the repo...).
    You can add at the end which type of update u prefer:
        > {utilities.PROD} (default) : uploads to the latest tested version
        > {utilities.DEV} : uploads to the latest version under development (not finished, not suggested)

    Es: notify {utilities.UPDATE} {utilities.DEV}
        Requests an update to the latest version under development

> notify {utilities.CONF}
    Print the configuration file location.
    You can add at the end one of those additional commands:
        > {utilities.ADD} <name> {utilities.TOKEN} <token> <other_params> : to add a profile to the configuration file
            <other_params>:
                {utilities.explanation[utilities.FROM_CHAT_ID]}
                {utilities.explanation[utilities.CHAT_ID]}
                {utilities.explanation[utilities.DISABLE_WEB_PAGE_PREVIEW]}
                {utilities.explanation[utilities.DISABLE_NOTIFICATION]}
                {utilities.explanation[utilities.PROTECT_CONTENT]}
                {utilities.explanation[utilities.ALLOW_SENDING_WITHOUT_REPLY]}
                {utilities.explanation[utilities.PARSE_MODE]}
            <other_params> can be omitted if you wish to use the default/selected profile ones
        > {utilities.REMOVE} <name> : removes a profile from the configuration file
        > {utilities.SET} <name> : sets the default profile for command line use
        > {utilities.SEE} : prints the content of the configuration file

    Es: notify {utilities.CONF} {utilities.SEE}
        Shows all configurations currently saved
    Es: notify {utilities.CONF} {utilities.ADD} test_name {utilities.TOKEN} valid_bot_token {utilities.PARSE_MODE} MarkdownV2 {utilities.DISABLE_NOTIFICATION} true
        Creates/Edits the profile named test_name setting the parameters token, parse_mode and disable_notification

> notify {utilities.UNINSTALL}
    Uninstall all the files associated to the notify app except, eventually, the credentials that have been stored in {utilities.std_config_path}

    
NOTIFY COMMANDS:

> notify {utilities.PROFILE} <profile_params> <send_options>
    Send a message.
    <profile_params>:
        <name> : the name of the profile to load (if used, it's the first parameter. Es: notify {utilities.PROFILE} <name> <other_params>)
        {utilities.TOKEN} <token> : the token to use.
        If both name and token are specified first is loaded the <name> profile, then the <token> will overwrite the one specified by the profile.
    If the {utilities.PROFILE} <profile_params> is omitted, the default profile found inside the configuration file will be used
    <send_options>:
        {utilities.TEXT} <text/path_to_file> <other_params> : Sends a text message by specifying the text or passing a text file.
        {utilities.PHOTO} <path_to_file> <other_params> : Sends a photo through file.
        {utilities.AUDIO} <path_to_file> <other_params> : Sends an audio throuhg file.
        {utilities.DOCUMENT} <path_to_file> <other_params> : sends a document through file.
        {utilities.VIDEO} <path_to_file> <other_params> : sends a video through file.
        {utilities.EXCEPTION} <text> <other_params> : sends a text message formatted as an exception.
        
        To see which parameters are allowed as <other_params> use >notify {utilities.HELP} <command>
        <other_params> can be omitted if you wish to use the default/selected profile ones

    Es: notify {utilities.PROFILE} test_name {utilities.PHOTO} path/to/photo.jpg {utilities.CAPTION} caption
        Sends a photo with caption using the profile test_name

"""
    else:
        
        type = sys.argv[2]

        if type == utilities.PARAMETERS:
            message = f"""the list of all parameters you can use with their description.
Each parameter is not guaranteed to work for each notify command.
Use notify {utilities.HELP} <notify_command> to get the list of parameters accepted for each command.

"""
            for exp in utilities.explanation:
                message = message + utilities.explanation[exp] + "\n"
        elif type == utilities.PROFILE:
            message = f"""the explanation of the {utilities.PROFILE} command.
> notify {utilities.PROFILE} <proile_params> ...
    <profile_params>:
        <name> : the name of the profile to load (if used, it's the first parameter. Es: notify {utilities.PROFILE} <name> <other_params>)
        {utilities.TOKEN} <token> : the token to use. If both token and name of the profile are specified, the token specified will have priority over the one stored in the profile.
    If the {utilities.PROFILE} <profile_params> is omitted, the 'default' profile found inside the configuration file will be used.
"""
        elif type == utilities.TEXT:
            message = f"""the explanation of the {utilities.TEXT} command.
> notify <optional_profile_setup> {utilities.TEXT} <text/file> <text_params>
    <text/file> : The text to write in the message or the path to a text file containing the text to send (is used, it's the first parameter. Es: notify -t text of the message <other_params>)
    <text_params>:
        {utilities.explanation[utilities.CHAT_ID]}
        {utilities.explanation[utilities.MESSAGE_THREAD_ID]}
        {utilities.explanation[utilities.PARSE_MODE]}
        {utilities.explanation[utilities.DISABLE_WEB_PAGE_PREVIEW]}
        {utilities.explanation[utilities.DISABLE_NOTIFICATION]}
        {utilities.explanation[utilities.PROTECT_CONTENT]}
        {utilities.explanation[utilities.REPLY_TO_MESSAGE_ID]}
        {utilities.explanation[utilities.ALLOW_SENDING_WITHOUT_REPLY]}
"""
        elif type == utilities.PHOTO:
            message = f"""the explanation of the {utilities.PHOTO} command.
> notify <optional_profile_setup> {utilities.PHOTO} <file_path> <photo_params>
    <file_path> : Path to the file to send.
    <photo_params>:
        {utilities.explanation[utilities.CHAT_ID]}
        {utilities.explanation[utilities.MESSAGE_THREAD_ID]}
        {utilities.explanation[utilities.CAPTION]}
        {utilities.explanation[utilities.PARSE_MODE]}
        {utilities.explanation[utilities.HAS_SPOILER]}
        {utilities.explanation[utilities.DISABLE_NOTIFICATION]}
        {utilities.explanation[utilities.PROTECT_CONTENT]}
        {utilities.explanation[utilities.REPLY_TO_MESSAGE_ID]}
        {utilities.explanation[utilities.ALLOW_SENDING_WITHOUT_REPLY]}
"""
        elif type == utilities.AUDIO:
            message = f"""the explanation of the {utilities.AUDIO} command.
> notify <optional_profile_setup> {utilities.AUDIO} <file_path> <audio_params>
    <file_path> : Path to the file to send.
    <audio_params>:
        {utilities.explanation[utilities.CHAT_ID]}
        {utilities.explanation[utilities.MESSAGE_THREAD_ID]}
        {utilities.explanation[utilities.CAPTION]}
        {utilities.explanation[utilities.PARSE_MODE]}
        {utilities.explanation[utilities.DURATION]}
        {utilities.explanation[utilities.PERFORMER]}
        {utilities.explanation[utilities.TITLE]}
        {utilities.explanation[utilities.THUMBNAIL]}
        {utilities.explanation[utilities.DISABLE_NOTIFICATION]}
        {utilities.explanation[utilities.PROTECT_CONTENT]}
        {utilities.explanation[utilities.REPLY_TO_MESSAGE_ID]}
        {utilities.explanation[utilities.ALLOW_SENDING_WITHOUT_REPLY]}
    """
        elif type == utilities.DOCUMENT:
            message = f"""the explanation of the {utilities.DOCUMENT} command.
> notify <optional_profile_setup> {utilities.DOCUMENT} <file_path> <document_params>
    <file_path> : Path to the file to send.
    <document_params>:
        {utilities.explanation[utilities.CHAT_ID]}
        {utilities.explanation[utilities.MESSAGE_THREAD_ID]}
        {utilities.explanation[utilities.THUMBNAIL]}
        {utilities.explanation[utilities.CAPTION]}
        {utilities.explanation[utilities.PARSE_MODE]}
        {utilities.explanation[utilities.DISABLE_CONTENT_TYPE_DETECTION]}
        {utilities.explanation[utilities.DISABLE_NOTIFICATION]}
        {utilities.explanation[utilities.PROTECT_CONTENT]}
        {utilities.explanation[utilities.REPLY_TO_MESSAGE_ID]}
        {utilities.explanation[utilities.ALLOW_SENDING_WITHOUT_REPLY]}
"""
        elif type == utilities.VIDEO:
            message = f"""the explanation of the {utilities.VIDEO} command.
> notify <optional_profile_setup> {utilities.VIDEO} <file_path> <video_params>
    <file_path> : Path to the file to send.
    <video_params>:
        {utilities.explanation[utilities.CHAT_ID]}
        {utilities.explanation[utilities.MESSAGE_THREAD_ID]}
        {utilities.explanation[utilities.DURATION]}
        {utilities.explanation[utilities.WIDTH]}
        {utilities.explanation[utilities.HEIGHT]}
        {utilities.explanation[utilities.THUMBNAIL]}
        {utilities.explanation[utilities.CAPTION]}
        {utilities.explanation[utilities.PARSE_MODE]}
        {utilities.explanation[utilities.HAS_SPOILER]}
        {utilities.explanation[utilities.SUPPORTS_STREAMING]}
        {utilities.explanation[utilities.DISABLE_NOTIFICATION]}
        {utilities.explanation[utilities.PROTECT_CONTENT]}
        {utilities.explanation[utilities.REPLY_TO_MESSAGE_ID]}
        {utilities.explanation[utilities.ALLOW_SENDING_WITHOUT_REPLY]}
"""
        elif type == utilities.EXCEPTION:
            message = f"""the explanation of the {utilities.EXCEPTION} command.
> notify <optional_profile_setup> {utilities.EXCEPTION} <text> <exception_params>
    <text> : The text of the exception to send.
    <exception_params>:
        {utilities.explanation[utilities.CHAT_ID]}
"""
        else:
            print(utilities.help_error)
            exit(1)
    
    print(utilities.help_beginning + message + utilities.help_conclusion)

def ntf_update():

    if len(sys.argv) == 3 and sys.argv[2] != utilities.PROD and sys.argv[2] != utilities.DEV:
        print(utilities.error)
        exit(1)

    additional_text = ""
    if len(sys.argv) == 3 and sys.argv[2] == utilities.DEV:
        additional_text = " d"

    subprocess.run(shlex.split(f"python3 {utilities.base_path}/updater.py{additional_text}"))

def ntf_uninstall(): 
        
    choice = input("Proceeding to uninstall notify? [y/n]: ")
    while choice not in ("y", "n"):
        choice = input(f"{utilities.command_error}Proceeding to uninstall notify? [y/n]: ")

    if choice == "n":
        print("Uninstall aborted.")
        exit(0)
    
    print("Uninstalling...")
    subprocess.run(shlex.split(f"rm -r {utilities.home}/.notify_zanz"))
    
    if os.path.exists(f"{utilities.home}/.bashrc"):
        bashrc = ""
        with open(f"{utilities.home}/.bashrc", "r") as f:
            bashrc = f.read()
        bashrc = bashrc.replace(utilities.bashrc_edit_title, "")
        bashrc = bashrc.replace(utilities.bashrc_edit_content, "")
        with open(f"{utilities.home}/.bashrc", "w") as f:
            f.write(bashrc)
    if os.path.exists(f"{utilities.home}/.zshrc"):
        zshrc = ""
        with open(f"{utilities.home}/.zshrc", "r") as f:
            zshrc = f.read()
        zshrc = zshrc.replace(utilities.bashrc_edit_title, "")
        zshrc = zshrc.replace(utilities.bashrc_edit_content, "")
        with open(f"{utilities.home}/.zshrc", "w") as f:
            f.write(zshrc)
            
    print("notify has been succesfully uninstalled.")

if not os.path.exists(utilities.std_config_path):
    choice = "n"
    if os.path.exists(utilities.old_config_path):

        choice = input(f"Found a configuration file ({utilities.old_config_path}) from a past version.\nUse that configuration to create a default profile? [y/n/q to quit]: ")
        while choice not in ("y", "n", "q"):
            choice = input("Command not recognised.\nUse that configuration to create a default profile? [y/n/q to quit]: ")

        if choice == "q":
            print("notify not installed.\nExiting setup.")
            exit(0)

        if choice == "y":
            with open(utilities.old_config_path, "r") as f:
                conf = json.loads(f.read())
                notify.write_conf_profile(name="default", token=conf["token"], to_chat_id=conf["chatid"])

    if choice == "n":

        choice = input("Do you wish to create a profile to store in the configuration file? [y/n/q to quit]: ")
        while choice not in ("y", "n", "q"):
            choice = input("Command not recognised.\nCreating a profile to store in the configuration file? [y/n/q to quit]: ")

        if choice == "q":
            print("notify not installed.\nExiting setup.")

        elif choice == "n":
            print("No profile loaded, remember to specify the token each time or create a new profile.")

        else:
            print("Creating a new profile.")
            name = input("Insert the name of the profile to create: ")
            token=input("Insert the token of the profile to create: ")
            notify.write_conf_profile(name=name, token=token)
            with open(utilities.std_config_path, "r") as f:
                profiles = json.loads(f.read())
            profiles["def"] = name
            with open(utilities.std_config_path, "w") as f:
                f.write(json.dumps(profiles, indent=4))

            print("Profile created.\nYou can edit configuration parameters later on using notify (use the help function).")

    choice = input(f"Removing old credentials file ({utilities.old_config_path})? [y/n]: ")
    while choice not in ("y", "n"):
        choice = input(f"Command not recognised.\nRemoving old credentials file ({utilities.old_config_path})? [y/n]: ")

    if choice == "y":
        subprocess.run(shlex.split(f"rm {utilities.old_config_path}"))

with open(utilities.std_config_path, "r") as f:
    bot = notify.bot(profile=json.loads(f.read())["def"])

if __name__ == "__main__":
    main()
