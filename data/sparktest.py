from pyspark.sql import SparkSession

# Cria a sessão Spark
spark = SparkSession.builder \
    .appName("Leitura de Parquet") \
    .getOrCreate()

# Lê o arquivo Parquet
df = spark.read.parquet("data/raw/sample_data.parquet")

# Mostra os primeiros registros
df.show(5)