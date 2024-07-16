from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB


with Diagram("Clustered Web Services", show=True):
    lb = ELB("nginx load balancer")

    with Cluster("Database Cluster"):
        db_cluster1 = [RDS("ENVIS DB"), RDS("JETFORGE DB")]

    with Cluster("Web Services"):
        svc_grp = [
            EC2("controller"),
            EC2("materials"),
            EC2("shopfloor"),
            # EC2("subcon"),
            # EC2("repairs"),
            # EC2("manpower"),
            EC2("forecast-input"),
            # EC2("system-workscope"),
        ]

    lb >> svc_grp
    svc_grp >> db_cluster1
