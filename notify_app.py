import subprocess, utilities, notify, shlex, json, sys, os

def main():

    global command

    try:
        
        if len(sys.argv)==1:
            utilities.print_notify_error(utilities.error)

        elif sys.argv[1] == utilities.HELP:
            if len(sys.argv) not in (2, 3):
                utilities.print_notify_error(utilities.error)

            utilities.print_info(f"Running {utilities.HELP} command.")
            help()
            exit(0)

        elif sys.argv[1] == utilities.UPDATE:
            if len(sys.argv) not in (2, 3):
                utilities.print_notify_error(utilities.error)

            utilities.print_info(F"Running {utilities.UPDATE} command.")
            ntf_update()
            exit(0)

        elif sys.argv[1] == utilities.UNINSTALL:
            if len(sys.argv) > 2:
                utilities.print_notify_error(utilities.error)

            utilities.print_info(f"Running {utilities.UNINSTALL} command.")
            ntf_uninstall()
            exit(0)

        elif sys.argv[1] == utilities.VERSION:
            if len(sys.argv) > 2:
                utilities.print_notify_error(utilities.error)

            print(utilities.version)
            exit(0)

        elif sys.argv[1] == utilities.CONF:
            
            utilities.print_info(f"Running {utilities.CONF} command.")
            command = " ".join(sys.argv[1:])
            ntf_config()

            if len(command.strip()) > 0:
                utilities.print_warning(f"Ignored parts of the input: {command}")
                utilities.print_info(utilities.suggestion)

            exit(0)

        command = " ".join(sys.argv[1:])

        if sys.argv[1] == utilities.PROFILE:

            utilities.print_info(f"Running {utilities.PROFILE} command.")
            ntf_profile()
        
        utilities.print_info(f"Sending message.")
        ntf_send()
        
        if len(command.strip()) > 0:
            utilities.print_info(f"Message sent.")
            utilities.print_warning(f"Ignored parts of the input: {command}")
            utilities.print_info(utilities.suggestion)

    except:
        pass

def ntf_config():

    global command
    
    command = command[6:]

    if command == "":
        utilities.print_info(utilities.conf_file_info)
        exit(0)

    type = command.partition(" ")[0]

    if type == utilities.ADD:

        name = get(utilities.ADD)
        token = get(utilities.TOKEN)

        if name == "" or token == "":
            utilities.print_notify_error(utilities.add_conf_error)

        notify.write_conf_profile(name=name, token=token, from_chat_id=get(utilities.FROM_CHAT_ID), to_chat_id=get(utilities.CHAT_ID), disable_web_page_preview=get(utilities.DISABLE_WEB_PAGE_PREVIEW), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), parse_mode=get(utilities.PARSE_MODE))

    elif type == utilities.EDIT:

        name = get(utilities.EDIT)

        if name == "":
            utilities.print_notify_error(utilities.profile_name_error)

        notify.edit_conf_profile(name=name, token=get(utilities.TOKEN), from_chat_id=get(utilities.FROM_CHAT_ID), to_chat_id=get(utilities.CHAT_ID), disable_web_page_preview=get(utilities.DISABLE_WEB_PAGE_PREVIEW), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), parse_mode=get(utilities.PARSE_MODE))
    
    elif type == utilities.REMOVE:

        name = get(utilities.REMOVE)

        choice = utilities.print_input(f"{utilities.cmd_input}Removing profile {name}?{utilities.cmd_end} [y/n]: ")
        while choice not in ("y", "n"):
            utilities.print_warning("Command not recognised.")
            choice = utilities.print_input(f"{utilities.cmd_input}Removing profile {name}?{utilities.cmd_end} [y/n]: ")

        if choice == "y":
            notify.remove_profile(name)
            utilities.print_info("Profile removed.")
        else:
            utilities.print_info("Profile not removed.")

    elif type == utilities.SET:

        name = get(utilities.SET)

        if name == "":
            utilities.print_notify_error(utilities.set_conf_error)

        notify.set_default_profile(name)

    elif type == utilities.SEE:

        get(utilities.SEE)

        with open(utilities.std_config_path, "r") as f:
            print(f.read())

    else:

        utilities.print_notify_error(utilities.command_error)

    if type != utilities.SEE: utilities.print_info(f"Edited configuration file.")

def ntf_profile():

    global command

    token = get(utilities.TOKEN)
    profile = get(utilities.PROFILE)

    if profile == "" and token == "":
        utilities.print_notify_error(utilities.profile_error)

    with open(utilities.std_config_path) as f:
        if profile not in json.loads(f.read())["profiles"]:
            utilities.print_notify_error(utilities.profile_name_error)
    
    bot.load_profile(token=token, name=profile)

def ntf_send():

    type = command.partition(" ")[0]

    if type == utilities.TEXT:

        content = get(utilities.TEXT)

        if content == "":
            utilities.print_notify_error(utilities.message_error)

        if ispath(content):
            response = bot.send_message_by_file(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), parse_mode=get(utilities.PARSE_MODE), disable_web_page_preview=get(utilities.DISABLE_WEB_PAGE_PREVIEW), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY))
        else:
            response = bot.send_message_by_text(text=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), parse_mode=get(utilities.PARSE_MODE), disable_web_page_preview=get(utilities.DISABLE_WEB_PAGE_PREVIEW), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY))

    elif type == utilities.PHOTO:

        content = get(utilities.PHOTO)

        if content == "":
            utilities.print_notify_error(utilities.photo_error)

        response = bot.send_photo_by_path(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), has_spoiler=get(utilities.HAS_SPOILER), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY))
        
    elif type == utilities.AUDIO:

        content = get(utilities.AUDIO)

        if content == "":
            utilities.print_notify_error(utilities.audio_error)

        response = bot.send_audio_by_path(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), duration=get(utilities.DURATION), performer=get(utilities.PERFORMER), title=get(utilities.TITLE), thumbnail=get(utilities.THUMBNAIL), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY))

    elif type == utilities.DOCUMENT:

        content = get(utilities.DOCUMENT)

        if content == "":
            utilities.print_notify_error(utilities.doc_error)

        response = bot.send_document_by_path(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), thumbnail=get(utilities.THUMBNAIL), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), disable_content_type_detection=get(utilities.DISABLE_CONTENT_TYPE_DETECTION), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY))

    elif type == utilities.VIDEO:

        content = get(utilities.VIDEO)

        if content == "":
            utilities.print_notify_error(utilities.video_error)

        response = bot.send_video_by_path(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), duration=get(utilities.DURATION), width=get(utilities.WIDTH), height=get(utilities.HEIGHT), thumbnail=get(utilities.THUMBNAIL), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), has_spoiler=get(utilities.HAS_SPOILER), supports_streaming=get(utilities.SUPPORTS_STREAMING), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY))

    elif type in utilities.EXCEPTION:

        response = bot.send_exception(text=get(utilities.EXCEPTION), chat_id=get(utilities.CHAT_ID))

    else:
        utilities.print_notify_error(utilities.command_error)

    if not response["ok"]:
        utilities.print_notify_error(f"Something went wrong:\n{response}")

    utilities.print_info("Message sent succesfully.")

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
            utilities.print_notify_error(utilities.error)
            
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
    If the update feature stops working, please refer to the change_log on github since the new version might require some additional steps to update due to some incompatibility with older versions.
    You can add at the end which type of update u prefer:
        > {utilities.PROD} (default) : uploads to the latest tested version
        > {utilities.DEV} : uploads to the latest version under development (not finished, not suggested)

    Es: notify {utilities.UPDATE} {utilities.DEV}
        Requests an update to the latest version under development

> notify {utilities.CONF}
    Print the configuration file location.
    You can add at the end one of those additional commands:
        > {utilities.ADD} <name> {utilities.TOKEN} <token> <other_params> : add a profile to the configuration file
            <other_params>:
                {utilities.explanation[utilities.FROM_CHAT_ID]}
                {utilities.explanation[utilities.CHAT_ID]}
                {utilities.explanation[utilities.DISABLE_WEB_PAGE_PREVIEW]}
                {utilities.explanation[utilities.DISABLE_NOTIFICATION]}
                {utilities.explanation[utilities.PROTECT_CONTENT]}
                {utilities.explanation[utilities.ALLOW_SENDING_WITHOUT_REPLY]}
                {utilities.explanation[utilities.PARSE_MODE]}
            <other_params> can be omitted if you wish to use the default/selected profile ones
        > {utilities.EDIT} <name> <other_params> : edit a profile from the configuration file (creates a new one if the specified one doesn't exist)
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
            utilities.print_notify_error(utilities.help_error)
    
    print(utilities.help_beginning + message + utilities.help_conclusion)

def ntf_update():

    if len(sys.argv) == 3 and sys.argv[2] != utilities.PROD and sys.argv[2] != utilities.DEV:
        utilities.print_notify_error(utilities.error)

    additional_text = ""
    if len(sys.argv) == 3 and sys.argv[2] == utilities.DEV:
        additional_text = " d"

    subprocess.run(shlex.split(f"python3 {utilities.base_path}/updater.py{additional_text}"))

def ntf_uninstall(): 
        
    choice = utilities.print_input(f"{utilities.cmd_input}Proceeding to uninstall notify?{utilities.cmd_end} [y/n]: ")
    while choice not in ("y", "n"):
        utilities.print_warning(f"{utilities.command_error}")
        choice = utilities.print_input(f"Proceeding to uninstall notify? [y/n]: ")

    if choice == "n":
        utilities.print_warning("Uninstall aborted.")
        exit(0)
    
    utilities.print_info("Uninstalling...")
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
            
    utilities.print_info("notify has been succesfully uninstalled.")

if not os.path.exists(utilities.std_config_path):
    choice = "n"
    if os.path.exists(utilities.old_config_path):

        utilities.print_warning(f"Found a configuration file ({utilities.old_config_path}) from a past version.")
        choice = utilities.print_input(f"{utilities.cmd_input}Use that configuration to create a default profile in the standard configuration file ({utilities.std_config_path})?{utilities.cmd_end} [y/n/q to quit]: ")
        while choice not in ("y", "n", "q"):
            utilities.print_warning("Command not recognised.")
            choice = utilities.print_input(f"{utilities.cmd_input}Use that configuration to create a default profile?{utilities.cmd_end} [y/n/q to quit]: ")

        if choice == "q":
            utilities.print_warning("Profiles not set up.")
            utilities.print_info("Exiting.")
            exit(0)

        if choice == "y":
            with open(utilities.old_config_path, "r") as f:
                conf = json.loads(f.read())
                notify.write_conf_profile(name="default", token=conf["token"], to_chat_id=conf["chatid"])

    if choice == "n":

        choice = utilities.print_input(f"{utilities.cmd_input}Do you wish to create a profile to store in the configuration file?{utilities.cmd_end} [y/n/q to quit]: ")
        while choice not in ("y", "n", "q"):
            utilities.print_warning("Command not recognised.")
            choice = utilities.print_input(f"{utilities.cmd_input}Creating a profile to store in the configuration file?{utilities.cmd_end} [y/n/q to quit]: ")

        if choice == "q":
            utilities.print_warning("Profiles not set up.")
            utilities.print_info("Exiting.")
            exit(0)

        elif choice == "n":
            utilities.print_warning("No profile loaded, remember to specify the token each time or create a new profile.")

        else:
            utilities.print_info("Creating a new profile.")
            name = utilities.print_input("Insert the name of the profile to create: ")
            token=utilities.print_input("Insert the token of the profile to create: ")
            notify.write_conf_profile(name=name, token=token)
            with open(utilities.std_config_path, "r") as f:
                profiles = json.loads(f.read())
            profiles["def"] = name
            with open(utilities.std_config_path, "w") as f:
                f.write(json.dumps(profiles, indent=4))

            utilities.print_info("Profile created.\nYou can edit configuration parameters later on using notify (use the help function).")

    choice = utilities.print_input(f"Removing old credentials file ({utilities.old_config_path})? [y/n]: ")
    while choice not in ("y", "n"):
        utilities.print_warning("Command not recognised.")
        choice = utilities.print_input(f"Removing old credentials file ({utilities.old_config_path})? [y/n]: ")

    if choice == "y":
        subprocess.run(shlex.split(f"rm {utilities.old_config_path}"))

with open(utilities.std_config_path, "r") as f:
    bot = notify.bot(profile=json.loads(f.read())["def"])

if __name__ == "__main__":
    main()
