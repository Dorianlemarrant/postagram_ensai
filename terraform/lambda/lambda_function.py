import json
import logging
import os
from urllib.parse import unquote_plus

import boto3

# Initialisation des logs
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Clients AWS
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
rekognition = boto3.client('rekognition')

# Nom de la table DynamoDB, défini via variable d’environnement dans CDK
DDB_TABLE = os.getenv("table")  # 🟡 À bien définir dans CDK plus tard
table = dynamodb.Table(DDB_TABLE)

def lambda_handler(event, context):
    logger.info("Événement reçu : %s", json.dumps(event, indent=2))

    try:
        bucket = event["Records"][0]["s3"]["bucket"]["name"]
        key = unquote_plus(event["Records"][0]["s3"]["object"]["key"])
        user, task_uuid = key.split('/')[:2]
    except (KeyError, ValueError, IndexError) as e:
        logger.error(f"Erreur lors de l'extraction des infos S3 ou parsing clé: {e}")
        return {"statusCode": 400, "body": "Erreur dans la structure de l'événement"}

    # 🏷️ Ajout de tags S3
    try:
        s3.put_object_tagging(
            Bucket=bucket,
            Key=key,
            Tagging={
                'TagSet': [
                    {'Key': 'user', 'Value': user},
                    {'Key': 'task_uuid', 'Value': task_uuid}
                ]
            }
        )
        logger.info(f"Tags ajoutés à l’objet S3 : {user}, {task_uuid}")
    except Exception as e:
        logger.error(f"Erreur lors de l'ajout des tags S3 : {e}")
        return {"statusCode": 500, "body": "Erreur lors du tagging"}

    # 📷 Analyse d’image via Rekognition
    try:
        response = rekognition.detect_labels(
            Image={
                "S3Object": {
                    "Bucket": bucket,
                    "Name": key
                }
            },
            MaxLabels=5,
            MinConfidence=75.0
        )
        labels = [label["Name"] for label in response.get("Labels", [])]
        logger.info(f"Labels détectés : {labels}")
    except Exception as e:
        logger.error(f"Erreur avec Rekognition : {e}")
        return {"statusCode": 500, "body": "Erreur avec Rekognition"}

    # 🗃️ Mise à jour de DynamoDB
    try:
        table.update_item(
            Key={
                "user": user,
                "id": task_uuid
            },
            UpdateExpression="SET labels = :labels",
            ExpressionAttributeValues={
                ":labels": labels
            }
        )
        logger.info("Item DynamoDB mis à jour avec les labels.")
    except Exception as e:
        logger.error(f"Erreur lors de la mise à jour DynamoDB : {e}")
        return {"statusCode": 500, "body": "Erreur DynamoDB"}

    return {"statusCode": 200, "body": f"Image analysée : {labels}"}