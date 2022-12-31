import sqlite3
from kubernetes import client, config

def add_namespace(db_name,namespace_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          INSERT INTO namespace(name)
          VALUES
          ('%s')
          """ 
          % (namespace_name)
          )
          
  conn.commit()

###

def list_k8s_namespaces():
  # Configs can be set in Configuration class directly or using helper utility
  config.load_kube_config()

  v1 = client.CoreV1Api()
  ret = v1.list_namespace(watch=False)
  ret_count = len(ret.items)
  namespaces = []
  i = 0
  while i < ret_count:
    namespace=ret.items[i].metadata.name
    namespaces.append(namespace)
    i = i + 1
  return namespaces

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