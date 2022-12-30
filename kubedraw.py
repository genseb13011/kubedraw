#Import lib
from functions import *

#set variables
db_name='kubedraw.db'

#delete and recreate database
delete_db(db_name)
create_db(db_name)
create_tables(db_name)

#insert namespaces in database
namespaces=list_k8s_namespaces()

for namespace in namespaces:
    add_namespace(db_name,namespace)

select_namespace(db_name)

#insert services in database
services_name, services_namespace = list_k8s_services()

for service_name in services_name:
    print(service)

for service_namespace in services_namespace:
    print service_namespace
