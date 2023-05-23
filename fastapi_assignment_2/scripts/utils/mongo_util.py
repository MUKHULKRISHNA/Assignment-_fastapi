from pymongo import MongoClient
from scripts.constants.app_constants import Mongo

clientMongo = MongoClient(Mongo.mongo_db)
mydb = clientMongo.interns_b2_23
student_Q = mydb.MUKHUL_KRISHNA
