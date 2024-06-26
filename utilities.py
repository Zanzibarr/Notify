import os

version = "notify version: 3.2"

home = os.path.expanduser('~')
std_config_path = f"{home}/.zanz_notify_profiles"
old_config_path = f"{home}/.zanz_notify_config"
base_path = os.path.dirname(os.path.abspath(__file__))
dest_path = f"{home}/.notify_zanz"
log = f"{dest_path}/log.log"

files = ["notify.py", "notify_app.py", "updater.py", "utilities.py", "update_setup.py", "change_log.md", "readme.md"]

bashrc_edit_title = "#notify - zanzi"
bashrc_edit_content = """alias notify='python3 $HOME/.notify_zanz/notify_app.py'
export PYTHONPATH=$HOME/.notify_zanz/python_module"""
bashrc_edit = f"{bashrc_edit_title}\n{bashrc_edit_content}"

HELP = "-help"
PARAMETERS = "-params"
VERSION = "-version"
UPDATE = "-update"
PROD = "-prod"
DEV = "-dev"
CONF = "-conf"
ADD = "-add"
TOKEN = "-token"
REMOVE = "-rm"
EDIT = "-edit"
SET = "-set"
SEE = "-see"
UNINSTALL = "-uninstall"
PROFILE = "-prof"
TEXT = "-t"
PHOTO = "-p"
AUDIO = "-a"
DOCUMENT = "-d"
VIDEO = "-v"
EXCEPTION = "-exc"

CHAT_ID = "-chat"
MESSAGE_THREAD_ID = "-mt_id"
PARSE_MODE = "-parse"
DISABLE_WEB_PAGE_PREVIEW = "-no_webp_preview"
DISABLE_NOTIFICATION = "-silent"
PROTECT_CONTENT = "-protect_content"
REPLY_TO_MESSAGE_ID = "-reply"
ALLOW_SENDING_WITHOUT_REPLY = "-reply_anyway"
MESSAGE_ID = "-message"
FROM_CHAT_ID = "-from"
CAPTION = "-caption"
HAS_SPOILER = "-spoiler"
DURATION = "-duration"
PERFORMER = "-performer"
TITLE = "-title"
THUMBNAIL = "-thumb_path"
DISABLE_CONTENT_TYPE_DETECTION = "-no_ctype_det"
WIDTH = "-width"
HEIGHT = "-height"
SUPPORTS_STREAMING = "-streaming"


SHORTCUT_COMMANDS = [DISABLE_WEB_PAGE_PREVIEW, DISABLE_NOTIFICATION, HAS_SPOILER, DISABLE_CONTENT_TYPE_DETECTION, ALLOW_SENDING_WITHOUT_REPLY, PROTECT_CONTENT]

explanation = {
    CHAT_ID: f"{CHAT_ID} <chat_id> : chat to send the message to.",
    MESSAGE_THREAD_ID: f"{MESSAGE_THREAD_ID} <thread_id> : Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.",
    PARSE_MODE: f"{PARSE_MODE} <parse_mode> : Mode for parsing entities in the message text/caption. See site for more details.",
    DISABLE_WEB_PAGE_PREVIEW: f"{DISABLE_WEB_PAGE_PREVIEW} : <bool> : Disables link previews for links in this message.",
    DISABLE_NOTIFICATION: f"{DISABLE_NOTIFICATION} <bool> : Sends the message silently. Users will receive a notification with no sound.",
    PROTECT_CONTENT: f"{PROTECT_CONTENT} <bool> : Protects the contents of the sent message from forwarding and saving.",
    REPLY_TO_MESSAGE_ID: f"{REPLY_TO_MESSAGE_ID} <message_id> : If the message is a reply, ID of the original message.",
    ALLOW_SENDING_WITHOUT_REPLY: f"{ALLOW_SENDING_WITHOUT_REPLY} <bool> : Pass True if the message should be sent even if the specified replied-to message is not found.",
    MESSAGE_ID: f"{MESSAGE_ID} <message_id> : the message to copy/forward.",
    FROM_CHAT_ID: f"{FROM_CHAT_ID} <chat_id> : chat_id of the message to copy/forward.",
    CAPTION: f"{CAPTION} <caption> : Caption, 0-1024 characters after entities parsing. If not specified, the original caption is kept.",
    HAS_SPOILER: f"{HAS_SPOILER} <bool> : Pass True if the file needs to be covered with a spoiler animation.",
    DURATION: f"{DURATION} <duration> : Duration in seconds.",
    PERFORMER: f"{PERFORMER} <performer> : Performer",
    TITLE: f"{TITLE} <title> : Title",
    THUMBNAIL: f"{THUMBNAIL} <thumbnail_path> : Path of the Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.",
    DISABLE_CONTENT_TYPE_DETECTION: f"{DISABLE_CONTENT_TYPE_DETECTION} <bool> : Disables automatic server-side content type detection for files uploaded using multipart/form-data",
    WIDTH: f"{WIDTH} <width> : Video/Animation width",
    HEIGHT: f"{HEIGHT} <height> : Video/Animation height",
    SUPPORTS_STREAMING: f"{SUPPORTS_STREAMING} <bool> : If the video is suitable for streaming"
}

cmd_red = '\033[91m'
cmd_yellow = '\033[93m'
cmd_green = '\033[92m'
cmd_blue = '\033[94m'

cmd_bold = '\033[1m'
cmd_underline = '\033[4m'

cmd_end = '\033[0m'

cmd_input = cmd_bold + cmd_underline
cmd_suggestion = cmd_green + cmd_bold
cmd_exception = cmd_bold+cmd_red

nerror = f"Notify error: "
suggestion = f"Use notify -help to get instructions."
command_error = f"{nerror}command not recognised."

error = f"{nerror}wrong arguments."

profile_error = f"{nerror}must specify at least the profile or the token."
add_conf_error = f"{nerror}must specify at least both name and token."
profile_name_error = f"{nerror}must specify a valid name from the profiles configuration file."
set_conf_error = f"{nerror}must specify a name."

message_error = f"{nerror}either specify a text message to send, or a file to read."
copy_error = f"{nerror}both message id and chat id must be specified."
forward_error = copy_error
photo_error = f"{nerror}specify the path to the photo to send."
audio_error = f"{nerror}specify the path to the audio to send."
doc_error = f"{nerror}specify the path to the doc to send."
video_error = f"{nerror}specify the path to the doc to send."
help_error = f"{nerror}either don't specify anything to have the full help message, or specify a notify command (not a parameter, to see the parameters description use {PARAMETERS})."

conf_file_info = f"""Configuration file: {std_config_path}"""

help_beginning = "Hi! Thanks for using notify!\n\nIf this instructions are not helping, please open an issue on github or give a look to the telegram API website (linked at the end of this message).\n\nHere's """
help_conclusion = f"""
SHORTCUTS:

- For each bool parameter, '--<param>' is equal to '-<param> true'


Base folder: {base_path}
Profiles file: {std_config_path}
Base repository: https://github.com/Zanzibarr/Notify
Telegram API explanation: https://core.telegram.org/bots/api

{version}
"""

def print_exception(message : str):
    for line in message.splitlines():
        if line != "": print(f"{cmd_exception}[ERROR]:{cmd_end} {line}")
        else: print()
    exit(1)

def print_bold(message):
    print(f"{cmd_bold}{message}{cmd_end}")

def print_info(message : str):
    for line in message.splitlines():
        if line != "": print(f"{cmd_suggestion}[INFO ]:{cmd_end} {line}")
        else: print()

def print_warning(message : str):
    for line in message.splitlines():
        if line != "": print(f"{cmd_yellow}[WARN ]:{cmd_end} {line}")
        else: print()

def print_input(message):
    return input(f"{cmd_bold}{cmd_blue}[INPUT]:{cmd_end} {message}")

def print_notify_error(message : str):
    for line in message.splitlines():
        if line != "": print(f"{cmd_exception}[ERROR]:{cmd_end} {line}")
        else: print()
    print_info(suggestion)
    exit(1)