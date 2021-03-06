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
START_MSG = os.environ.get("START_MESSAGE", "βπ­ βπͺ βπΎ {first} Κα΄α΄‘ aΠ³Ξ΅ Κα΄α΄!!<b> \nπΈπ  ππ¦π€π₯ πΈ  π¦ π© π» π¦ π³ π¨ πͺ α΄Iαͺα΄ ΥαΌα©αIαα α·OT  π \nΚα΄α΄  α΄Κα΄  Ι΄α΄α΄  α΄ΚΚα΄  α΄α΄ α΄α΄α΄ α΄α΄  α΄α΄  Κα΄α΄Κ  πΎπ£π π¦π‘ οΏ½\nπ§ βπΊ βπΉ   ππ π¦  πππ  ππππ  π₯π   ααα΄α©T α΄α΄  π\nTαΌIΥ α΄α΄α΄α΄ α΄‘α΄s ππππ£ππ ΚΚ  βπ² βπͺ \nπ΄ βπ³ βπ± βπΎ  α΄α΄Ιͺα΄α΄Κ  βπ³ βπ΄ βπΉ  α΄α΄α΄Κα΄Κ πππ</b>")
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
