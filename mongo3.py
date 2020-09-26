#importing necessary modules
import pandas as pd
from pandas import ExcelFile
import csv
import json
from pymongo import MongoClient
import os
from bson.json_util import loads
from bson import ObjectId
import re

#path=pd.ExcelFile("Alarm.xls")#Reading excel file using pandas module
#s=path.sheet_names
#print(s)

#three functions are created for the three files
def file_watcher():
    jdf=open('Archivejson.json').read()#reading json
    data=loads(jdf)#loading data from the json file
    #print(data)
    header=["Date","BatchName","Step Description","TICR-01","TICR-02"]
    #data = csv.to_dict(orient = 'data')
    client=MongoClient('localhost',27017)
    db=client['excel2-db']
    col=db.col
    #inserting data into mongodb and removing the file using os module
    col.insert(data)
    print("done1")
    #os.remove("Archive.csv")
    os.remove("Archive(Autosaved).xls")
    print("file removed")


def xl_1():
    path=pd.ExcelFile("Alarm.xls")#Reading excel file using pandas module
    print(path)
    s=path.sheet_names
    print(s)
    if s==['Sheet2']:
        df=path.parse("Electricity Archive")#parsing excel data,parameter to this function is the sheet name
        df.to_csv("Archive.csv",encoding='utf-8')#converting to cs
        csv=pd.read_csv('Archive.csv',encoding='utf-8')#reading csv
        csv.to_json('Archivejson.json')#converting to json
        file_watcher()
        
    else:
        pass
    print(data)
    header=["Date","BatchName","Step Description","TICR-01","TICR-02"]
    data = csv.to_dict(orient = 'data')
    client=MongoClient('localhost',27017)
    db=client['excel2-db']
    col=db.col
    #inserting data into mongodb and removing the file using os module
    col.insert(data)
    print("done1")
    os.remove("Archive.csv")
    #print("file removed")
def xl_2():
    path1=pd.ExcelFile("Alarm.xls")#Reading excel file using pandas module
    s1=path1.sheet_names
    #print(s)
    df1=path1.parse("Sheet2")#parsing excel data,parameter to this function is the sheet name
    df1.to_csv("Alarm.csv",encoding='utf-8')#converting to csv
    csv1=pd.read_csv('Alarm.csv',encoding='utf-8')#reading csv
    csv1.to_json('Alarmjson.json')#converting to json
    jdf1=open('Alarmjson.json').read()#reading json
    data1=loads(jdf1)#loading data from the json file
    #header=["Date","BatchName","Step Description","TICR-01","TICR-02"]
    #data = csv.to_dict(orient = 'data')
    client1=MongoClient('localhost',27017)
    db1=client1['excel3-db']
    col1=db1.col1
    #inserting data into mongodb and removing the file using os module
    col1.insert(data1)
    print("done2")
    #os.remove("Archive.csv")
    #print("file removed")

def xl_3():
    path2=pd.ExcelFile("3Hours_Batch.xls")#Reading excel file using pandas module
    s2=path2.sheet_names
    path2=pd.ExcelFile("3Hours_Batch.xls")#Reading excel file using pandas module
    df2=path2.parse("3Hours_Batch")#parsing excel data,parameter to this function is the sheet name
    df2.to_csv("3Hours_batch.csv",encoding='utf-8')#converting to csv
    csv2=pd.read_csv('3Hours_batch.csv',encoding='utf-8')#reading csv
    csv2.to_json('3Hours_batch.json')#converting to json
    jdf2=open('3Hours_batch.json').read()#reading json
    data2=loads(jdf2)#loading data from the json file
    #header=["Date","BatchName","Step Description","TICR-01","TICR-02"]
    #data = csv.to_dict(orient = 'data')
    client2=MongoClient('localhost',27017)
    db2=client2['excel4-db']
    col2=db2.col2
    #inserting data into mongodb and removing the file using os module
    col2.insert(data2)
    print("done3")
    #os.remove("Archive.csv")
    #print("file removed")

xl_1()
xl_2()
xl_3()
