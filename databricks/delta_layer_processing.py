from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RetailDeltaLayer").getOrCreate()

df = spark.read.parquet("gs://manoj-retail-lake-001/transform/retail_parquet")

df.write.format("delta").mode("overwrite").save(
    "gs://manoj-retail-lake-001/analytics/retail_delta"
)

spark.stop()
