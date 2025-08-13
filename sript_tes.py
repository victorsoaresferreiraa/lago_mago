from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Test Spark") \
    .master("local[*]") \
    .getOrCreate()

print("Spark iniciado com sucesso!")
spark.stop()