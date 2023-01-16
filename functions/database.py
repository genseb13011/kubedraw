import sqlite3
import os

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

def create_table(db_name,table_name,columns):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  #Namespace table
  c.execute("""
  CREATE TABLE IF NOT EXISTS %s (%s)
  """
  %
  (table_name,columns)
  )

  conn.commit()

###

def db_select(db_name,table_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          SELECT * FROM %s
          """
          % (table_name)
          )

  rows = c.fetchall()

  for row in rows:
      print(row)

  conn.commit()