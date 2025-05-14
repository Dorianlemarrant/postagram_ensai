#################################################################################################
##                                                                                             ##
##                                 NE PAS TOUCHER CETTE PARTIE                                 ##
##                                                                                             ##
## 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 ##
import boto3
from botocore.config import Config
import os
import uuid
from dotenv import load_dotenv
from typing import Union
import logging
from fastapi import FastAPI, Request, status, Header
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

from getSignedUrl import getSignedUrl

load_dotenv()

app = FastAPI()
logger = logging.getLogger("uvicorn")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
	exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
	logger.error(f"{request}: {exc_str}")
	content = {'status_code': 10422, 'message': exc_str, 'data': None}
	return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


class Post(BaseModel):
    title: str
    body: str

my_config = Config(
    region_name='us-east-1',
    signature_version='v4',
)

dynamodb = boto3.resource('dynamodb', config=my_config)
table = dynamodb.Table(os.getenv("DYNAMO_TABLE"))
s3_client = boto3.client('s3', config=boto3.session.Config(signature_version='s3v4'))
bucket = os.getenv("BUCKET")

## ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ##
##                                                                                                ##
####################################################################################################


from boto3.dynamodb.conditions import Key

@app.post("/posts")
async def post_a_post(post: Post, authorization: str | None = Header(default=None)):
    logger.info(f"title : {post.title}")
    logger.info(f"body : {post.body}")
    logger.info(f"user : {authorization}")

    str_id = f'{uuid.uuid4()}'

    item = {
        'id': f'POST#{str_id}',
        'user': f'USER#{authorization}',
        'title': post.title,
        'body': post.body,
        'image': '',
        'label': []
    }

    res = table.put_item(Item=item)
    return {"message": "Post créé", "post_id": str_id}


@app.get("/posts")
async def get_all_posts(user: Union[str, None] = None):
    if user:
        logger.info(f"Récupération des postes de : {user}")
        response = table.query(
            KeyConditionExpression=Key('user').eq(f'USER#{user}')
        )
        items = response.get("Items", [])
    else:
        logger.info("Récupération de tous les postes")
        response = table.scan()
        items = response.get("Items", [])

    for item in items:
        if item.get("image"):
            item["image"] = s3_client.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': bucket,
                    'Key': item["image"]
                },
                ExpiresIn=3600
            )

    return items


@app.delete("/posts/{post_id}")
async def delete_post(post_id: str, authorization: str | None = Header(default=None)):
    user_key = f'USER#{authorization}'
    post_key = f'POST#{post_id}'

    response = table.get_item(Key={'user': user_key, 'id': post_key})
    item = response.get("Item")

    if not item:
        return JSONResponse(status_code=404, content={"message": "Post not found"})

    if "image" in item and item["image"]:
        try:
            s3_client.delete_object(Bucket=bucket, Key=item["image"])
        except Exception as e:
            logger.warning(f"Erreur S3 : {e}")

    table.delete_item(Key={'user': user_key, 'id': post_key})

    return {"message": "Post supprimé"}




#################################################################################################
##                                                                                             ##
##                                 NE PAS TOUCHER CETTE PARTIE                                 ##
##                                                                                             ##
## 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 👇 ##
@app.get("/signedUrlPut")
async def get_signed_url_put(filename: str,filetype: str, postId: str,authorization: str | None = Header(default=None)):
    return getSignedUrl(filename, filetype, postId, authorization)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="debug")

## ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ☝️ ##
##                                                                                                ##
####################################################################################################