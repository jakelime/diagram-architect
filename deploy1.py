from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS, DynamodbTable
from diagrams.aws.general import Client
from diagrams.aws.network import ELB

with Diagram("PPCS Dev Design", show=True):
    client = Client("user_client")
    nginx = ELB("nginx reverse proxy")

    with Cluster("Services"):
        controller = EC2("controller")
        materials = EC2("materials")
        shopfloor = EC2("shopfloor")
        subcon = EC2("subcon")
        repairs = EC2("repairs")
        manpower = EC2("manpower")
        forecast_input = EC2("forecast-input")
        sysworkscope = EC2("system-workscope")
        svc_group = [
            controller,
            materials,
            shopfloor,
            subcon,
            repairs,
            manpower,
            forecast_input,
            sysworkscope,
        ]

        controller - materials
        controller - shopfloor
        controller - subcon
        controller - repairs
        controller - manpower
        controller - sysworkscope
        controller - forecast_input


    with Cluster("DB Cluster"):
        db_primary = RDS("ENVIS_RDS")
        db_primary - [DynamodbTable("envis"), DynamodbTable("jetforge")]

    client >> nginx >> controller
    svc_group >> db_primary
