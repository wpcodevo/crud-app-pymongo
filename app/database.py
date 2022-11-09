from pymongo import mongo_client, ASCENDING
from app.config import settings

client = mongo_client.MongoClient(settings.DATABASE_URL)
print('🚀 Connected to MongoDB...')

db = client[settings.MONGO_INITDB_DATABASE]
Note = db.notes
Note.create_index([("title", ASCENDING)], unique=True)
