#!/usr/bin/env python
from constructs import Construct
from cdktf import App

# Importation des deux stacks
from main_server import ServerStack
from main_serverless import ServerlessStack

app = App()

# Création des deux stacks sous un même projet
ServerlessStack(app, "cdktf_serverless")
ServerStack(app, "cdktf_server")

app.synth()
