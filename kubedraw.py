############
#Import lib#
############
from .functions.functions import *

###############
#Set variables#
###############
db_name='kubedraw.db'

namespace_table_request="CREATE TABLE IF NOT EXISTS namespace ([name] TEXT PRIMARY KEY UNIQUE)"
service_table_request="CREATE TABLE IF NOT EXISTS service ([id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, UNIQUE(name,namespace))"
pod_table_request="CREATE TABLE IF NOT EXISTS pod ([id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, UNIQUE(name,namespace))"

######
#Main#
######

#delete and recreate database
delete_db(db_name)
create_db(db_name)

#create tables
create_table(db_name,namespace_table_request)
create_table(db_name,service_table_request)
create_table(db_name,pod_table_request)

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
