import os

version = "notify version: 1.9.0"

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

HELP = ["-help", "-h"]
PARAMETERS = ["-param"]
VERSION = ["-version"]
UPDATE = ["-update", "-u"]
PROD = ["-prod"]
DEV = ["-dev"]
CONF = ["-conf", "-c"]
ADD = ["-add"]
TOKEN = ["-token"]
REMOVE = ["-rm"]
SET = ["-set"]
SEE = ["-see"]
UNINSTALL = ["-uninstall"]
PROFILE = ["-prof"]
TEXT = ["-t"]
COPY = ["-cpy"]
FORWARD = ["-frw"]
PHOTO = ["-p"]
AUDIO = ["-a"]
DOCUMENT = ["-d"]
VIDEO = ["-v"]
VOICE = ["-voice"]
ANIMATION = ["-anim"]
VIDEONOTE = ["-vnote"]
LOCATION = ["-loc"]
VENUE = ["-ven"]
CONTACT = ["-cnt"]
POLL = ["-pll"]
DICE = ["-dice"]
ACTION = ["-act"]
EXCEPTION = ["-exc"]
CHAT_ID = ["-chat"]
MESSAGE_THREAD_ID = ["-mt_id"]
REPLY_TO_MESSAGE_ID = ["-reply"]
MESSAGE_ID = ["-message"]
FROM_CHAT_ID = ["-from"]
INLINE_MESSAGE_ID = ["-inline_id"]
ENTITIES = ["-entities"]
CAPTION = ["-caption"]
CAPTION_ENTITIES = ["-caption_entities"]
PARSE_MODE = ["-parse"]
REPLY_MARKUP = ["-reply_markup"]
DURATION = ["-duration"]
LENGTH = ["-length"]
PERFORMER = ["-performer"]
TITLE = ["-title"]
THUMBNAIL = ["-thumb_path"]
WIDTH = ["-width"]
HEIGHT = ["-height"]
LATITUDE = ["-lat"]
LONGITUDE = ["-lon"]
HORIZONTAL_ACCURACY = ["-accuracy"]
LIVE_PERIOD = ["-live_period"]
HEADING = ["-heading"]
PROXIMITY_ALERT_RADIUS = ["-alert_radius"]
ADDRESS = ["-address"]
FOURSQUARE_ID = ["-foursquare_id"]
FOURSQUARE_TYPE = ["-foursquare_type"]
GOOGLE_PLACE_ID = "-google_place_id"
GOOGLE_PLACE_TYPE = ["-google_place_type"]
PHONE_NUMBER = ["-number"]
FIRST_NAME = ["-name"]
LAST_NAME = ["-surname"]
VCARD = ["-vcard"]
QUESTION = ["-question"]
OPTIONS = ["-options"]
TYPE = ["-type"]
CORRECT_OPTION_ID = ["-correct"]
EXPLANATION = ["-explanation"]
EXPLANATION_PARSE_MODE = ["-exp_parse"]
EXPLANATION_ENTITIES = ["-exp_entities"]
OPEN_PERIOD = ["-period"]
CLOSE_DATE = ["-close_date"]
EMOJI = ["-emoji"]
DISABLE_WEB_PAGE_PREVIEW = ["-no_webp_preview"]
DISABLE_NOTIFICATION = ["-silent"]
PROTECT_CONTENT = ["-protect_content"]
ALLOW_SENDING_WITHOUT_REPLY = ["-reply_anyway"]
HAS_SPOILER = ["-spoiler"]
DISABLE_CONTENT_TYPE_DETECTION = ["-no_ctype_det"]
SUPPORTS_STREAMING = ["-streaming"]
IS_ANONYMOUS = ["-anon"]
ALLOWS_MULTIPLE_ANSWERS = ["-multiple"]
IS_CLOSED = ["-is_closed"]
EDIT = ["-edit"]

SHORTCUT_COMMANDS = DISABLE_WEB_PAGE_PREVIEW + DISABLE_NOTIFICATION + HAS_SPOILER + DISABLE_CONTENT_TYPE_DETECTION + SUPPORTS_STREAMING + IS_ANONYMOUS + ALLOWS_MULTIPLE_ANSWERS + ALLOW_SENDING_WITHOUT_REPLY + IS_CLOSED + PROTECT_CONTENT

def tostr(lst):
    return "|".join(lst)

explanation = {
    tostr(CHAT_ID) : f"{tostr(CHAT_ID)} <chat_id> : chat to send the message to.",
    tostr(MESSAGE_THREAD_ID) : f"{tostr(MESSAGE_THREAD_ID)} <thread_id> : Unique identifier for the target message thread (topic) of the forum; for forum supergroups only.",
    tostr(PARSE_MODE) : f"{tostr(PARSE_MODE)} <parse_mode> : Mode for parsing entities in the message text/caption. See site for more details.",
    tostr(ENTITIES) : f"{tostr(ENTITIES)} <TODO> : TODO",
    tostr(DISABLE_WEB_PAGE_PREVIEW) : f"{tostr(DISABLE_WEB_PAGE_PREVIEW)} : <bool> : Disables link previews for links in this message.",
    tostr(DISABLE_NOTIFICATION) : f"{tostr(DISABLE_NOTIFICATION)} <bool> : Sends the message silently. Users will receive a notification with no sound.",
    tostr(PROTECT_CONTENT) : f"{tostr(PROTECT_CONTENT)} <bool> : Protects the contents of the sent message from forwarding and saving.",
    tostr(REPLY_TO_MESSAGE_ID) : f"{tostr(REPLY_TO_MESSAGE_ID)} <message_id> : If the message is a reply, ID of the original message.",
    tostr(ALLOW_SENDING_WITHOUT_REPLY) : f"{tostr(ALLOW_SENDING_WITHOUT_REPLY)} <bool> : Pass True if the message should be sent even if the specified replied-to message is not found.",
    tostr(REPLY_MARKUP) : f"{tostr(REPLY_MARKUP)} <TODO> : TODO",
    tostr(MESSAGE_ID) : f"{tostr(MESSAGE_ID)} <message_id> : the message to copy/forward.",
    tostr(FROM_CHAT_ID) : f"{tostr(FROM_CHAT_ID)} <chat_id> : chat_id of the message to copy/forward.",
    tostr(CAPTION) : f"{tostr(CAPTION)} <caption> : Caption, 0-1024 characters after entities parsing. If not specified, the original caption is kept.",
    tostr(CAPTION_ENTITIES) : f"{tostr(CAPTION_ENTITIES)} <TODO> : TODO",
    tostr(HAS_SPOILER) : f"{tostr(HAS_SPOILER)} <bool> : Pass True if the file needs to be covered with a spoiler animation.",
    tostr(DURATION) : f"{tostr(DURATION)} <duration> : Duration in seconds.",
    tostr(PERFORMER) : f"{tostr(PERFORMER)} <performer> : Performer",
    tostr(TITLE) : f"{tostr(TITLE)} <title> : Title",
    tostr(THUMBNAIL) : f"{tostr(THUMBNAIL)} <thumbnail_path> : Path of the Thumbnail of the file sent; can be ignored if thumbnail generation for the file is supported server-side. The thumbnail should be in JPEG format and less than 200 kB in size. A thumbnail's width and height should not exceed 320.",
    tostr(DISABLE_CONTENT_TYPE_DETECTION) : f"{tostr(DISABLE_CONTENT_TYPE_DETECTION)} <bool> : Disables automatic server-side content type detection for files uploaded using multipart/form-data",
    tostr(WIDTH) : f"{tostr(WIDTH)} <width> : Video/Animation width",
    tostr(HEIGHT) : f"{tostr(HEIGHT)} <height> : Video/Animation height",
    tostr(SUPPORTS_STREAMING) : f"{tostr(SUPPORTS_STREAMING)} <bool> : Pass True if the uploaded video is suitable for streaming",
    tostr(LENGTH) : f"{tostr(LENGTH)} <length> : Length of the video note.",
    tostr(LATITUDE) : f"{tostr(LATITUDE)} <latitude> : Latitude.",
    tostr(LONGITUDE) : f"{tostr(LONGITUDE)} <longitude> : Longitude.",
    tostr(HORIZONTAL_ACCURACY) : f"{tostr(HORIZONTAL_ACCURACY)} <horizontal_accuracy> : The radius of uncertainty for the location, measured in meters; 0-1500.",
    tostr(LIVE_PERIOD) : f"{tostr(LIVE_PERIOD)} <live_period> : Period in seconds for which the location will be updated, should be between 60 and 86400.",
    tostr(HEADING) : f"{tostr(HEADING)} <heading> : For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.",
    tostr(PROXIMITY_ALERT_RADIUS) : f"{tostr(PROXIMITY_ALERT_RADIUS)} <alert_radius> : For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.",
    tostr(ADDRESS) : f"{tostr(ADDRESS)} <address> : Address of the venue.",
    tostr(FOURSQUARE_ID) : f"{tostr(FOURSQUARE_ID)} <foursquare_id> : Foursquare identifier of the venue, if known.",
    tostr(FOURSQUARE_TYPE) : f"{tostr(FOURSQUARE_TYPE)} <foursquare_type> : Foursquare type of the venue, if known.",
    tostr(GOOGLE_PLACE_ID) : f"{tostr(GOOGLE_PLACE_ID)} <googleplace_id> : Google Places identifier of the venue.",
    tostr(GOOGLE_PLACE_TYPE) : f"{tostr(GOOGLE_PLACE_TYPE)} <googleplace_type> : Google Places type of the venue",
    tostr(PHONE_NUMBER) : f"{tostr(PHONE_NUMBER)} <phone_number> : Contact's phone number.",
    tostr(FIRST_NAME) : f"{tostr(FIRST_NAME)} <first_name> : Contact's first name.",
    tostr(LAST_NAME) : f"{tostr(LAST_NAME)} <last_name> : Contact's last name.",
    tostr(VCARD) : f"{tostr(VCARD)} <vcard> : Additional data about the contact in the form of a vCard.",
    tostr(QUESTION) : f"{tostr(QUESTION)} <question> : Poll question.",
    tostr(OPTIONS) : f"{tostr(OPTIONS)} <TODO> : TODO",
    tostr(IS_ANONYMOUS) : F"{tostr(IS_ANONYMOUS)} <bool> : True, if the poll needs to be anonymous.",
    tostr(TYPE) : f"{tostr(TYPE)} <type> : Poll type.",
    tostr(ALLOWS_MULTIPLE_ANSWERS) : f"{tostr(ALLOWS_MULTIPLE_ANSWERS)} <bool> : Allows multiple answers if True.",
    tostr(CORRECT_OPTION_ID) : f"{tostr(CORRECT_OPTION_ID)} <option_id> : ID of the correct answer for quizzes.",
    tostr(EXPLANATION) : f"{tostr(EXPLANATION)} <explanation> : Explanation for the correct answer.",
    tostr(EXPLANATION_PARSE_MODE) : f"{tostr(EXPLANATION_PARSE_MODE)} <explanation_parse_mode> : Mode for parsing entities in the explanation.",
    tostr(EXPLANATION_ENTITIES) : f"{tostr(EXPLANATION_ENTITIES)} <TODO> : TODO",
    tostr(OPEN_PERIOD) : f"{tostr(OPEN_PERIOD)} <open_period> : Time in seconds for which the poll will be active.",
    tostr(CLOSE_DATE) : f"{tostr(CLOSE_DATE)} <close_date> : UNIX timestamp for the poll's closing date.",
    tostr(IS_CLOSED) : f"{tostr(IS_CLOSED)} <bool> : Closes the poll if True.",
    tostr(EMOJI) : f"{tostr(EMOJI)} <emoji> : Emoji symbolizing the dice throw animation (see the site).",
    tostr(ACTION) : f"{tostr(ACTION)} <chat_action> : Type of action to broadcast. Choose one, depending on what the user is about to receive: typing for text messages, upload_photo for photos, record_video or upload_video for videos, record_voice or upload_voice for voice notes, upload_document for general files, choose_sticker for stickers, find_location for location data, record_video_note or upload_video_note for video notes."
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
voice_error = f"\n{nerror}either specify a voice_id/web_url or the path to the voice to send.\n{suggestion}\n"
animation_error = f"\n{nerror}either specify an animation_id/web_url or the path to the animation to send.\n{suggestion}"
videonote_error = f"\n{nerror}either specify a videonote_id/web_url or the path to the videonote to send.\n{suggestion}"
location_error = f"\n{nerror}both latitude and longitude must be specified.\n{suggestion}"
venue_error = f"\n{nerror}latitude, longitude, title and address must be specified.\n{suggestion}"
contact_error = f"\n{nerror}both phone number and name must be specified.\n{suggestion}"
poll_error = f"\n{nerror}both question and option must be specified.\n{suggestion}"
action_error = f"\n{nerror}naction must be specified.\n{suggestion}"
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

def print(text:str, on_file = False):
    if on_file:
        with open(log, "a") as f:
            f.write(f"\n{text}")
    else:
        print(text)