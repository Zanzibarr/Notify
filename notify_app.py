import subprocess, notify, requests, utilities, shlex, json, sys, os
import numpy as np

# TODO : How to pass entities
# TODO : How to pass reply_markup
# TODO : How to pass caption entities
# TODO : How to pass explanation entities

# TODO : edit functions

# TODO : Help function for edit options

def main():

    global command

    try:
        
        if len(sys.argv)==1:
            print(utilities.error)
            exit(1)

        elif sys.argv[1] in utilities.HELP:
            if len(sys.argv) not in (2, 3):
                print(utilities.error)
                exit(1)

            help()
            exit(0)

        elif sys.argv[1] in utilities.UPDATE:
            if len(sys.argv) not in (2, 3):
                print(utilities.error)
                exit(1)

            ntf_update()
            exit(0)

        elif sys.argv[1] in utilities.UNINSTALL:
            if len(sys.argv) > 2:
                print(utilities.error)
                exit(1)

            ntf_uninstall()
            exit(0)

        elif sys.argv[1] in utilities.VERSION:
            if len(sys.argv) > 2:
                print(utilities.error)
                exit(1)

            print(utilities.version)
            exit(0)

        elif sys.argv[1] in utilities.CONF:
            
            command = " ".join(sys.argv[1:])
            ntf_config()

            if len(command.strip()) > 0:
                print(f"\nIgnored parts of the input: {command}\n{utilities.suggestion}\n")

            exit(0)

        command = " ".join(sys.argv[1:])

        if sys.argv[1] in utilities.PROFILE:

            ntf_profile()

        index = [command.find(e) for e in utilities.EDIT]
        if all(i < 0 for i in index):
            ntf_send()
        else:
            print("UNIMPLEMENTED")#ntf_edit() #TODO

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

    if type in utilities.ADD:

        name = get(utilities.ADD)
        token = get(utilities.TOKEN)

        if name == "" or token == "":
            print(utilities.add_conf_error)
            exit(1)

        notify.write_conf_profile(name=name, token=token, from_chat_id=get(utilities.FROM_CHAT_ID), to_chat_id=get(utilities.CHAT_ID), disable_web_page_preview=get(utilities.DISABLE_WEB_PAGE_PREVIEW), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), parse_mode=get(utilities.PARSE_MODE))
        
    elif type in utilities.REMOVE:

        name = get(utilities.REMOVE)

        notify.remove_profile(name)

    elif type in utilities.SET:

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

    elif type in utilities.SEE:

        get(utilities.SEE)

        print(json.dumps(notify.get_profiles()), indent=4)

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

    if type in utilities.TEXT:

        content = get(utilities.TEXT)

        if content == "":
            print(utilities.message_error)
            exit(1)

        if ispath(content):
            response = bot.send_message_by_file(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), parse_mode=get(utilities.PARSE_MODE), entities=get(utilities.ENTITIES), disable_web_page_preview=get(utilities.DISABLE_WEB_PAGE_PREVIEW), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))
        else:
            response = bot.send_message_by_text(text=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), parse_mode=get(utilities.PARSE_MODE), entities=get(utilities.ENTITIES), disable_web_page_preview=get(utilities.DISABLE_WEB_PAGE_PREVIEW), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))

    elif type in utilities.COPY:

        message_id = get(utilities.MESSAGE_ID)
        chat_id = get(utilities.CHAT_ID)
        if message_id == "" and chat_id == "":
            print(utilities.copy_error)
            exit(1)

        response = bot.copy_message(message_id=message_id, chat_id=chat_id, from_chat_id=get(utilities.FROM_CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), caption_entities=get(utilities.CAPTION_ENTITIES), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))

    elif type in utilities.FORWARD:

        message_id = get(utilities.MESSAGE_ID)
        chat_id = get(utilities.CHAT_ID)
        if message_id == "" and chat_id == "":
            print(utilities.forward_error)
            exit(1)

        response = bot.forward_message(message_id=message_id, chat_id=chat_id, from_chat_id=get(utilities.FROM_CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT))

    elif type in utilities.PHOTO:

        content = get(utilities.PHOTO)

        if content == "":
            print(utilities.photo_error)
            exit(1)

        if ispath(content):
            response = bot.send_photo_by_path(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), caption_entities=get(utilities.CAPTION_ENTITIES), has_spoiler=get(utilities.HAS_SPOILER), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))
        else:
            response = bot.send_photo(photo=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), caption_entities=get(utilities.CAPTION_ENTITIES), has_spoiler=get(utilities.HAS_SPOILER), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))
            
    elif type in utilities.AUDIO:

        content = get(utilities.AUDIO)

        if content == "":
            print(utilities.audio_error)
            exit(1)

        if ispath(content):
            response = bot.send_audio_by_path(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), caption_entities=get(utilities.CAPTION_ENTITIES), duration=get(utilities.DURATION), performer=get(utilities.PERFORMER), title=get(utilities.TITLE), thumbnail=get(utilities.THUMBNAIL), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))
        else:
            response = bot.send_audio(audio=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), caption_entities=get(utilities.CAPTION_ENTITIES), duration=get(utilities.DURATION), performer=get(utilities.PERFORMER), title=get(utilities.TITLE), thumbnail=get(utilities.THUMBNAIL), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))

    elif type in utilities.DOCUMENT:

        content = get(utilities.DOCUMENT)

        if content == "":
            print(utilities.doc_error)
            exit(1)

        if ispath(content):
            response = bot.send_document_by_path(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), thumbnail=get(utilities.THUMBNAIL), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), caption_entities=get(utilities.CAPTION_ENTITIES), disable_content_type_detection=get(utilities.DISABLE_CONTENT_TYPE_DETECTION), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))
        else:
            response = bot.send_document(document=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), thumbnail=get(utilities.THUMBNAIL), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), caption_entities=get(utilities.CAPTION_ENTITIES), disable_content_type_detection=get(utilities.DISABLE_CONTENT_TYPE_DETECTION), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))

    elif type in utilities.VIDEO:

        content = get(utilities.VIDEO)

        if content == "":
            print(utilities.video_error)
            exit(1)

        if ispath(content):
            response = bot.send_video_by_path(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), duration=get(utilities.DURATION), width=get(utilities.WIDTH), height=get(utilities.HEIGHT), thumbnail=get(utilities.THUMBNAIL), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), caption_entities=get(utilities.CAPTION_ENTITIES), has_spoiler=get(utilities.HAS_SPOILER), supports_streaming=get(utilities.SUPPORTS_STREAMING), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))
        else:
            response = bot.send_video(video=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), duration=get(utilities.DURATION), width=get(utilities.WIDTH), height=get(utilities.HEIGHT), thumbnail=get(utilities.THUMBNAIL), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), caption_entities=get(utilities.CAPTION_ENTITIES), has_spoiler=get(utilities.HAS_SPOILER), supports_streaming=get(utilities.SUPPORTS_STREAMING), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))
        
    elif type in utilities.VOICE:

        content = get(utilities.VOICE)

        if content == "":
            print(utilities.voice_error)
            exit(1)

        if ispath(content):
            response = bot.send_voice_by_path(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), caption_entities=get(utilities.CAPTION_ENTITIES), duration=get(utilities.DURATION), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))
        else:
            response = bot.send_voice(voice=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), caption_entities=get(utilities.CAPTION_ENTITIES), duration=get(utilities.DURATION), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))

    elif type in utilities.ANIMATION:

        content = get(utilities.ANIMATION)

        if content == "":
            print(utilities.animation_error)
            exit(1)

        if ispath(content):
            response = bot.send_animation_by_path(file_path=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), duration=get(utilities.DURATION), width=get(utilities.WIDTH), height=get(utilities.HEIGHT), thumbnail=get(utilities.THUMBNAIL), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), caption_entities=get(utilities.CAPTION_ENTITIES), has_spoiler=get(utilities.HAS_SPOILER), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))
        else:
            response = bot.send_animation(animation=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), duration=get(utilities.DURATION), width=get(utilities.WIDTH), height=get(utilities.HEIGHT), thumbnail=get(utilities.THUMBNAIL), caption=get(utilities.CAPTION), parse_mode=get(utilities.PARSE_MODE), caption_entities=get(utilities.CAPTION_ENTITIES), has_spoiler=get(utilities.HAS_SPOILER), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))

    elif type in utilities.VIDEONOTE:

        content = get(utilities.VIDEONOTE)

        if content == "":
            print(utilities.videonote_error)
            exit(1)

        if ispath(content):
            response = bot.send_videonote_by_path(file_path=content, cchat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), duration=get(utilities.DURATION), length=get(utilities.LENGTH), thumbnail=get(utilities.THUMBNAIL), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))
        else:
            response = bot.send_videonote(videonote=content, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), duration=get(utilities.DURATION), length=get(utilities.LENGTH), thumbnail=get(utilities.THUMBNAIL), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))

    elif type in utilities.LOCATION:

        lat = get(utilities.LATITUDE)
        lon = get(utilities.LONGITUDE)

        if lat == "" or lon == "":
            print(utilities.location_error)
            exit(1)

        response = bot.send_location(latitude=lat, longitude=lon, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), horizontal_accuracy=get(utilities.HORIZONTAL_ACCURACY), live_period=get(utilities.LIVE_PERIOD), heading=get(utilities.HEADING), proximity_alert_radius=get(utilities.PROXIMITY_ALERT_RADIUS), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))

    elif type in utilities.VENUE:

        lat = get(utilities.LATITUDE)
        lon = get(utilities.LONGITUDE)
        title = get(utilities.TITLE)
        address = get(utilities.ADDRESS)

        if lat == "" or lon == "" or title == "" or address == "":
            print(utilities.venue_error)
            exit(1)

        response = bot.send_venue(latitude=lat, longitude=lon, title=title, address=address, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), foursquare_id=get(utilities.FOURSQUARE_ID), foursquare_type=get(utilities.FOURSQUARE_TYPE), google_place_id=get(utilities.GOOGLE_PLACE_ID), google_place_type=get(utilities.GOOGLE_PLACE_TYPE), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))

    elif type in utilities.CONTACT:

        number = get(utilities.PHONE_NUMBER)
        name = get(utilities.FIRST_NAME)

        if number == "" or name == "":
            print(utilities.contact_error)
            exit(1)

        response = bot.send_contact(phone_number=number, first_name=name, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), last_name=get(utilities.LAST_NAME), vcard=get(utilities.VCARD), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))

    elif type in utilities.POLL:

        question = get(utilities.QUESTION)
        options = get(utilities.OPTIONS)

        if question == "" or options == "":
            print(utilities.poll_error)
            exit(1)

        response = bot.send_poll(question=question, options=options, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), is_anonymous=get(utilities.IS_ANONYMOUS), type=get(utilities.TYPE), allows_multiple_answers=get(utilities.ALLOWS_MULTIPLE_ANSWERS), correct_option_id=get(utilities.CORRECT_OPTION_ID), explanation=get(utilities.EXPLANATION), explanation_parse_mode=get(utilities.EXPLANATION_PARSE_MODE), explanation_entities=get(utilities.EXPLANATION_ENTITIES), open_period=get(utilities.OPEN_PERIOD), close_date=get(utilities.CLOSE_DATE), is_closed=get(utilities.IS_CLOSED), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOWS_MULTIPLE_ANSWERS), reply_markup=get(utilities.REPLY_MARKUP))

    elif type in utilities.DICE:

        response = bot.send_dice(chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID), emoji=get(utilities.EMOJI), disable_notification=get(utilities.DISABLE_NOTIFICATION), protect_content=get(utilities.PROTECT_CONTENT), reply_to_message_id=get(utilities.REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(utilities.ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(utilities.REPLY_MARKUP))

    elif type in utilities.ACTION:

        action = get(utilities.ACTION)

        if action == "":
            print(utilities.action_error)
            exit(1)

        response = bot.send_chataction(action=action, chat_id=get(utilities.CHAT_ID), message_thread_id=get(utilities.MESSAGE_THREAD_ID))

    elif type in utilities.EXCEPTION:

        response = bot.send_exception(text=get(utilities.EXCEPTION), chat_id=get(utilities.CHAT_ID))

    else:
        print(utilities.command_error)
        exit(1)    

    if not response["ok"]:
        print(f"Something went wrong:\n{response}")

def ispath(content):
    return os.path.exists(content)

def get(lst_type):

    global command

    for type in lst_type:
        index = command.find(f"-{type}")
        if index >= 0:
            break
    if index < 0:
        for type in lst_type:
            index = command.find(type)
            if index >= 0:
                break
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

        if lst_type[0] not in utilities.SHORTCUT_COMMANDS:
            print(utilities.error)
            exit(1)
            
        c_len = command[index+2:].find("-")
        if c_len < 0:
            cut = len(command)
        else:
            cut = index + 2 + c_len
        command = command[:index]+command[cut:]
        
        return True

def help(): #TODO

    if len(sys.argv) == 2:
        message = f"""the list of commands allowed with their explaination.
          
CONFIGURATION COMMANDS:

> notify {utilities.tostr(utilities.HELP)}
    Prints the instructions
    You can add at the end the type of notify command you need help with
    To see the description of ALL parameters that can be used, use {utilities.tostr(utilities.PARAMETERS)}

    Es: notify {utilities.HELP[0]} {utilities.TEXT[0]}
    Es: notify {utilities.HELP[1]} {utilities.EDIT[0]}
    Es: notify {utilities.HELP[1]} {utilities.VOICE[0]}

> notify {utilities.tostr(utilities.VERSION)}
    See the current notify version

> notify {utilities.tostr(utilities.UPDATE_1)}
    Download the latest version of notify
    You can add at the end which type of update u prefer:
        > {utilities.tostr(utilities.PROD)} (default) : uploads to the latest tested version
        > {utilities.tostr(utilities.DEV)} : uploads to the latest version under development (not finished, not suggested)

    Es: notify {UPDATE_2} {DEV}
        Requests an update to the latest version under development

> notify {CONF_1} / > notify {CONF_2}
    Print the configuration file location.
    You can add at the end one of those additional commands:
        > {ADD} <name> {TOKEN} <token> <other_params> : to add a profile to the configuration file
            <other_params>:
                {explanation[FROM_CHAT_ID]}
                {explanation[CHAT_ID]}
                {explanation[DISABLE_WEB_PAGE_PREVIEW]}
                {explanation[DISABLE_NOTIFICATION]}
                {explanation[PROTECT_CONTENT]}
                {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
                {explanation[PARSE_MODE]}
            <other_params> can be omitted if you wish to use the default/selected profile ones
        > {REMOVE} <name> : removes a profile from the configuration file
        > {SET} <name> : sets the default profile for command line use
        > {SEE} : prints the content of the configuration file

    Es: notify {CONF_2} {SEE}
        Shows all configurations currently saved
    Es: notify {CONF_1} {ADD} test_name {TOKEN} valid_bot_token {PARSE_MODE} MarkdownV2 {DISABLE_NOTIFICATION} true
        Creates/Edits the profile named test_name setting the parameters token, parse_mode and disable_notification

> notify {UNINSTALL}
    Uninstall all the files associated to the notify app except, eventually, the credentials that have been stored in {std_config_path}

    
NOTIFY COMMANDS:

> notify {PROFILE} <profile_params> <send_options>
    Send a message.
    <profile_params>:
        <name> : the name of the profile to load (if used, it's the first parameter. Es: notify {PROFILE} <name> <other_params>)
        {TOKEN} <token> : the token to use.
        If both name and token are specified first is loaded the <name> profile, then the <token> will overwrite the one specified by the profile.
    If the {PROFILE} <profile_params> is omitted, the 'default' profile found inside the configuration file will be used
    <send_options>:
        {TEXT} <text/path_to_file> <other_params> : Sends a text message by specifying the text or passing a text file.
        {COPY} {MESSAGE_ID} <message_id> {CHAT_ID} <chat_id> <other_params> : Copies a message and sends it.
        {FORWARD} {MESSAGE_ID} <message_id> {CHAT_ID} <chat_id> <other_params> : Forwards a message.
        {PHOTO} <photo_id/path_to_file> <other_params> : Sends a photo through photo_id or file.
        {AUDIO} <audio_id/path_to_file> <other_params> : Sends an audio throuhg audio_id or file.
        {DOCUMENT} <document_id/path_to_file> <other_params> : sends a document through document_id or file.
        {VIDEO} <video_id/path_to_file> <other_params> : sends a video through document_id or file.
        {VOICE} <voice_id/path_to_file> <other_params> : sends a voice through voice_id or file.
        {ANIMATION} <animation_id/path_to_file> <other_params> : sends an annimation through animation_id or file.
        {VIDEONOTE} <videonote_id/path_to_file> <other_params> : sends a videonote through videonote_id or file.
        {LOCATION} {LATITUDE} <latitude> {LONGITUDE} <longitude> <other_params> : sends a location.
        {VENUE} {LATITUDE} <latitude> {LONGITUDE} <longitude> {TITLE} <title> {ADDRESS} <address> <other_params> : sends a venue.
        {CONTACT} {PHONE_NUMBER} <phone_number> {FIRST_NAME} <first_name> <other_params> : sends a contact.
        {POLL} {QUESTION} <question> {OPTIONS} <options> <other_params> : sends a poll.
        {DICE} <other_params> : sends a dice.
        
        To see which parameters are allowed as <other_params> use >notify {HELP_1} <command>
        <other_params> can be omitted if you wish to use the default/selected profile ones

    Es: notify {PROFILE} test_name {PHOTO} path/to/photo.jpg {CAPTION} caption
        Sends a photo with caption using the profile test_name

"""
    else:
        
        type = sys.argv[2]

        if type == PARAMETERS:
            message = f"""the list of all parameters you can use with their description.
Each parameter is not guaranteed to work for each notify command.
Use notify {HELP_1} <notify_command> or {HELP_2} <notify_command> to get the list of parameters accepted for each command.

"""
            for exp in explanation:
                message = message + explanation[exp] + "\n"
        elif type == PROFILE:
            message = f"""the explanation of the {PROFILE} command.
> notify {PROFILE} <proile_params> ...
    <profile_params>:
        <name> : the name of the profile to load (if used, it's the first parameter. Es: notify {PROFILE} <name> <other_params>)
        {TOKEN} <token> : the token to use. If both token and name of the profile are specified, the token specified will have priority over the one stored in the profile.
    If the {PROFILE} <profile_params> is omitted, the 'default' profile found inside the configuration file will be used.
"""
        elif type == TEXT:
            message = f"""the explanation of the {TEXT} command.
> notify <optional_profile_setup> {TEXT} <text/file> <text_params>
    <text/file> : The text to write in the message or the path to a text file containing the text to send (is used, it's the first parameter. Es: notify -t text of the message <other_params>)
    <text_params>:
        {explanation[CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[PARSE_MODE]}
        {explanation[ENTITIES]}
        {explanation[DISABLE_WEB_PAGE_PREVIEW]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
        {explanation[REPLY_TO_MESSAGE_ID]}
        {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
        {explanation[REPLY_MARKUP]}
"""
        elif type == COPY:
            message = f"""the explanation of the {COPY} command.
> notify <optional_profile_setup> {COPY} {MESSAGE_ID} <message_id> {CHAT_ID} <chat_id> <send_params>
    {explanation[MESSAGE_ID]}
    {explanation[CHAT_ID]}
    <send_params>:
        {explanation[FROM_CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[CAPTION]}
        {explanation[PARSE_MODE]}
        {explanation[CAPTION_ENTITIES]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
        {explanation[REPLY_TO_MESSAGE_ID]}
        {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
        {explanation[REPLY_MARKUP]}
"""
        elif type == FORWARD:
            message = f"""the explanation of the {FORWARD} command.
> notify <optional_profile_setup> {FORWARD} {MESSAGE_ID} <message_id> {CHAT_ID} <chat_id> <forward_params>
    {explanation[MESSAGE_ID]}
    {explanation[CHAT_ID]}
    <forward_params>:
        {explanation[FROM_CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
"""
        elif type == PHOTO:
            message = f"""the explanation of the {PHOTO} command.
> notify <optional_profile_setup> {PHOTO} <file_path/photo_id> <photo_params>
    <file_path/photo_id> : Path to the file to send of the photo id to use.
    <photo_params>:
        {explanation[CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[CAPTION]}
        {explanation[PARSE_MODE]}
        {explanation[CAPTION_ENTITIES]}
        {explanation[HAS_SPOILER]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
        {explanation[REPLY_TO_MESSAGE_ID]}
        {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
        {explanation[REPLY_MARKUP]}
"""
        elif type == AUDIO:
            message = f"""the explanation of the {AUDIO} command.
> notify <optional_profile_setup> {AUDIO} <file_path/audio_id> <audio_params>
    <file_path/audio_id> : Path to the file to send of the audio id to use.
    <audio_params>:
        {explanation[CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[CAPTION]}
        {explanation[PARSE_MODE]}
        {explanation[CAPTION_ENTITIES]}
        {explanation[DURATION]}
        {explanation[PERFORMER]}
        {explanation[TITLE]}
        {explanation[THUMBNAIL]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
        {explanation[REPLY_TO_MESSAGE_ID]}
        {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
        {explanation[REPLY_MARKUP]}
    """
        elif type == DOCUMENT: #TODO
            message = f"""the explanation of the {DOCUMENT} command.
> notify <optional_profile_setup> {DOCUMENT} <file_path/document_id> <document_params>
    <file_path/document_id> : Path to the file to send of the document id to use.
    <document_params>:
        {explanation[CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[THUMBNAIL]}
        {explanation[CAPTION]}
        {explanation[PARSE_MODE]}
        {explanation[CAPTION_ENTITIES]}
        {explanation[DISABLE_CONTENT_TYPE_DETECTION]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
        {explanation[REPLY_TO_MESSAGE_ID]}
        {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
        {explanation[REPLY_MARKUP]}
"""
        elif type == VIDEO:
            message = f"""the explanation of the {VIDEO} command.
> notify <optional_profile_setup> {VIDEO} <file_path/video_id> <video_params>
    <file_path/video_id> : Path to the file to send of the video id to use.
    <video_params>:
        {explanation[CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[DURATION]}
        {explanation[WIDTH]}
        {explanation[HEIGHT]}
        {explanation[THUMBNAIL]}
        {explanation[CAPTION]}
        {explanation[PARSE_MODE]}
        {explanation[CAPTION_ENTITIES]}
        {explanation[HAS_SPOILER]}
        {explanation[SUPPORTS_STREAMING]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
        {explanation[REPLY_TO_MESSAGE_ID]}
        {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
        {explanation[REPLY_MARKUP]}
"""
        elif type == VOICE:
            message = f"""the explanation of the {VOICE} command.
> notify <optional_profile_setup> {VOICE} <file_path/voice_id> <voice_params>
    <file_path/voice_id> : Path to the file to send of the voice id to use.
    <voice_params>:
        {explanation[CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[DURATION]}
        {explanation[CAPTION]}
        {explanation[PARSE_MODE]}
        {explanation[CAPTION_ENTITIES]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
        {explanation[REPLY_TO_MESSAGE_ID]}
        {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
        {explanation[REPLY_MARKUP]}
"""
        elif type == ANIMATION:
            message = f"""the explanation of the {ANIMATION} command.
> notify <optional_profile_setup> {ANIMATION} <file_path/animation_id> <animation_params>
    <file_path/animation_id> : Path to the file to send of the animation id to use.
    <animation_params>:
        {explanation[CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[DURATION]}
        {explanation[WIDTH]}
        {explanation[HEIGHT]}
        {explanation[THUMBNAIL]}
        {explanation[CAPTION]}
        {explanation[PARSE_MODE]}
        {explanation[CAPTION_ENTITIES]}
        {explanation[HAS_SPOILER]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
        {explanation[REPLY_TO_MESSAGE_ID]}
        {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
        {explanation[REPLY_MARKUP]}
"""
        elif type == VIDEONOTE:
            message = f"""the explanation of the {VIDEONOTE} command.
> notify <optional_profile_setup> {VIDEONOTE} <file_path/videonote_id> <videonote_params>
    <file_path/videonote_id> : Path to the file to send of the videonote id to use.
    <videonote_params>:
        {explanation[CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[DURATION]}
        {explanation[LENGTH]}
        {explanation[THUMBNAIL]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
        {explanation[REPLY_TO_MESSAGE_ID]}
        {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
        {explanation[REPLY_MARKUP]}
"""
        elif type == LOCATION:
            message = f"""the explanation of the {LOCATION} command.
> notify <optional_profile_setup> {LOCATION} {LATITUDE} <latitude> {LONGITUDE} <longitude> <location_params>
    {explanation[LATITUDE]}
    {explanation[LONGITUDE]}
    <location_params>:
        {explanation[CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[HORIZONTAL_ACCURACY]}
        {explanation[LIVE_PERIOD]}
        {explanation[HEADING]}
        {explanation[PROXIMITY_ALERT_RADIUS]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
        {explanation[REPLY_TO_MESSAGE_ID]}
        {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
        {explanation[REPLY_MARKUP]}
"""
        elif type == VENUE:
            message = f"""the explanation of the {VENUE} command.
> notify <optional_profile_setup> {VENUE} {LATITUDE} <latitude> {LONGITUDE} <longitude> {TITLE} <title> {ADDRESS} <address> <venue_params>
    {explanation[LATITUDE]}
    {explanation[LONGITUDE]}
    {explanation[TITLE]}
    {explanation[ADDRESS]}
    <venue_params>:
        {explanation[CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[FOURSQUARE_ID]}
        {explanation[FOURSQUARE_TYPE]}
        {explanation[GOOGLE_PLACE_ID]}
        {explanation[GOOGLE_PLACE_TYPE]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
        {explanation[REPLY_TO_MESSAGE_ID]}
        {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
        {explanation[REPLY_MARKUP]}
"""
        elif type == CONTACT:
            message = f"""the explanation of the {CONTACT} command.
> notify <optional_profile_setup> {CONTACT} {PHONE_NUMBER} <phone_number> {FIRST_NAME} <first_name> <contact_params>
    {explanation[PHONE_NUMBER]}
    {explanation[FIRST_NAME]}
    <contact_params>:
        {explanation[CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[LAST_NAME]}
        {explanation[VCARD]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
        {explanation[REPLY_TO_MESSAGE_ID]}
        {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
        {explanation[REPLY_MARKUP]}
"""
        elif type == POLL:
            message = f"""the explanation of the {POLL} command.
> notify <optional_profile_setup> {POLL} {QUESTION} <question> {OPTIONS} <options> <poll_params>
    {explanation[QUESTION]}
    {explanation[OPTIONS]}
    <poll_params>:
        {explanation[CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[IS_ANONYMOUS]}
        {explanation[TYPE]}
        {explanation[ALLOWS_MULTIPLE_ANSWERS]}
        {explanation[CORRECT_OPTION_ID]}
        {explanation[EXPLANATION]}
        {explanation[EXPLANATION_PARSE_MODE]}
        {explanation[EXPLANATION_ENTITIES]}
        {explanation[OPEN_PERIOD]}
        {explanation[CLOSE_DATE]}
        {explanation[IS_CLOSED]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
        {explanation[REPLY_TO_MESSAGE_ID]}
        {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
        {explanation[REPLY_MARKUP]}
"""
        elif type == DICE:
            message = f"""the explanation of the {DICE} command.
> notify <optional_profile_setup> {DICE} <dice_params>
    <dice_params>:
        {explanation[CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
        {explanation[EMOJI]}
        {explanation[DISABLE_NOTIFICATION]}
        {explanation[PROTECT_CONTENT]}
        {explanation[REPLY_TO_MESSAGE_ID]}
        {explanation[ALLOW_SENDING_WITHOUT_REPLY]}
        {explanation[REPLY_MARKUP]}
"""
        elif type == ACTION:
            message = f"""the explanation of the {ACTION} command.
> notify <optional_profile_setup> {ACTION} <chat_action> <action_params>
    {explanation[ACTION]}
    <action_params>:
        {explanation[CHAT_ID]}
        {explanation[MESSAGE_THREAD_ID]}
"""
        elif type == EDIT:
            message = f"""the explanation of the {EDIT} command."""
        #...
        else:
            print(help_error)
            exit(1)
    
    print(help_beginning + message + help_conclusion)
    
def ntf_update():

    if len(sys.argv) == 3 and sys.argv[2] != PROD and sys.argv[2] != DEV:
        print(error)
        exit(1)

    r = requests.get('https://raw.githubusercontent.com/Zanzibarr/Telegram_Python_Notifier/main/change_log.md')
    new_version = r.text.partition("Version ")[2].partition("\n")[0]

    if len(sys.argv) == 2 or sys.argv[2] == PROD:

        if "200" in str(r):
            _1, _2, _3 = version.partition(": ")[2].partition(".")
            old = _1 + _2 + _3.partition(".")[0]
            _1, _2, _3 = new_version.partition(".")
            new = _1 + _2 + _3.partition(".")[0]
            if old == new:
                print("notify is already up-to-date")
                exit(0)

        else:
            print(f"Request to find latest version had as response: {r}.\nUpdate failed")
            exit(1)

    print("Downloading latest version...")
    for file in files:
        with open(f"{base_path}/{file}", "w") as f:
            f.write(download_file_content(file))
    subprocess.run(shlex.split(f"mv {base_path}/notify.py {base_path}/python_module/"))

    print(f"Update completed.\nnotify version: {new_version}")

def download_file_content(name):

    r = requests.get(f'https://raw.githubusercontent.com/Zanzibarr/Telegram_Python_Notifier/main/{name}')

    if "200" not in str(r):
        print(f"Request to download updated files had as response: {r}.Request failed.")
        exit(1)
    
    return r.text

def ntf_uninstall(): 
        
    choice = input("Proceeding to uninstall notify? [y/n]: ")
    while choice not in ("y", "n"):
        choice = input(f"{command_error}Proceeding to uninstall notify? [y/n]: ")

    if choice == "n":
        print("Uninstall aborted.")
        exit(0)
    
    print("Uninstalling...")
    subprocess.run(shlex.split(f"rm -r {home}/.notify_zanz"))
    
    if os.path.exists(f"{home}/.bashrc"):
        bashrc = ""
        with open(f"{home}/.bashrc", "r") as f:
            bashrc = f.read()
        bashrc = bashrc.replace(bashrc_edit_title, "")
        bashrc = bashrc.replace(bashrc_edit_content, "")
        with open(f"{home}/.bashrc", "w") as f:
            f.write(bashrc)
    if os.path.exists(f"{home}/.zshrc"):
        zshrc = ""
        with open(f"{home}/.zshrc", "r") as f:
            zshrc = f.read()
        zshrc = zshrc.replace(bashrc_edit_title, "")
        zshrc = zshrc.replace(bashrc_edit_content, "")
        with open(f"{home}/.zshrc", "w") as f:
            f.write(zshrc)
    print("notify has been succesfully uninstalled.")

if not os.path.exists(std_config_path):
    choice = "n"
    if os.path.exists(old_config_path):

        choice = input(f"Found a configuration file ({old_config_path}) from a past version.\nUse that configuration to create a default profile? [y/n/q to quit]: ")
        while choice not in ("y", "n", "q"):
            choice = input("Command not recognised.\nUse that configuration to create a default profile? [y/n/q to quit]: ")

        if choice == "q":
            print("notify not installed.\nExiting setup.")
            exit(0)

        if choice == "y":
            with open(old_config_path, "r") as f:
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
            with open(std_config_path, "r") as f:
                profiles = json.loads(f.read())
            profiles["def"] = name
            with open(std_config_path, "w") as f:
                f.write(json.dumps(profiles, indent=4))

            print("Profile created.\nYou can edit configuration parameters later on using notify (use the help function).")

    choice = input(f"Removing old credentials file ({old_config_path})? [y/n]: ")
    while choice not in ("y", "n"):
        choice = input(f"Command not recognised.\nRemoving old credentials file ({old_config_path})? [y/n]: ")

    if choice == "y":
        subprocess.run(shlex.split(f"rm {old_config_path}"))

with open(std_config_path, "r") as f:
    bot = notify.bot(profile=json.loads(f.read())["def"])

if __name__ == "__main__":
    main()
