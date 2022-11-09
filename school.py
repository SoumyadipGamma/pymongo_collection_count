import pymongo
import pandas as pd
from pymongo import MongoClient
client = MongoClient('mongodb://gamma:gamma231@gamman2.cluster.kol:27015')
db = client["school"]
print (db)
collection = db["student_fee"]
print (collection)
one_record = collection. find_one
print (one_record)
all_records = collection.find()
print (all_records)
all_records =collection.find()
print (all_records)
list_cursor = list (all_records)
print(list_cursor)
df = pd.DataFrame(list_cursor)
df.head()
df.tail()

