import sqlite3
from kubernetes import client, config

###

def insert_ingress(db_name):
   
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  # Configs can be set in Configuration class directly or using helper utility
  config.load_kube_config()

  v1 = client.NetworkingV1Api()
  ingress = v1.list_ingress_for_all_namespaces(watch=False)
  ingress_count = len(ingress.items)
  
  i = 0
  while i < ingress_count:
    name=ingress.items[i].metadata.name
    namespace=ingress.items[i].metadata.namespace

    c.execute("""
            INSERT INTO ingress(name,namespace)
            VALUES
            ("%s","%s")
            """ 
            % (name, namespace)
            )
    i = i + 1
          
  conn.commit()

###

def select_ingress(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          SELECT * FROM ingress
          """
          )

  rows = c.fetchall()

  for row in rows:
      print(row)

  conn.commit()