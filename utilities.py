import os

version = "notify version: 2.0.1"

home = os.path.expanduser('~')
std_config_path = f"{home}/.zanz_notify_profiles"
old_config_path = f"{home}/.zanz_notify_config"
base_path = os.path.dirname(os.path.abspath(__file__))
dest_path = f"{home}/.notify_zanz"
log = f"{dest_path}/log.log"

files = ["notify.py", "notify_app.py", "updater.py", "utilities.py", "update_setup.py"]

bashrc_edit_title = "#notify - zanzi"
bashrc_edit_content = """alias notify='python3 $HOME/.notify_zanz/notify_app.py'
export PYTHONPATH=$HOME/.notify_zanz/python_module"""
bashrc_edit = f"{bashrc_edit_title}\n{bashrc_edit_content}"

HELP = "-help"
PARAMETERS = "-param"
VERSION = "-version"
UPDATE = "-update"
PROD = "-prod"
DEV = "-dev"
CONF = "-conf"
ADD = "-add"
TOKEN = "-token"
REMOVE = "-rm"
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
help_error = f"\n{nerror}either don't specify anything to have the full help message, or specify a notify command (not a parameter,t o see the parameters description use {PARAMETERS})."

conf_file_info = f"""
Configuration file: {std_config_path}"""

help_beginning = "Hi! Thanks for using notify!\n\nIf this instructions are not helping, please open an issue on github or give a look to the telegram API website (linked at the end of this message).\n\nHere's """
help_conclusion = f"""
SHORTCUTS:

- For each bool parameter, '--<param>' is equal to '-<param> true'


Base folder: {base_path}
Profiles file: {std_config_path}
Base repository: https://github.com/Zanzibarr/Telegram_Python_Notifier
Telegram API explanation: https://core.telegram.org/bots/api

{version}
"""

def ntf_print(text:str, on_file = False):
    if on_file:
        with open(log, "a") as f:
            f.write(f"\n{text}")
    else:
        print(text)