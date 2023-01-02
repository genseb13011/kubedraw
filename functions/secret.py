import sqlite3
from kubernetes import client, config

###

def insert_secrets(db_name):
   
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  # Configs can be set in Configuration class directly or using helper utility
  config.load_kube_config()

  v1 = client.CoreV1Api()
  secrets = v1.list_secret_for_all_namespaces(watch=False)
  secrets_count = len(secrets.items)
  
  i = 0
  while i < secrets_count:
    name=secrets.items[i].metadata.name
    namespace=secrets.items[i].metadata.namespace
    type=secrets.items[i].type

    c.execute("""
            INSERT INTO secret(name,namespace,type)
            VALUES
            ("%s","%s","%s")
            """ 
            % (name, namespace,type)
            )
    i = i + 1
          
  conn.commit()

###

def select_secrets(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          SELECT * FROM secret
          """
          )

  rows = c.fetchall()

  for row in rows:
      print(row)

  conn.commit()