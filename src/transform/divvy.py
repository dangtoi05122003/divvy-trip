from utils import get_logger, load_yaml, load_setting
from utils.spark_session import get_spark
from transform.schema import build_schema
from pyspark.sql.functions import col, row_number
from pyspark.sql import Window

logger = get_logger(__name__)
setting = load_setting()
class Silver:
    def __init__(self):
        self.config = load_yaml("/opt/spark/config/silver.yml")
        self.schema = load_yaml("/opt/spark/config/schema.yml")
        self.spark = get_spark()
    def run(self):
        bronze_path = self.config['path']['bronze_path'].format(bucket_name = setting.bucket_name)
        silver_path = self.config['path']['silver_path'].format(bucket_name = setting.bucket_name)
        logger.info(f"Read bronze: {bronze_path}")
        df = self.spark.read.schema(build_schema(self.schema)).option("header", True).csv(bronze_path)
        df =self.process(df)
        logger.info(f"Write silver: {silver_path}")
        df.write.mode("overwrite").partitionBy("year").parquet(silver_path)
    def process(self, df):
        for step in self.config['process']:
            if "filter" in step:
                for name, condition in step['filter'].items():
                    logger.info(f"Applying filter: {name}")
                    df = df.filter(condition)
            if "deduplicate" in step:
                config = step["deduplicate"]
                subset = config["subset"]
                logger.info(f"Deduplicate: {subset}")
                df = df.dropDuplicates(subset)
        return df
if __name__ == "__main__":
    Silver().run()