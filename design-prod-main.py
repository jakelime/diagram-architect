from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS, RDSMysqlInstance
from diagrams.aws.general import Client, Users, User
from diagrams.aws.network import ELB


with Diagram("PPCS Design - Dev Main", show=True):
    client = Users("users")
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
        controller - forecast_input
        controller - sysworkscope

    with Cluster("DB Cluster"):
        db_primary = RDS("ENVIS_RDS")
        envis_db = RDSMysqlInstance("envis_db")
        jetforge_db = RDSMysqlInstance("jetforge_db")
        smartanalytics_db = RDSMysqlInstance("smartanalytics_db")
        db_primary - [envis_db, jetforge_db, smartanalytics_db]

    client >> nginx >> controller
    controller >> db_primary
    shopfloor >> jetforge_db
    materials >> smartanalytics_db
    subcon >> smartanalytics_db
    # controller - shopfloor
