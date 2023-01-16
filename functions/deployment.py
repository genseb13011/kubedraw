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
  config.load_incluster_config()

  v1 = client.AppsV1Api()
  deployments = v1.list_deployment_for_all_namespaces(watch=False)
  deployments_count = len(deployments.items)
  
  i = 0
  while i < deployments_count:
    name=deployments.items[i].metadata.name
    namespace=deployments.items[i].metadata.namespace
    selector=deployments.items[i].spec.selector.match_labels

    c.execute("""
            INSERT INTO deployment(name,namespace,selector)
            VALUES
            ("%s","%s","%s")
            """ 
            % (name, namespace,selector)
            )
    i = i + 1
          
  conn.commit()
