from pyspark.sql import SparkSession

def get_spark(key: str = "/opt/spark/key.json"):
    return SparkSession.builder.appName("divvy") \
        .config("spark.hadoop.fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem") \
        .config("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
        .config("spark.hadoop.google.cloud.auth.service.account.json.keyfile", key) \
        .config("spark.sql.shuffle.partitions", "400") \
        .config("spark.hadoop.fs.gs.outputstream.upload.chunk.size", "16777216") \
        .getOrCreate()