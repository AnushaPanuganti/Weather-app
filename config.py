
import urllib.parse

DB_NAME="weatherpapp"
DB_USERNAME="anushasweety17"
DB_PASSWORD="Panuganti"

DB_CONNECTION_STRING = f"mongodb+srv://{urllib.parse.quote(DB_USERNAME)}:{urllib.parse.quote(DB_PASSWORD)}@cluster0.fdnorpi.mongodb.net/?retryWrites=true&w=majority"
NOTES_CHARACTER_LIMIT = 250

from pymongo import MongoClient
client = MongoClient(DB_CONNECTION_STRING)
db = client[DB_NAME]
print("connection established")
user = db.users.find_one({"username": "root", "password":"root"})
if not user:
        
    res = db.users.insert_one({"username": "root", "password":"root"})
    print("user created: ", res)

else:
    print("root user already exists", user)