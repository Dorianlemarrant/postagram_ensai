#!/usr/bin/env python
from constructs import Construct
from cdktf import App, TerraformStack, TerraformAsset, AssetType
from cdktf_cdktf_provider_aws.provider import AwsProvider
from cdktf_cdktf_provider_aws.lambda_function import LambdaFunction
from cdktf_cdktf_provider_aws.iam_role import IamRole
from cdktf_cdktf_provider_aws.iam_role_policy_attachment import IamRolePolicyAttachment
from cdktf_cdktf_provider_aws.sqs_queue import SqsQueue
from cdktf_cdktf_provider_aws.lambda_event_source_mapping import LambdaEventSourceMapping

class MyStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # define resources here


#app = App()
#MyStack(app, "ter")

#app.synth()


class LambdaStack(TerraformStack):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        AwsProvider(self, "AWS", region="us-east-1")

        # Archive du dossier ./lambda
        code = TerraformAsset(self, "lambda-zip",
            path="./lambda",
            type=AssetType.ARCHIVE
        )

        # Lambda
        lambda_function = LambdaFunction(self,
                "lambda",
                function_name="first_lambda",
                runtime="python3.8",
                memory_size=128,
                timeout=60,
                role="arn:aws:iam::ID_COMPTE:role/LabRole",
                filename= code.path,
                handler="lambda_function.lambda_function",
                environment={"variables":{"foo":"bar"}})

        # SQS
        queue = SqsQueue(
            self,
            "queue",
            name="input_queue",
            visibility_timeout_seconds=60
        )

        # Connect SQS → Lambda
        LambdaEventSourceMapping(self, "lambda-sqs-link",
            event_source_arn=queue.arn,  # ARN de la file SQS
            function_name=lambda_function.arn,  # ARN de la fonction Lambda
            batch_size=1  # Taille du lot de messages à traiter
        )


app = App()
LambdaStack(app, "ter")

app.synth()