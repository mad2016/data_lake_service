import logging
import boto3
from botocore.exceptions import ClientError
import os
import pandas as pd
import redshift_connector
from utils import secrets


config = secrets.read_secrets_from_config()

ACCESS_KEY = config.get("ACCESS_KEY")
SECRET_KEY = config.get("SECRET_KEY")
HOST = config.get("HOST")
DATABASE = config.get("DATABASE")
USER = config.get("USER")
PASSWORD = config.get("PASSWORD")

s3 = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY
    )

def upload_file_to_s3(file_name, bucket, object_name=None):
    
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file

    try:
        s3.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def get_file_names(bucket_name):
    keys = []
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    prefix_objs = bucket.objects.filter()
    # (Prefix="/")
    for obj in prefix_objs:
        keys.append(obj.key)
    return keys


def read_csv_to_pandas(bucket_name, file_name):

    response = s3.get_object(Bucket=bucket_name, Key=file_name)

    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode")

    if status == 200:
        print(f"Successful S3 get_object response. Status - {status}")
        books_df = pd.read_csv(response.get("Body"), header=None)
        return books_df
    else:
        print(f"Unsuccessful S3 get_object response. Status - {status}")


def sync_s3_to_redshift(bucket_name, file_name):

    conn = redshift_connector.connect(host=HOST, database=DATABASE, user=USER,
                                      password=PASSWORD)

    copy_cmd_str = "COPY " + file_name + " from s3://" + bucket_name + "/" + file_name

    with conn.cursor() as curs:
        curs.execute(copy_cmd_str)
