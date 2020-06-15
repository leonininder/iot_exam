# -*- coding: utf-8 -*-
from pymongo import MongoClient
import urllib.parse
import datetime

#db_name='Leon_test'
#table_name='mydb'

def constructor():
    #client = MongoClient("mongodb+srv://iot:1234qwer@cluster0-x4loq.mongodb.net/test")
    
    client = pymongo.MongoClient("mongodb+srv://iot:<password>@cluster0-x4loq.mongodb.net/<dbname>?retryWrites=true&w=majority")
    db = client.test

    #db = client[db_name]
    return db
   
#----------------------------儲存使用者的股票--------------------------
#def write_user_stock_fountion(stock, bs, price):  
#    db=constructor()
#    collect = db[table_name]
#    collect.insert({"stock": stock,
#                    "data": 'care_stock',
#                    "bs": bs,
#                    "price": float(price),
#                    "date_info": datetime.datetime.utcnow()
#                    })

##def write_user_stock_fountion(stock):  
#    db=constructor()
#    collect = db[table_name]
#    collect.insert({"stock": stock,
#                    "date_info": datetime.datetime.utcnow()
#                    })

#----------------------------殺掉使用者的股票--------------------------
#def delete_user_stock_fountion(stock):  
#    db=constructor()
#    collect = db[table_name]
#    collect.remove({"stock": stock})
    
##----------------------------秀出使用者的股票--------------------------
#def show_user_stock_fountion():  
#    db=constructor()
#    collect = db[table_name]
#    #cel=list(collect.find({"data": 'care_stock'}))
#    cel=list(collect.find())
#    return cel

def write_temp_humi(temp, humi): 
    db=constructor()
    collect = db[table_name]
    collect.update_one({ "temp": temp, "humi": humi})

def read_temp_humi(temp, humi): 
    db=constructor()
    #collect = db[table_name]
    #collect.update_one({ "temp": temp, "humi": humi})
    #cel = list(collect.find({"data": 'care_stock'}))
    return list(db.products.findOne())

