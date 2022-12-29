#Import lib
from functions import *

#set variables
db_name='kubedraw.db'

#delete and recreate database
delete_db(db_name)
create_db(db_name)
create_tables(db_name)

#insert namespace in database
namespaces=list_k8s_namespace()

for namespace in namespaces:
    add_namespace(db_name,namespace)

select_namespace(db_name)