# -*- coding: utf-8 -*-
from pymongo import MongoClient
import urllib.parse
import datetime

db_name='iot_db'
table_name='iot_table'

def constructor():
    client = pymongo.MongoClient("mongodb+srv://iot:1234qwer@cluster0-x4loq.mongodb.net/test?retryWrites=true&w=majority")
    db = client[db_name]
    coll = db[table_name]
    return coll

def test_connect(): 
    try:
        coll = constructor()
        #coll.count_documents({})
        return 0
    except InvalidSignatureError:
        return 400


