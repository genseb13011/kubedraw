import sqlite3
from kubernetes import client, config

###

def insert_persistentvolumes(db_name):
   
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  # Configs can be set in Configuration class directly or using helper utility
  config.load_incluster_config()

  v1 = client.CoreV1Api()
  persistentvolumes = v1.list_persistent_volume(watch=False)
  persistentvolumes_count = len(persistentvolumes.items)
  
  i = 0
  while i < persistentvolumes_count:
    name=persistentvolumes.items[i].metadata.name
    storageclassname=persistentvolumes.items[i].metadata.storageClassName

    c.execute("""
            INSERT INTO persistentvolume(name,storageclassname)
            VALUES
            ("%s","%s")
            """ 
            % (name,storageclassname)
            )
    i = i + 1
          
  conn.commit()

###

def select_persistentvolumes(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          SELECT * FROM persistentvolume
          """
          )

  rows = c.fetchall()

  for row in rows:
      print(row)

  conn.commit()