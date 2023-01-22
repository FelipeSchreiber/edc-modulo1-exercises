from pyspark import *
from pyspark.sql import SparkSession


spark = {
    SparkSession.builder
    .appName("ExerciseSpark")
    .getOrCreate()
}

df = spark.read\
    .csv('s3://datalake-felipeschreiber-689150947157/raw-data/microdados_enem_2020.csv',\
        sep=";",\
        header = True)

df.write.mode('overwrite')\
        .format('parquet')\
        .partitionBy("NU_ANO")\
        .save('s3://datalake-felipeschreiber-689150947157/consumer-zone/microdados_enem_2020.parquet')
