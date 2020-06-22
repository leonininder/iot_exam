# -*- coding: utf-8 -*-
from pymongo import MongoClient
import pymongo
import urllib.parse
import datetime

db_name='Leon_test'
table_name='iot_table'

def constructor():
    client = MongoClient("mongodb://leon:qqqq1111@cluster0-shard-00-00-w1qgj.mongodb.net:27017,cluster0-shard-00-01-w1qgj.mongodb.net:27017,cluster0-shard-00-02-w1qgj.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client[db_name]
    coll = db[table_name]
    return coll

def test_connect(): 
    try:
        coll = constructor()
        #cel=list(collect.find())
        #
        return coll.count_documents({})
    except InvalidSignatureError:
        return 400


