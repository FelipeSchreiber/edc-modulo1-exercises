import boto3

s3_client = boto3.client("s3",region_name="us-east-2")
s3_client.upload_file("microdados_enem_2020/DADOS/MICRODADOS_ENEM_2020.csv","datalake-felipeschreiber-689150947157","raw-data/microdados_enem_2020.csv")
