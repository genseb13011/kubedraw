import sqlite3
from kubernetes import client, config

###

def insert_pods(db_name):
   
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  # Configs can be set in Configuration class directly or using helper utility
  config.load_incluster_config()

  v1 = client.CoreV1Api()
  pods = v1.list_pod_for_all_namespaces(watch=False)
  pods_count = len(pods.items)
  
  i = 0
  while i < pods_count:
    name=pods.items[i].metadata.name
    namespace=pods.items[i].metadata.namespace

    c.execute("""
            INSERT INTO pod(name,namespace)
            VALUES
            ("%s","%s")
            """ 
            % (name, namespace)
            )
    i = i + 1
          
  conn.commit()
