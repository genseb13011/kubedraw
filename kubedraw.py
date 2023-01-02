############
#Import lib#
############
from functions.database import *
from functions.namespace import *
from functions.service import *

###############
#Set variables#
###############
db_name='kubedraw.db'

namespace_columns="[name] TEXT PRIMARY KEY UNIQUE"
service_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, UNIQUE(name,namespace)"
pod_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, UNIQUE(name,namespace)"

######
#Main#
######

#delete and recreate database
delete_db(db_name)
create_db(db_name)

#create tables
create_table(db_name,"namespace",namespace_columns)
create_table(db_name,"service",service_columns)
create_table(db_name,"pod",pod_columns)

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
