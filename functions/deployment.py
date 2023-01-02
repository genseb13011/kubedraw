import sqlite3
from kubernetes import client, config

###

def insert_deployments(db_name):
   
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  # Configs can be set in Configuration class directly or using helper utility
  config.load_kube_config()

  v1 = client.CoreV1Api()
  deployments = v1.list_deployment_for_all_namespaces(watch=False)
  deployments_count = len(deployments.items)
  
  i = 0
  while i < deployments_count:
    name=deployments.items[i].metadata.name
    namespace=deployments.items[i].metadata.namespace

    c.execute("""
            INSERT INTO pod(name,namespace)
            VALUES
            ("%s","%s")
            """ 
            % (name, namespace)
            )
    i = i + 1
          
  conn.commit()

###

def select_deployments(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          SELECT * FROM pod
          """
          )

  rows = c.fetchall()

  for row in rows:
      print(row)

  conn.commit()