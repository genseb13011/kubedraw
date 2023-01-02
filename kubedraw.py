############
#Import lib#
############
from functions.database import *
from functions.namespace import *
from functions.service import *
from functions.deployment import *
from functions.pod import *
from functions.configmap import *
from functions.ingress import *

###############
#Set variables#
###############
db_name='kubedraw.db'

namespace_columns="[name] TEXT PRIMARY KEY UNIQUE"
service_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, [selector] TEXT, UNIQUE(name,namespace)"
deployment_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, UNIQUE(name,namespace)"
pod_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, UNIQUE(name,namespace)"
configmap_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, UNIQUE(name,namespace)"
secret_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, UNIQUE(name,namespace)"
ingress_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, UNIQUE(name,namespace)"

######
#Main#
######

#delete and recreate database
delete_db(db_name)
create_db(db_name)

#create tables
create_table(db_name,"namespace",namespace_columns)
create_table(db_name,"service",service_columns)
create_table(db_name,"deployment",deployment_columns)
create_table(db_name,"pod",pod_columns)
create_table(db_name,"configmap",configmap_columns)
create_table(db_name,"secret",secret_columns)
create_table(db_name,"ingress",ingress_columns)


#insert resources in database
insert_namespaces(db_name)
insert_services(db_name)
insert_deployments(db_name)
insert_pods(db_name)
insert_configmaps(db_name)
insert_ingress(db_name)

select_namespaces(db_name)
select_services(db_name)
select_deployments(db_name)
select_pods(db_name)
select_configmaps(db_name)
select_ingress(db_name)
