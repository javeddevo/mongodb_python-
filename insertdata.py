from pymongo import MongoClient
from dotenv import load_dotenv
import os 
load_dotenv()
username=os.getenv("user")
password=os.getenv("password")

client=MongoClient(f"mongodb+srv://{username}:{password}@awslambdademo.tzxoalb.mongodb.net/?retryWrites=true&w=majority&appName=AWSLambdaDemo")
db = client['mydatabase']
collection = db['mycollection']

document = {"name": "sun", "city": "universe"}
inserted_document = collection.insert_one(document)

print(f"Inserted Document ID: {inserted_document.inserted_id}")
client.close()