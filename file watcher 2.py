import csv
import os
import pandas as pd
import json
import codecs
from pymongo import MongoClient
import time
import shutil
import glob
import time
os.chdir('E:\\Data')
#os.chmod('REP0.txt',stat.S_IREAD )
#txt="REP0.txt"
#csv1="mycsv.csv"
#source='E:\Data'
#dest='E:\file watch'
#target = os.path.join(dest, os.path.dirname(source))
fields=['DATE','WIZ1','WIZ2','WIZ3']
#file=open('REP0.txt','r')
client=MongoClient('localhost',27017)
db=client['file7-db']
file6= db.file6
#file1=db1.file1
#file2=db2.file2
        
def transfer_file():
    os.chdir("E://Data")
    path=('/Data/*.txt')
    #dest=("E:\\file watch")
    files=glob.glob(path)
    print(files)
    l=len(files)
    print(l)
    if l!=0:
        while l!=0:
            try:
                for name in files:
                    #print("===================================\n\n\n", name)
                    with open(name,newline='') as f:
                        reader = csv.DictReader( (line.replace('\0','') for line in f),delimiter=';')
                        for r in reader:
                            d=dict(r)
                            print(d)
                            #del d['']
                            d['filename']=name
                            #doc={'name':name,'contents':d}
                            file6.insert(d)
                            print('done')
                            
                        
                        #print('done')
                        time.sleep(2)

                    
                    '''with open(name,'r') as f:
                        line=f.readline()
                        cnt=1
                        while line:
                            line=f.readline()
                            new_line = ""
                            #print('done')
                            for element in line:
                                if not element == "\n":
                                    new_line += element

                            line = new_line
                            #doc={"File":name,"Contents":line}
                            if not (line == "\x00" or line == ""):
                                doc={"File":name,"Contents":line}
                                file2.insert(doc)
                        f.close()'''

                    #print("File Path: ", os.path.abspath(name))
                    #os.remove(os.path.abspath(name))
                    #print('done1')
                    l=l-1
                    print(l)
                    time.sleep(2)
            except:
                print('reading')
                l=len(files)
                continue
    else:
        print('no files')
while(1):
    transfer_file()
