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
    print("Can not delete the file as it doesn't exists")

###

def create_tables(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  #Namespace table
  c.execute('''
          CREATE TABLE IF NOT EXISTS namespace
          ([name] TEXT PRIMARY KEY UNIQUE)
          ''')

  #Pods
  c.execute('''
          CREATE TABLE IF NOT EXISTS pods
          ([name] TEXT PRIMARY KEY UNIQUE, [namespace] TEXT)
          ''')

  conn.commit()

###

def add_namespace(db_name,namespace_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          INSERT INTO namespace(name)
          VALUES
          ('%s')
          """ 
          % (namespace_name)
          )
          
  conn.commit()

###

def list_k8s_namespace():
  # Configs can be set in Configuration class directly or using helper utility
  config.load_kube_config()

  v1 = client.CoreV1Api()
  ret = v1.list_namespace(watch=False)
  ret_count = len(ret.items)
  results = []
  i = 0
  while i < ret_count:
    result=ret.items[i].metadata.name
    results.append(result)
    i = i + 1
  return results

###

# select example

def select_namespace(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          SELECT * FROM namespace
          """
          )

  rows = c.fetchall()

  for row in rows:
      print(row)

  conn.commit()