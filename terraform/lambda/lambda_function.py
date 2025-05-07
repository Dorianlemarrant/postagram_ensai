import json
from urllib.parse import unquote_plus
import boto3
import os
import logging
print('Loading function')
logger = logging.getLogger()
logger.setLevel("INFO")
s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
reckognition = boto3.client('rekognition')

table = dynamodb.Table(os.getenv("table"))

def lambda_handler(event, context):
    logger.info(json.dumps(event, indent=2))
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = unquote_plus(event["Records"][0]["s3"]["object"]["key"]) # <- A modifier !!!!

    # Récupération de l'utilisateur et de l'UUID de la tâche
    try:
        user, task_uuid = key.split('/')[:2]
    except ValueError:
        logger.error("Nom de fichier invalide, attendu: user/id/image.jpg")
        return

    # Ajout des tags user et task_uuid
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
    except Exception as e:
        logger.error(f"Erreur lors de l'ajout des tags: {e}")
        return
    # Appel à reckognition
    # Appel au service, en passant l'image à analyser (bucket et key)
    # On souhaite au maximum 5 labels et uniquement les labels avec un taux de confiance >0.75
    # Vous pouvez faire varier ces valeurs.
    label_data = reckognition.detect_labels(
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key
            }
        },
        MaxLabels=5,
        MinConfidence=0.75
    )
    logger.info(f"Labels data : {label_data}")

    # Récupération des résultats des labels
    labels = [label["Name"] for label in label_data.get("Labels", [])]
    logger.info(f"Labels détectés : {labels}")

    # Mise à jour de la table dynamodb
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