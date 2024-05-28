from pymongo import MongoClient
from dotenv import load_dotenv
import os 
load_dotenv()
username=os.getenv("user")
password=os.getenv("password")
try:
    client=MongoClient(f"mongodb+srv://{username}:{password}@awslambdademo.tzxoalb.mongodb.net/?retryWrites=true&w=majority&appName=AWSLambdaDemo")
    db=client["sample"]
    connection=db["sampleconnection"]
    document=[{"name":"ram",
               "address":"delhi"},
              {"name":"rakesh",
               "address":"hyd"}]
    inserted_doc=connection.insert_many(document)
    print("Data inserted successfully")
except Exception as e:
    print(e)


