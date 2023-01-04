from diagrams import Cluster, Diagram
from diagrams.k8s.clusterconfig import HPA
from diagrams.k8s.compute import Deployment, Pod, ReplicaSet
from diagrams.k8s.network import Ingress, Service

def draw_diagram():

  with Diagram("K8S diagram", show=False):
    with Cluster("Namespace1"):
      net = Ingress("ingress1") >> Service("Service1")
      with Cluster("Deployment1"):
        pods = [Pod("pod1"),Pod("pod2")]
    net >> pods