# Don't Remove Credit @teamrxs
# Follow Github For More Project BINOD-XD
# Ask Doubt on telegram @mrboombastic4


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21895677")

API_HASH = os.environ.get("API_HASH", "8c5255f020234293f7184ddb5c4402bf")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6870571887:AAF6iNfd9lZNdiZ6BNd33rpruby8vsiMuHo") 

FORCE_SUB = os.environ.get("FORCE_SUB", "teamrxs") 

             # Don't Remove Credit @teamrxs
             # Follow Github For More Project BINOD-XD
             # Ask Doubt on telegram @mrboombastic4

DB_NAME = os.environ.get("DB_NAME", "teamrxs")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://teamrxs:shanto27@cluster0.qcltlqe.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/Welcome-To-The-Bot-12-26")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1945035762').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @teamrxs
# Follow Github For More Project BINOD-XD
# Ask Doubt on telegram @mrboombastic4
