############
#Import lib#
############
from functions.database import *
from functions.namespace import *
from functions.service import *
from functions.deployment import *
from functions.pod import *
from functions.configmap import *
from functions.secret import *
from functions.ingress import *
from functions.ingressclass import *
from functions.persistentvolume import *
from functions.storageclass import *
from functions.persistentvolumeclaim import *
from functions.draw_diagram import *

###############
#Set variables#
###############
db_name='kubedraw.db'

namespace_columns="[name] TEXT PRIMARY KEY UNIQUE"
service_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, [type] TEXT , [selector] TEXT, UNIQUE(name,namespace)"
deployment_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, [selector] TEXT, UNIQUE(name,namespace)"
pod_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, UNIQUE(name,namespace)"
configmap_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, UNIQUE(name,namespace)"
secret_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, [type] TEXT, UNIQUE(name,namespace)"
ingress_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [namespace] TEXT, [ingressclass] TEXT, [services] TEXT, UNIQUE(name,namespace)"
ingressclass_columns="[id] INTEGER PRIMARY KEY, [name] TEXT"
persistentvolume_columns="[id] INTEGER PRIMARY KEY, [name] TEXT, [storageclassname] TEXT"
storageclass_columns="[id] INTEGER PRIMARY KEY, [name] TEXT"
persistentvolumeclaim_columns="[id] INTEGER PRIMARY KEY, [name] TEXT"

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
create_table(db_name,"ingressclass",ingressclass_columns)
create_table(db_name,"persistentvolume",persistentvolume_columns)
create_table(db_name,"storageclass",storageclass_columns)
create_table(db_name,"persistentvolumeclaim",persistentvolumeclaim_columns)


#insert resources in database
insert_namespaces(db_name)
insert_services(db_name)
insert_deployments(db_name)
insert_pods(db_name)
insert_configmaps(db_name)
insert_secrets(db_name)
insert_ingress(db_name)
insert_ingressclass(db_name)
insert_persistentvolumes(db_name)
insert_storageclass(db_name)
insert_persistentvolumeclaims(db_name)

print("Namespaces")
db_select(db_name,"namespace")
print("Services")
db_select(db_name,"service")
print("Deployments")
db_select(db_name,"deployment")
print("Pods")
db_select(db_name,"pod")
print("Configmaps")
db_select(db_name,"configmap")
print("Secrets")
db_select(db_name,"secret")
print("Ingress")
db_select(db_name,"ingress")
print("IngressClass")
db_select(db_name,"ingressclass")
print("PersistentVolumes")
db_select(db_name,"persistentvolume")
print("storageclass")
db_select(db_name,"storageclass")
print("PersistentVolumeClaims")
db_select(db_name,"persistentvolumeclaim")

draw_diagram(db_name)