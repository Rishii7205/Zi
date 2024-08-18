import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "28418579")) #optional
API_HASH = getenv("API_HASH", "18f478e57266f63fe00a3a975d66428e") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5605223316").split()))
OWNER_ID = int(getenv("OWNER_ID"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "6775324227:AAF5uXJ2p2hSq3jVypMxfqCIWRiDX1TpEqU")
ALIVE_PIC = getenv("ALIVE_PIC", 'https://telegra.ph/file/3c52a01057865f7511168.jpg')
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/rishii7205/Zi")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQGxohMANQI0FoWVY6Apc8ly0mqpF0oDshSwWdbL1UpOcUy7DVKb1ODborMsLmu-9b301R8UT5NtAJobMi4Kbo6TjjDvyuE3BinGHzqW3bEESg-QB8xo-FZ17GTPy-mVkgNEkwgUcWLmRbidH6BU0LcVwM_1CBzSZn1PSh946Nk03MVp8qozYuqAI7nHnigY9mHbZ110I24tRCPuIU_4BAnHNrH8bIahdTJ053SI53vydNPxqW1d9bBN79VPV-1UoHn3Z5l9-CK-MAqFyMY7hFRB7RyOrzTZZepqjwv3xSQLGGRuDT6LBkU5b4wqDehuvp4CRnVYIfN-xMcS3Y6ZxZVf9NLy8AAAAAFiXTd4AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
