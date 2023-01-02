import sqlite3
from kubernetes import client, config

def insert_namespaces(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  # Configs can be set in Configuration class directly or using helper utility
  config.load_kube_config()

  v1 = client.CoreV1Api()
  namespaces = v1.list_namespace(watch=False)
  namespaces_count = len(namespaces.items)

  i = 0
  while i < namespaces_count:
    namespace=namespaces.items[i].metadata.name

    c.execute("""
            INSERT INTO namespace(name)
            VALUES
            ('%s')
            """ 
            % (namespace)
            )
    i = i + 1
            
  conn.commit()

###

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