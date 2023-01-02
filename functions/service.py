import sqlite3
from kubernetes import client, config

###

def add_service(db_name):
   
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  # Configs can be set in Configuration class directly or using helper utility
  config.load_kube_config()

  v1 = client.CoreV1Api()
  services = v1.list_service_for_all_namespaces(watch=False)
  services_count = len(services.items)
  
  i = 0
  while i < service_count:
    name=services.items[i].metadata.name
    namespace=services.items[i].metadata.namespace

    c.execute("""
            INSERT INTO service(name,namespace)
            VALUES
            ('%s','%s')
            """ 
            % (name, namespace)
            )
    i = i + 1
          
  conn.commit()

###

def select_service(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          SELECT * FROM service
          """
          )

  rows = c.fetchall()

  for row in rows:
      print(row)

  conn.commit()