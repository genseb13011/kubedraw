import sqlite3
import os
from kubernetes import client, config

###

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

def add_service(db_name,service_name,namespace_name):
  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          INSERT INTO service(name,namespace)
          VALUES
          ('%s','%s')
          """ 
          % (service_name, namespace_name)
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

def list_k8s_services():
  # Configs can be set in Configuration class directly or using helper utility
  config.load_kube_config()

  v1 = client.CoreV1Api()
  ret = v1.list_service_for_all_namespaces(watch=False)
  ret_count = len(ret.items)
  services = []
  namespaces = []
  i = 0
  while i < ret_count:
    service=ret.items[i].metadata.name
    services.append(service)
    namespace=ret.items[i].metadata.namespace
    namespaces.append(namespace)
    i = i + 1
  return services, namespaces

###

# select example

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