# Don't Remove Credit @teamrxs
# Follow Github For More Project BINOD-XD
# Ask Doubt on telegram @mrboombastic4


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "")

API_HASH = os.environ.get("API_HASH", "")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

FORCE_SUB = os.environ.get("FORCE_SUB", "VJ_Botz") 

             # Don't Remove Credit @teamrxs
             # Follow Github For More Project BINOD-XD
             # Ask Doubt on telegram @mrboombastic4

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/Welcome-To-The-Bot-12-26")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @teamrxs
# Follow Github For More Project BINOD-XD
# Ask Doubt on telegram @mrboombastic4