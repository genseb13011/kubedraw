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
          SELECT * FROM namespaces
          """
          )

  namespaces = c.fetchall()

  with Diagram("K8S diagram", show=False):
    for namespace in namespaces:
      with Cluster("%s" % (namespace)):
        net = Ingress("ingress1") >> Service("Service1")
        with Cluster("Deployment1"):
          pods = [Pod("pod1"),Pod("pod2")]
      net >> pods

  conn.commit()