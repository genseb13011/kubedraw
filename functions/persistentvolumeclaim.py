import sqlite3
from kubernetes import client, config

###

def insert_persistentvolumeclaims(db_name):
   
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  # Configs can be set in Configuration class directly or using helper utility
  config.load_incluster_config()

  v1 = client.CoreV1Api()
  persistentvolumeclaims = v1.list_persistent_volume(watch=False)
  persistentvolumeclaims_count = len(persistentvolumeclaims.items)
  
  i = 0
  while i < persistentvolumeclaims_count:
    name=persistentvolumeclaims.items[i].metadata.name

    c.execute("""
            INSERT INTO persistentvolumeclaim(name)
            VALUES
            ("%s")
            """ 
            % (name)
            )
    i = i + 1
          
  conn.commit()

###

def select_persistentvolumeclaims(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          SELECT * FROM persistentvolumeclaim
          """
          )

  rows = c.fetchall()

  for row in rows:
      print(row)

  conn.commit()