import pymongo
import pandas as pd
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client["mydatabase2"]
print (db)
collection = db["mycollection"]
print (collection)
one_record = collection. find_one
print (one_record)
all_records = collection.find()
print (all_records)
all_records = collection.find()
print (all_records)
all_records =collection.find()
print (all_records)
list_cursor = list (all_records)
print(list_cursor)
df = pd.DataFrame(list_cursor)
df.head()
