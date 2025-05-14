#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.default_vpc import DefaultVpc
from cdktf_cdktf_provider_aws.default_subnet import DefaultSubnet
from cdktf_cdktf_provider_aws.launch_template import LaunchTemplate
from cdktf_cdktf_provider_aws.lb import Lb
from cdktf_cdktf_provider_aws.lb_target_group import LbTargetGroup
from cdktf_cdktf_provider_aws.lb_listener import LbListener, LbListenerDefaultAction
from cdktf_cdktf_provider_aws.autoscaling_group import AutoscalingGroup
from cdktf_cdktf_provider_aws.security_group import SecurityGroup, SecurityGroupIngress, SecurityGroupEgress
from cdktf_cdktf_provider_aws.data_aws_caller_identity import DataAwsCallerIdentity

import base64

# Infos provenant de la partie serverless
bucket = "s320250514144543646900000001"
dynamo_table = "posts"
your_repo = "https://github.com/Dorianlemarrant/postagram_ensai"

user_data = base64.b64encode(f"""#!/bin/bash
echo "userdata-start"        
apt update
apt install -y python3-pip python3.12-venv
git clone {your_repo} projet
cd projet/webservice
python3 -m venv venv
source venv/bin/activate
rm .env
echo 'BUCKET={bucket}' >> .env
echo 'DYNAMO_TABLE={dynamo_table}' >> .env
pip3 install -r requirements.txt
venv/bin/python app.py
echo "userdata-end"
""".encode("ascii")).decode("ascii")


class ServerStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)
        account_id, security_group, subnets, default_vpc = self.infra_base()

        launch_template = LaunchTemplate(
            self, "launch_template",
            image_id="ami-053b0d53c279acc90",  # Ubuntu Server 22.04 LTS us-east-1
            instance_type="t2.micro",
            vpc_security_group_ids=[security_group.id],
            key_name="my-keypair",  
            user_data=user_data,
            tags={"Name": "TP-noté"},
            iam_instance_profile={"name": "LabInstanceProfile"}
        )

        lb = Lb(
            self, "lb",
            load_balancer_type="application",
            security_groups=[security_group.id],
            subnets=subnets
        )

        target_group = LbTargetGroup(
            self, "target_group",
            port=8080,
            protocol="HTTP",
            vpc_id=default_vpc.id,
            target_type="instance"
        )

        lb_listener = LbListener(
            self, "lb_listener",
            load_balancer_arn=lb.arn,
            port=80,
            protocol="HTTP",
            default_action=[LbListenerDefaultAction(
                type="forward",
                target_group_arn=target_group.arn
            )]
        )

        asg = AutoscalingGroup(
            self, "asg",
            min_size=1,
            max_size=3,
            desired_capacity=1,
            launch_template={"id": launch_template.id},
            vpc_zone_identifier=subnets,
            target_group_arns=[target_group.arn]
        )

    def infra_base(self):
        AwsProvider(self, "AWS", region="us-east-1")
        account_id = DataAwsCallerIdentity(self, "account_id").account_id

        default_vpc = DefaultVpc(self, "default_vpc")

        az_ids = [f"us-east-1{i}" for i in "abcdef"]
        subnets = [
            DefaultSubnet(self, f"default_sub{i}", availability_zone=az_id).id
            for i, az_id in enumerate(az_ids)
        ]

        security_group = SecurityGroup(
            self, "sg-tp",
            ingress=[
                SecurityGroupIngress(from_port=22, to_port=22, protocol="TCP", cidr_blocks=["0.0.0.0/0"]),
                SecurityGroupIngress(from_port=80, to_port=80, protocol="TCP", cidr_blocks=["0.0.0.0/0"]),
                SecurityGroupIngress(from_port=8080, to_port=8080, protocol="TCP", cidr_blocks=["0.0.0.0/0"]),
            ],
            egress=[
                SecurityGroupEgress(from_port=0, to_port=0, protocol="-1", cidr_blocks=["0.0.0.0/0"])
            ]
        )

        return account_id, security_group, subnets, default_vpc


app = App()
ServerStack(app, "cdktf_server")
app.synth()
