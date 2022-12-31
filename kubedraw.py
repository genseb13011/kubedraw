#Import lib
from .functions.functions import *

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
services_count=len(services_name)

i_services = 0

while i_services < services_count:
    add_service(db_name,services_name[i_services],services_namespace[i_services])
    i_services = i_services + 1

select_service(db_name)
