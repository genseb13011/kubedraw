import sqlite3
from kubernetes import client, config

###

def insert_storageclass(db_name):
   
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  # Configs can be set in Configuration class directly or using helper utility
  config.load_incluster_config()

  v1 = client.StorageV1Api()
  storageclasses = v1.list_storage_class(watch=False)
  storageclasses_count = len(storageclasses.items)
  
  i = 0
  while i < storageclasses_count:
    name=storageclasses.items[i].metadata.name

    c.execute("""
            INSERT INTO storageclass(name)
            VALUES
            ("%s")
            """ 
            % (name)
            )
    i = i + 1
          
  conn.commit()

###

def select_storageclasses(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          SELECT * FROM storageclass
          """
          )

  rows = c.fetchall()

  for row in rows:
      print(row)

  conn.commit()