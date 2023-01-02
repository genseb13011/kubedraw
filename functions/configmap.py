import sqlite3
from kubernetes import client, config

###

def insert_configmaps(db_name):
   
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  # Configs can be set in Configuration class directly or using helper utility
  config.load_kube_config()

  v1 = client.CoreV1Api()
  configmaps = v1.list_pod_for_all_namespaces(watch=False)
  configmaps_count = len(configmaps.items)
  
  i = 0
  while i < configmaps_count:
    name=configmaps.items[i].metadata.name
    namespace=configmaps.items[i].metadata.namespace

    c.execute("""
            INSERT INTO configmap(name,namespace)
            VALUES
            ("%s","%s")
            """ 
            % (name, namespace)
            )
    i = i + 1
          
  conn.commit()

###

def select_configmaps(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          SELECT * FROM configmap
          """
          )

  rows = c.fetchall()

  for row in rows:
      print(row)

  conn.commit()