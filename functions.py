import sqlite3
import os

def create_db(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

def delete_db(db_name):
  if os.path.exists(db_name):
    os.remove(db_name)
  else:
    print("Can not delete the file as it doesn't exists")

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
          ([id] INTEGER PRIMARY KEY, [name] TEXT UNIQUE)
          ''')
          
  #Pods
  c.execute('''
          CREATE TABLE IF NOT EXISTS pods
          ([id] INTEGER PRIMARY KEY, [name] TEXT UNIQUE, [namespace_id] INTEGER)
          ''')

  conn.commit()


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





def show_tables(db_name):
  conn = sqlite3.connect(db_name) 
  c = conn.cursor()

  c.execute('''
          SELECT name FROM sqlite_schema
          WHERE type='table'
          ORDER BY name;
          ''')

  rows = c.fetchall()

  for row in rows:
    print(row)

          
  conn.commit()
