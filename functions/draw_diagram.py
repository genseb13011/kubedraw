from diagrams import Cluster, Diagram
from diagrams.k8s.clusterconfig import HPA
from diagrams.k8s.compute import Deployment, Pod, ReplicaSet
from diagrams.k8s.network import Ingress, Service
import sqlite3

def draw_diagram(db_name):

  conn = None
  try:
    conn = sqlite3.connect(db_name)
  except Error as e:
    print(e)

  c = conn.cursor()

  c.execute("""
          SELECT name FROM namespace
          """
          )

  namespaces = c.fetchall()

  with Diagram("K8S diagram", show=False):
    for namespace in namespaces:
      with Cluster("%s" % (namespace)):
        c.execute("""
        SELECT name FROM ingress where namespace = '%s'
        """ % (namespace)
        )
        ingress_list = c.fetchall()
        for ingress in ingress_list:
          Ingress("%s" % (ingress))

        c.execute("""
        SELECT name FROM deployment where namespace = '%s'
        """ % (namespace)
        )

        deployments = c.fetchall()
        for deployment in deployments:
          with Cluster("%s" % (deployment)):

            c.execute("""
            SELECT name FROM pod where namespace = '%s' AND name like '%s'
            """ % (namespace, deployment+'%')
            )
            pods = c.fetchall()
            for pod in pods:
              Pod("%s" % (pod))

  conn.commit()