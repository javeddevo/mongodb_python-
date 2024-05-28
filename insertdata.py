from pymongo import MongoClient

client = MongoClient("mongodb+srv://javed:mongo@awslambdademo.tzxoalb.mongodb.net/?retryWrites=true&w=majority&appName=AWSLambdaDemo")


db = client['mydatabase']
collection = db['mycollection']

document = {"name": "sun", "city": "universe"}
inserted_document = collection.insert_one(document)

print(f"Inserted Document ID: {inserted_document.inserted_id}")
client.close()