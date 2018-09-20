#!/usr/bin/python

import os
import time
import datetime
import glob
import shutil

DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = '!qazxsw@'
DB_NAME = 'test'
BACK_PATH = '/home/admin/PycharmProjects/python/log/'

current_date = time.strftime('%Y%m%d')
today_back_path = BACK_PATH + current_date

print ('delete folder three days ago')
folders = glob.glob(BACK_PATH + '*')

today = datetime.datetime.now()

for item in folders:
    try:
        foldername = os.path.split(item)[1]
        day = datetime.datetime.strftime(foldername,'%Y%m%d')
        diff = today - day
        if diff.days >=3:
            shutil.rmtree(item)
    except:
        pass
print ("createing backup folder")

if not os.path.exists(today_back_path):
    os.makedirs(today_back_path)

print ("checking for databases names files")
if os.path.exists(DB_NAME):
    file1 = open(DB_NAME)
    multi = 1
    print ("Databases file found...")
    print ("Starting backup of all dbs listed in file " + DB_NAME)
else:
    print ("Databases file not found...")
    print ("Starting backup of database " + DB_NAME)
    multi = 0

# Starting actual database backup process.
if multi:
   in_file = open(DB_NAME,"r")
   flength = len(in_file.readlines())
   in_file.close()
   p = 1
   dbfile = open(DB_NAME,"r")

   while p <= flength:
       db = dbfile.readline()   # reading database name from file
       print ("db is")
       print (db)
       db = db[:-1]         # deletes extra line
       dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_PASSWORD + " " + db + " > " + today_back_path + "/" + db + ".sql"
       os.system(dumpcmd)
       p = p + 1
   dbfile.close()
else:
   db = DB_NAME
   dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_PASSWORD + " " + db + " > " + today_back_path + "/" + db + ".sql"
   os.system(dumpcmd)

print ("Backup script completed")
print ("Your backups has been created in '" + today_back_path + "' directory")