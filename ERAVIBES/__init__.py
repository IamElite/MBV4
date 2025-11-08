
import time
import logging
import sys
import os
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler("log.txt", maxBytes=10485760, backupCount=5),
        logging.StreamHandler(),
    ],
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.ERROR)
logging.getLogger("ntgcalls").setLevel(logging.CRITICAL)
logging.getLogger("pymongo").setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("pytgcalls").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)


__version__ = "3.0.1"

# Add parent directory to sys.path for config import
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from config import Config

config = Config()
config.check()
tasks = []
boot = time.time()

from ERAVIBES.core.bot import Bot
app = Bot()

from ERAVIBES.core.dir import ensure_dirs
ensure_dirs()

from ERAVIBES.core.userbot import Userbot
userbot = Userbot()

from ERAVIBES.core.mongo import MongoDB
db = MongoDB()

from ERAVIBES.core.lang import Language
lang = Language()

from ERAVIBES.core.telegram import Telegram
from ERAVIBES.core.youtube import YouTube
tg = Telegram()
yt = YouTube()

from ERAVIBES.helpers import Queue
queue = Queue()

from ERAVIBES.core.calls import TgCall
era = TgCall()
