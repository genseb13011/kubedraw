import sqlite3
import os
from kubernetes import client, config

###

def create_db(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

###

def delete_db(db_name):
  if os.path.exists(db_name):
    os.remove(db_name)
  else:
    print("%s cannot be delete because it doesn't exists" % (db_name))

###

def create_table(db_name,create_request):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  #Namespace table
  c.execute(create_request)

  conn.commit()

###