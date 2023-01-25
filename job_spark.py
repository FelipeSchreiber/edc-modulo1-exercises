import pyspark
from pyspark.sql.functions import col, count
from pyspark.sql import SparkSession


pathSource = "s3://datalake-felipeschreiber-689150947157/raw-data/"
pathDestination = "s3://datalake-felipeschreiber-689150947157/consumer-zone/"

# Create SparkSession
spark = (
          SparkSession.builder
                      .appName('tarn-csv-to-parquet')
                      .getOrCreate()
         )


# DataframeRead 
df_enem = (spark.read
                .format("csv")
                .option("header", "true")
                .option("sep", ";")
                .option("encoding", "ISO-8859-1")
                .option("inferSchema", "true")
                .load(pathSource)
                .withColumn("year", col("NU_ANO")))


# DataframeWrite 
(
  df_enem.write
         .format("parquet")
         .mode("overwrite")
         .partitionBy("year")
         .save(pathDestination)
)
