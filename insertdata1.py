from pymongo import MongoClient
from dotenv import load_dotenv
import os 
load_dotenv()
username=os.getenv("user")
password=os.getenv("password")

client=MongoClient(f"mongodb+srv://{username}:{password}@awslambdademo.tzxoalb.mongodb.net/?retryWrites=true&w=majority&appName=AWSLambdaDemo")
db=client["sample"]
connection=db["SampleConnection"]
document={"name":"javeed","address":"india"}
connection.insert_one(document)
client.close()
