import sqlite3
from kubernetes import client, config

###

def insert_ingressclass(db_name):
   
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  # Configs can be set in Configuration class directly or using helper utility
  config.load_kube_config()

  v1 = client.NetworkingV1Api()
  ingressclass = v1.list_ingress_class(watch=False)
  ingressclass_count = len(ingressclass.items)
  
  i = 0
  while i < ingressclass_count:
    name=ingressclass.items[i].metadata.name

    c.execute("""
            INSERT INTO ingressclass(name)
            VALUES
            ("%s")
            """ 
            % (name)
            )
    i = i + 1
          
  conn.commit()

###

def select_ingressclass(db_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          SELECT * FROM ingressclass
          """
          )

  rows = c.fetchall()

  for row in rows:
      print(row)

  conn.commit()