from pyspark.sql import SparkSession

# Create SparkSession
spark = (
          SparkSession.builder
                      .master("local[*]")
                      .appName('tarn-csv-parquet')
                      .config("spark.sql.shuffle.partitions", 8)  
                      .getOrCreate()
         )


df_enem = (spark.read
                .format("csv")
                .option("header", "true")
                .option("sep", ";")
                .option("inferSchema", "true")
                .load("s3://datalake-felipeschreiber-689150947157/raw-data/microdados_enem_2020.csv"))


(
  df_enem.write
         .format("parquet")
         .option("compression","snappy")
         .mode("overwrite")
         .option("mergeSchema", "true")
         .partitionBy("NU_ANO")
         .save('s3://datalake-felipeschreiber-689150947157/consumer-zone/microdados_enem_2020.parquet')
)
