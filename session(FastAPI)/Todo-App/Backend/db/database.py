from pymongo.mongo_client import MongoClient
import urllib.parse

# Encode username and password
username = urllib.parse.quote_plus("sami606713")
password = urllib.parse.quote_plus("$@m!u11@h")

uri = f"mongodb+srv://{username}:{password}@cluster0.pawnz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Connect to thse database
db = client['Todo-App']

# Connect to the collection
collection = db['todos']

# collection for users
user_collection = db['users']
