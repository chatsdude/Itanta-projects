from pymongo import MongoClient
import csv
import pandas as pd
import os
import json
from bson.json_util import loads

os.chdir('E:\\file watch')
csv=pd.read_csv('DOWNTIME.csv',encoding='utf-8')#reading csv
csv.to_json('DOWNTIMEjson.json')#converting to json
jdf=open('DOWNTIMEjson.json').read()#reading json
data=loads(jdf)#loading data from the json file
    #header=["Date","BatchName","Step Description","TICR-01","TICR-02"]
    #data = csv.to_dict(orient = 'data')
client1=MongoClient('localhost',27017)
db1=client1['cssv-db']
col1=db1.col1
    #inserting data into mongodb and removing the file using os module
col1.insert(data)
print('done')
