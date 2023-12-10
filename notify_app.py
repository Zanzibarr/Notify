import subprocess, notify, requests, shlex, json, sys, os

HELP_1 = "-help"
HELP_2 = "-h"
PARAMETERS = "-param"
VERSION = "-version"
UPDATE_1 = "-update"
UPDATE_2 = "-u"
PROD = "-prod"
DEV = "-dev"
CONF_1 = "-conf"
CONF_2 = "-c"
ADD = "-add"
TOKEN = "-token"
REMOVE = "-rm"
SET = "-set"
SEE = "-see"
UNINSTALL = "-uninstall"
PROFILE = "-prof"
TEXT = "-t"
COPY = "-cpy"
FORWARD = "-frw"
PHOTO = "-p"
AUDIO = "-a"
DOCUMENT = "-d"
VIDEO = "-v"
VOICE = "-voice"
ANIMATION = "-anim"
VIDEONOTE = "-vnote"
LOCATION = "-loc"
VENUE = "-ven"
CONTACT = "-cnt"
POLL = "-pll"
DICE = "-dice"
ACTION = "-act"
EXCEPTION = "-exc"
CHAT_ID = "-chat"
MESSAGE_THREAD_ID = "-mt_id"
REPLY_TO_MESSAGE_ID = "-reply"
MESSAGE_ID = "-message"
FROM_CHAT_ID = "-from"
INLINE_MESSAGE_ID = "-inline_id"
ENTITIES = "-entities"
CAPTION = "-caption"
CAPTION_ENTITIES = "-caption_entities"
PARSE_MODE = "-parse"
REPLY_MARKUP = "-reply_markup"
DURATION = "-duration"
LENGTH = "-length"
PERFORMER = "-performer"
TITLE = "-title"
THUMBNAIL = "-thumb_path"
WIDTH = "-width"
HEIGHT = "-height"
LATITUDE = "-lat"
LONGITUDE = "-lon"
HORIZONTAL_ACCURACY = "-accuracy"
LIVE_PERIOD = "-live_period"
HEADING = "-heading"
PROXIMITY_ALERT_RADIUS = "-alert_radius"
ADDRESS = "-address"
FOURSQUARE_ID = "-foursquare_id"
FOURSQUARE_TYPE = "-foursquare_type"
GOOGLE_PLACE_ID = "-google_place_id"
GOOGLE_PLACE_TYPE = "-google_place_type"
PHONE_NUMBER = "-number"
FIRST_NAME = "-name"
LAST_NAME = "-surname"
VCARD = "-vcard"
QUESTION = "-question"
OPTIONS = "-options"
TYPE = "-type"
CORRECT_OPTION_ID = "-correct"
EXPLANATION = "-explanation"
EXPLANATION_PARSE_MODE = "-exp_parse"
EXPLANATION_ENTITIES = "-exp_entities"
OPEN_PERIOD = "-period"
CLOSE_DATE = "-close_date"
EMOJI = "-emoji"
DISABLE_WEB_PAGE_PREVIEW = "-no_webp_preview"
DISABLE_NOTIFICATION = "-silent"
PROTECT_CONTENT = "-protect_content"
ALLOW_SENDING_WITHOUT_REPLY = "-reply_anyway"
HAS_SPOILER = "-spoiler"
DISABLE_CONTENT_TYPE_DETECTION = "-no_ctype_det"
SUPPORTS_STREAMING = "-streaming"
IS_ANONYMOUS = "-anon"
ALLOWS_MULTIPLE_ANSWERS = "-multiple"
IS_CLOSED = "-is_closed"
EDIT = "-edit"

SHORTCUT_COMMANDS = [DISABLE_WEB_PAGE_PREVIEW, DISABLE_NOTIFICATION, HAS_SPOILER, DISABLE_CONTENT_TYPE_DETECTION, SUPPORTS_STREAMING, IS_ANONYMOUS, ALLOWS_MULTIPLE_ANSWERS, ALLOW_SENDING_WITHOUT_REPLY, IS_CLOSED, PROTECT_CONTENT]

explanation = {
    CHAT_ID : f"{CHAT_ID} <chat_id> : chat to send the message to.",
    MESSAGE_THREAD_ID : f"{MESSAGE_THREAD_ID} <thread_id> : Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.",
    PARSE_MODE : f"{PARSE_MODE} <parse_mode> : Mode for parsing entities in the message text/caption. See site for more details.",
    ENTITIES : f"{ENTITIES} <TODO> : TODO",
    DISABLE_WEB_PAGE_PREVIEW : f"{DISABLE_WEB_PAGE_PREVIEW} : <bool> : Disables link previews for links in this message.",
    DISABLE_NOTIFICATION : f"{DISABLE_NOTIFICATION} <bool> : Sends the message silently. Users will receive a notification with no sound.",
    PROTECT_CONTENT : f"{PROTECT_CONTENT} <bool> : Protects the contents of the sent message from forwarding and saving.",
    REPLY_TO_MESSAGE_ID : f"{REPLY_TO_MESSAGE_ID} <message_id> : If the message is a reply, ID of the original message.",
    ALLOW_SENDING_WITHOUT_REPLY : f"{ALLOW_SENDING_WITHOUT_REPLY} <bool> : Pass True if the message should be sent even if the specified replied-to message is not found.",
    REPLY_MARKUP : f"{REPLY_MARKUP} <TODO> : TODO",
    MESSAGE_ID : f"{MESSAGE_ID} <message_id> : the message to copy/forward.",
    FROM_CHAT_ID : f"{FROM_CHAT_ID} <chat_id> : chat_id of the message to copy/forward.",
    CAPTION : f"{CAPTION} <caption> : Caption, 0-1024 characters after entities parsing. If not specified, the original caption is kept.",
    CAPTION_ENTITIES : f"{CAPTION_ENTITIES} <TODO> : TODO",
    HAS_SPOILER : f"{HAS_SPOILER} <bool> : Pass True if the file needs to be covered with a spoiler animation.",
    DURATION : f"{DURATION} <duration> : Duration in seconds.",
    PERFORMER : f"{PERFORMER} <performer> : Performer",
    TITLE : f"{TITLE} <title> : Title",
    THUMBNAIL : f"{THUMBNAIL} <thumbnail_path> : Path of the Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.",
    DISABLE_CONTENT_TYPE_DETECTION : f"{DISABLE_CONTENT_TYPE_DETECTION} <bool> : Disables automatic server-side content type detection for files uploaded using multipart/form-data",
    WIDTH : f"{WIDTH} <width> : Video/Animation width",
    HEIGHT : f"{HEIGHT} <height> : Video/Animation height",
    SUPPORTS_STREAMING : f"{SUPPORTS_STREAMING} <bool> : Pass True if the uploaded video is suitable for streaming",
    LENGTH : f"{LENGTH} <length> : Length of the video note.",
    LATITUDE : f"{LATITUDE} <latitude> : Latitude.",
    LONGITUDE : f"{LONGITUDE} <longitude> : Longitude.",
    HORIZONTAL_ACCURACY : f"{HORIZONTAL_ACCURACY} <horizontal_accuracy> : The radius of uncertainty for the location, measured in meters; 0-1500.",
    LIVE_PERIOD : f"{LIVE_PERIOD} <live_period> : Period in seconds for which the location will be updated, should be between 60 and 86400.",
    HEADING : f"{HEADING} <heading> : For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.",
    PROXIMITY_ALERT_RADIUS : f"{PROXIMITY_ALERT_RADIUS} <alert_radius> : For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.",
    ADDRESS : f"{ADDRESS} <address> : Address of the venue.",
    FOURSQUARE_ID : f"{FOURSQUARE_ID} <foursquare_id> : Foursquare identifier of the venue, if known.",
    FOURSQUARE_TYPE : f"{FOURSQUARE_TYPE} <foursquare_type> : Foursquare type of the venue, if known.",
    GOOGLE_PLACE_ID : f"{GOOGLE_PLACE_ID} <googleplace_id> : Google Places identifier of the venue.",
    GOOGLE_PLACE_TYPE : f"{GOOGLE_PLACE_TYPE} <googleplace_type> : Google Places type of the venue",
    PHONE_NUMBER : f"{PHONE_NUMBER} <phone_number> : Contact's phone number.",
    FIRST_NAME : f"{FIRST_NAME} <first_name> : Contact's first name.",
    LAST_NAME : f"{LAST_NAME} <last_name> : Contact's last name.",
    VCARD : f"{VCARD} <vcard> : Additional data about the contact in the form of a vCard.",
    QUESTION : f"{QUESTION} <question> : Poll question.",
    OPTIONS : f"{OPTIONS} <TODO> : TODO",
    IS_ANONYMOUS : F"{IS_ANONYMOUS} <bool> : True, if the poll needs to be anonymous.",
    TYPE : f"{TYPE} <type> : Poll type.",
    ALLOWS_MULTIPLE_ANSWERS : f"{ALLOWS_MULTIPLE_ANSWERS} <bool> : Allows multiple answers if True.",
    CORRECT_OPTION_ID : f"{CORRECT_OPTION_ID} <option_id> : ID of the correct answer for quizzes.",
    EXPLANATION : f"{EXPLANATION} <explanation> : Explanation for the correct answer.",
    EXPLANATION_PARSE_MODE : f"{EXPLANATION_PARSE_MODE} <explanation_parse_mode> : Mode for parsing entities in the explanation.",
    EXPLANATION_ENTITIES : f"{EXPLANATION_ENTITIES} <TODO> : TODO",
    OPEN_PERIOD : f"{OPEN_PERIOD} <open_period> : Time in seconds for which the poll will be active.",
    CLOSE_DATE : f"{CLOSE_DATE} <close_date> : UNIX timestamp for the poll's closing date.",
    IS_CLOSED : f"{IS_CLOSED} <bool> : Closes the poll if True.",
    EMOJI : f"{EMOJI} <emoji> : Emoji symbolizing the dice throw animation (see the site).",
    ACTION : f"{ACTION} <chat_action> : Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_voice or upload_voice for voice notes, upload_document for general files, choose_sticker for stickers, find_location for location data, record_video_note or upload_video_note for video notes."
}

version = "notify version: 1.9.0"

nerror = "Notify error: "
suggestion = "Use notify -h or notify -help to get instructions."
command_error = f"\n{nerror}command not recognised.\n{suggestion}\n"

error = f"\n{nerror}wrong arguments.\n{suggestion}\n"

profile_error = f"\n{nerror}must specify at least the profile or the token.\n{suggestion}\n"
add_conf_error = f"\n{nerror}must specify at least both name and token.\n{suggestion}\n"
set_conf_error = f"\n{nerror}must specify a name.\n{suggestion}\n"

message_error = f"\n{nerror}either specify a text message to send, or a file to read.\n{suggestion}\n"
copy_error = f"\n{nerror}both message id and chat id must be specified.\n{suggestion}\n"
forward_error = copy_error
photo_error = f"\n{nerror}either specify a photo_id/web_url or the path to the photo to send.\n{suggestion}\n"
audio_error = f"\n{nerror}either specify a audio_id/web_url or the path to the audio to send.\n{suggestion}\n"
doc_error = f"\n{nerror}either specify a document_id/web_url or the path to the doc to send.\n{suggestion}\n"
video_error = f"\n{nerror}either specify a video_id/web_url or the path to the doc to send.\n{suggestion}\n"
voice_error = f"\n{nerror}either specify a voice_id/web_url or the path to the voice to send.\n{suggestion}\n"
animation_error = f"\n{nerror}either specify an animation_id/web_url or the path to the animation to send.\n{suggestion}"
videonote_error = f"\n{nerror}either specify a videonote_id/web_url or the path to the videonote to send.\n{suggestion}"
location_error = f"\n{nerror}both latitude and longitude must be specified.\n{suggestion}"
venue_error = f"\n{nerror}latitude, longitude, title and address must be specified.\n{suggestion}"
contact_error = f"\n{nerror}both phone number and name must be specified.\n{suggestion}"
poll_error = f"\n{nerror}both question and option must be specified.\n{suggestion}"
action_error = f"\n{nerror}naction must be specified.\n{suggestion}"
help_error = f"\n{nerror}either don't specify anything to have the full help message, or specify a notify command (not a parameter,t o see the parameters description use {PARAMETERS})."

bashrc_edit_title = "#notify - zanzi"
bashrc_edit_content = """alias notify='python3 $HOME/.notify_zanz/notify_app.py'
export PYTHONPATH=$HOME/.notify_zanz/python_module
"""

home = os.path.expanduser('~')
base_path = os.path.dirname(os.path.abspath(__file__))
old_config_path = f"{home}/.zanz_notify_config"
std_config_path = f"{home}/.zanz_notify_profiles"
conf_file_info = f"""
Configuration file: {std_config_path}"""
files = ["notify.py", "notify_app.py", "change_log.md", "readme.md"]

help_beginning = "Hi! Thanks for using notify!\n\nIf this instructions are not helping, please open an issue on github or give a look to the telegram API website (linked at the end of this message).\n\nHere's """
help_conclusion = f"""
SHORTCUTS:

- For each bool parameter, '--<param>' is equal to '-<param> true'


Base folder: {base_path}
Credentials folder: {std_config_path}
Base repository: https://github.com/Zanzibarr/Telegram_Python_Notifier
Telegram API explanation: https://core.telegram.org/bots/api

{version}
"""

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
            print(error)
            exit(1)

        elif sys.argv[1] in (HELP_1, HELP_2):
            if len(sys.argv) not in (2, 3):
                print(error)
                exit(1)

            help()
            exit(0)

        elif sys.argv[1] in (UPDATE_1, UPDATE_2):
            if len(sys.argv) not in (2, 3):
                print(error)
                exit(1)

            ntf_update()
            exit(0)

        elif sys.argv[1] == UNINSTALL:
            if len(sys.argv) > 2:
                print(error)
                exit(1)

            ntf_uninstall()
            exit(0)

        elif sys.argv[1] == VERSION:
            if len(sys.argv) > 2:
                print(error)
                exit(1)

            print(version)
            exit(0)

        elif sys.argv[1] in (CONF_1, CONF_2):
            
            command = " ".join(sys.argv[1:])
            ntf_config()

            if len(command.strip()) > 0:
                print(f"\nIgnored parts of the input: {command}\n{suggestion}\n")

            exit(0)

        command = " ".join(sys.argv[1:])

        if sys.argv[1] == PROFILE:

            ntf_profile()

        index = command.find(EDIT)
        if index < 0:
            ntf_send()
        elif index == 0:
            print("UNIMPLEMENTED")#ntf_edit() #TODO
        else:
            print(error)
            exit(1)

        if len(command.strip()) > 0:
            print(f"\nMessage sent successfully.\nIgnored parts of the input: {command}\n{suggestion}\n")

    except Exception as e:
        print(e)

def ntf_config():

    global command
    
    command = command[6:]

    if command == "":
        print(conf_file_info)
        exit(0)

    type = command.partition(" ")[0]

    if type == ADD:

        name = get(ADD)
        token = get(TOKEN)

        if name == "" or token == "":
            print(add_conf_error)
            exit(1)

        notify.write_conf_profile(name=name, token=token, from_chat_id=get(FROM_CHAT_ID), to_chat_id=get(CHAT_ID), disable_web_page_preview=get(DISABLE_WEB_PAGE_PREVIEW), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), parse_mode=get(PARSE_MODE))
        
    elif type == REMOVE:

        name = get(REMOVE)

        notify.remove_profile(name)

    elif type == SET:

        name = get(SET)

        if name == "":
            print(set_conf_error)
            exit(1)

        with open(std_config_path, "r") as f:
            profiles = json.loads(f.read())
        
        if name not in [i for i in profiles["profiles"].keys()]:
            print("The name specified was not found in the profiles configuration file.\nNot changing the default profile.")
            exit(0)

        profiles["def"] = name

        with open(std_config_path, "w") as f:
            f.write(json.dumps(profiles, indent=4))

    elif type == SEE:

        get(SEE)

        print(notify.get_profiles())

    else:

        print(command_error)
        exit(1)

def ntf_profile():

    global command

    token = get(TOKEN)
    profile = get(PROFILE)

    if profile == "" and token == "":
        print(profile_error)
        exit(1)

    bot.load_profile(token=token, name=profile)

def ntf_send():

    type = command.partition(" ")[0]

    if type == TEXT:

        content = get(TEXT)

        if content == "":
            print(message_error)
            exit(1)

        if ispath(content):
            response = bot.send_message_by_file(file_path=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), parse_mode=get(PARSE_MODE), entities=get(ENTITIES), disable_web_page_preview=get(DISABLE_WEB_PAGE_PREVIEW), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))
        else:
            response = bot.send_message_by_text(text=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), parse_mode=get(PARSE_MODE), entities=get(ENTITIES), disable_web_page_preview=get(DISABLE_WEB_PAGE_PREVIEW), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))

    elif type == COPY:

        message_id = get(MESSAGE_ID)
        chat_id = get(CHAT_ID)
        if message_id == "" and chat_id == "":
            print(copy_error)
            exit(1)

        response = bot.copy_message(message_id=message_id, chat_id=chat_id, from_chat_id=get(FROM_CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), caption=get(CAPTION), parse_mode=get(PARSE_MODE), caption_entities=get(CAPTION_ENTITIES), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))

    elif type == FORWARD:

        message_id = get(MESSAGE_ID)
        chat_id = get(CHAT_ID)
        if message_id == "" and chat_id == "":
            print(forward_error)
            exit(1)

        response = bot.forward_message(message_id=message_id, chat_id=chat_id, from_chat_id=get(FROM_CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT))

    elif type == PHOTO:

        content = get(PHOTO)

        if content == "":
            print(photo_error)
            exit(1)

        if ispath(content):
            response = bot.send_photo_by_path(file_path=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), caption=get(CAPTION), parse_mode=get(PARSE_MODE), caption_entities=get(CAPTION_ENTITIES), has_spoiler=get(HAS_SPOILER), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))
        else:
            response = bot.send_photo(photo=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), caption=get(CAPTION), parse_mode=get(PARSE_MODE), caption_entities=get(CAPTION_ENTITIES), has_spoiler=get(HAS_SPOILER), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))
            
    elif type == AUDIO:

        content = get(AUDIO)

        if content == "":
            print(audio_error)
            exit(1)

        if ispath(content):
            response = bot.send_audio_by_path(file_path=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), caption=get(CAPTION), parse_mode=get(PARSE_MODE), caption_entities=get(CAPTION_ENTITIES), duration=get(DURATION), performer=get(PERFORMER), title=get(TITLE), thumbnail=get(THUMBNAIL), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))
        else:
            response = bot.send_audio(audio=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), caption=get(CAPTION), parse_mode=get(PARSE_MODE), caption_entities=get(CAPTION_ENTITIES), duration=get(DURATION), performer=get(PERFORMER), title=get(TITLE), thumbnail=get(THUMBNAIL), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))

    elif type == DOCUMENT:

        content = get(DOCUMENT)

        if content == "":
            print(doc_error)
            exit(1)

        if ispath(content):
            response = bot.send_document_by_path(file_path=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), thumbnail=get(THUMBNAIL), caption=get(CAPTION), parse_mode=get(PARSE_MODE), caption_entities=get(CAPTION_ENTITIES), disable_content_type_detection=get(DISABLE_CONTENT_TYPE_DETECTION), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))
        else:
            response = bot.send_document(document=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), thumbnail=get(THUMBNAIL), caption=get(CAPTION), parse_mode=get(PARSE_MODE), caption_entities=get(CAPTION_ENTITIES), disable_content_type_detection=get(DISABLE_CONTENT_TYPE_DETECTION), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))

    elif type == VIDEO:

        content = get(VIDEO)

        if content == "":
            print(video_error)
            exit(1)

        if ispath(content):
            response = bot.send_video_by_path(file_path=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), duration=get(DURATION), width=get(WIDTH), height=get(HEIGHT), thumbnail=get(THUMBNAIL), caption=get(CAPTION), parse_mode=get(PARSE_MODE), caption_entities=get(CAPTION_ENTITIES), has_spoiler=get(HAS_SPOILER), supports_streaming=get(SUPPORTS_STREAMING), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))
        else:
            response = bot.send_video(video=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), duration=get(DURATION), width=get(WIDTH), height=get(HEIGHT), thumbnail=get(THUMBNAIL), caption=get(CAPTION), parse_mode=get(PARSE_MODE), caption_entities=get(CAPTION_ENTITIES), has_spoiler=get(HAS_SPOILER), supports_streaming=get(SUPPORTS_STREAMING), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))
        
    elif type == VOICE:

        content = get(VOICE)

        if content == "":
            print(voice_error)
            exit(1)

        if ispath(content):
            response = bot.send_voice_by_path(file_path=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), caption=get(CAPTION), parse_mode=get(PARSE_MODE), caption_entities=get(CAPTION_ENTITIES), duration=get(DURATION), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))
        else:
            response = bot.send_voice(voice=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), caption=get(CAPTION), parse_mode=get(PARSE_MODE), caption_entities=get(CAPTION_ENTITIES), duration=get(DURATION), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))

    elif type == ANIMATION:

        content = get(ANIMATION)

        if content == "":
            print(animation_error)
            exit(1)

        if ispath(content):
            response = bot.send_animation_by_path(file_path=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), duration=get(DURATION), width=get(WIDTH), height=get(HEIGHT), thumbnail=get(THUMBNAIL), caption=get(CAPTION), parse_mode=get(PARSE_MODE), caption_entities=get(CAPTION_ENTITIES), has_spoiler=get(HAS_SPOILER), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))
        else:
            response = bot.send_animation(animation=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), duration=get(DURATION), width=get(WIDTH), height=get(HEIGHT), thumbnail=get(THUMBNAIL), caption=get(CAPTION), parse_mode=get(PARSE_MODE), caption_entities=get(CAPTION_ENTITIES), has_spoiler=get(HAS_SPOILER), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))

    elif type == VIDEONOTE:

        content = get(VIDEONOTE)

        if content == "":
            print(videonote_error)
            exit(1)

        if ispath(content):
            response = bot.send_videonote_by_path(file_path=content, cchat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), duration=get(DURATION), length=get(LENGTH), thumbnail=get(THUMBNAIL), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))
        else:
            response = bot.send_videonote(videonote=content, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), duration=get(DURATION), length=get(LENGTH), thumbnail=get(THUMBNAIL), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))

    elif type == LOCATION:

        lat = get(LATITUDE)
        lon = get(LONGITUDE)

        if lat == "" or lon == "":
            print(location_error)
            exit(1)

        response = bot.send_location(latitude=lat, longitude=lon, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), horizontal_accuracy=get(HORIZONTAL_ACCURACY), live_period=get(LIVE_PERIOD), heading=get(HEADING), proximity_alert_radius=get(PROXIMITY_ALERT_RADIUS), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))

    elif type == VENUE:

        lat = get(LATITUDE)
        lon = get(LONGITUDE)
        title = get(TITLE)
        address = get(ADDRESS)

        if lat == "" or lon == "" or title == "" or address == "":
            print(venue_error)
            exit(1)

        response = bot.send_venue(latitude=lat, longitude=lon, title=title, address=address, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), foursquare_id=get(FOURSQUARE_ID), foursquare_type=get(FOURSQUARE_TYPE), google_place_id=get(GOOGLE_PLACE_ID), google_place_type=get(GOOGLE_PLACE_TYPE), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))

    elif type == CONTACT:

        number = get(PHONE_NUMBER)
        name = get(FIRST_NAME)

        if number == "" or name == "":
            print(contact_error)
            exit(1)

        response = bot.send_contact(phone_number=number, first_name=name, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), last_name=get(LAST_NAME), vcard=get(VCARD), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))

    elif type == POLL:

        question = get(QUESTION)
        options = get(OPTIONS)

        if question == "" or options == "":
            print(poll_error)
            exit(1)

        response = bot.send_poll(question=question, options=options, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), is_anonymous=get(IS_ANONYMOUS), type=get(TYPE), allows_multiple_answers=get(ALLOWS_MULTIPLE_ANSWERS), correct_option_id=get(CORRECT_OPTION_ID), explanation=get(EXPLANATION), explanation_parse_mode=get(EXPLANATION_PARSE_MODE), explanation_entities=get(EXPLANATION_ENTITIES), open_period=get(OPEN_PERIOD), close_date=get(CLOSE_DATE), is_closed=get(IS_CLOSED), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOWS_MULTIPLE_ANSWERS), reply_markup=get(REPLY_MARKUP))

    elif type == DICE:

        response = bot.send_dice(chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID), emoji=get(EMOJI), disable_notification=get(DISABLE_NOTIFICATION), protect_content=get(PROTECT_CONTENT), reply_to_message_id=get(REPLY_TO_MESSAGE_ID), allow_sending_without_reply=get(ALLOW_SENDING_WITHOUT_REPLY), reply_markup=get(REPLY_MARKUP))

    elif type == ACTION:

        action = get(ACTION)

        if action == "":
            print(action_error)
            exit(1)

        response = bot.send_chataction(action=action, chat_id=get(CHAT_ID), message_thread_id=get(MESSAGE_THREAD_ID))

    elif type == EXCEPTION:

        response = bot.send_exception(text=get(EXCEPTION), chat_id=get(CHAT_ID))

    else:
        print(command_error)
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

        if type not in SHORTCUT_COMMANDS:
            print(error)
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

> notify {HELP_1} / > notify {HELP_2}
    Prints the instructions
    You can add at the end the type of notify command you need help with
    To see the description of ALL parameters that can be used, use {PARAMETERS}

    Es: notify {HELP_1} {TEXT}
    Es: notify {HELP_2} {EDIT}
    Es: notify {HELP_1} {VOICE}

> notify {VERSION}
    See the current notify version

> notify {UPDATE_1} / > notify {UPDATE_2}
    Download the latest version of notify
    You can add at the end which type of update u prefer:
        > {PROD} (default) : uploads to the latest tested version
        > {DEV} : uploads to the latest version under development (not finished, not suggested)

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
    subprocess.run(shlex.split(f"mv notify.py python_module/"))

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

if __name__ == "__main__":
    main()
