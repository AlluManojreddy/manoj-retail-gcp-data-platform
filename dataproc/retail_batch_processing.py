from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RetailBatchEngine").getOrCreate()

df = spark.read.json("gs://manoj-retail-lake-001/landing/stream*")

filtered_df = df.filter(df.amount > 0)

filtered_df.write.mode("overwrite").parquet(
    "gs://manoj-retail-lake-001/transform/retail_parquet"
)

spark.stop()
