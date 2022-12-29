from functions import *

db_name='kubedraw.db'

delete_db(db_name)
create_db(db_name)
create_tables(db_name)

namespaces=list_namespace()

for namespace in namespaces:
    add_namespace(db_name,namespace)

