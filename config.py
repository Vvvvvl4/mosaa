## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AQAGlVnL8jcgAK9OUC7IncKFmPCc9x96fra4gxUQCsHSR3EGwP5xP_h1-8yFIGnp05A074c6u7YNiwbjpF_lFqVyPGe076MfvSsoiRr6AX-Cq-Z1lRVzpAsdm2Zeh3Yjda4vNUsO63ErxNCHI573_AkMvemFrzSSWIFMBoxmiMoFOVaDkfp2L8u8dSvablPitTEBQu6R9d34PVZzIc5WQCAb-APk0re1SSIV8cX5Pnu3az49nJXWUiVyXJz-1o0CIRui7Cq1rtvhSjHsfhrWfz4BynvX11TejUqjAW7Xkwt69QCmen-iyN2U0XZbCOZhbCinKRmLnYiyJDfMz0RHkpiuAAAAATSeKvoA")
BOT_TOKEN = getenv("BOT_TOKEN", "5449317523:AAEBc0cJLOxnabCmaUqIoAiftzlRvoL1gzA")
BOT_NAME = getenv("BOT_NAME", "MUSIC RANI")
API_ID = int(getenv("API_ID", "12652905"))
API_HASH = getenv("API_HASH", "5d08ee6bc8284efcd6eeda4e8e5e5394")
OWNER_NAME = getenv("OWNER_NAME", "RANI")
OWNER_USERNAME = getenv("OWNER_USERNAME", "@UIIII4")
ALIVE_NAME = getenv("ALIVE_NAME", "RANI")
BOT_USERNAME = getenv("BOT_USERNAME", "Music0_1bot")
OWNER_ID = getenv("OWNER_ID", "5177748218")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "@RETA_VV")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "RRNN44")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "G6_9R")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
