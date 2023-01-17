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
  config.load_incluster_config()

  v1 = client.NetworkingV1Api()
  ingress = v1.list_ingress_for_all_namespaces(watch=False)
  services_list=[]
  ingress_count = len(ingress.items)
  
  i = 0
  while i < ingress_count:
    name=ingress.items[i].metadata.name
    namespace=ingress.items[i].metadata.namespace
    ingressclassname=ingress.items[i].spec.ingress_class_name
    rules_length=len(ingress.items[i].spec.rules)
    j = 0
    while j < rules_length:
      path_length=len(ingress.items[i].spec.rules[j].http.paths)
      k=0
      while k < path_length:
        service_name=ingress.items[i].spec.rules[j].http.paths[k].backend.service.name
        services_list.append(service_name)
        k = k + 1
      j = j + 1
    
    services_list_length=len(services_list)
    services_result=""
    i=0
    while i < services_list_length:
      services_result = services_result + services_list[i]

    c.execute("""
            INSERT INTO ingress(name,namespace,ingressclass,services)
            VALUES
            ("%s","%s","%s")
            """ 
            % (name, namespace, ingressclassname,services_result)
            )
    i = i + 1
          
  conn.commit()
