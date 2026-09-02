from pyspark.sql.types import *

def build_schema(schema):
    type_map = {
        "string": StringType(),
        "timestamp": TimestampType(),
        "double": DoubleType(),
        "integer": IntegerType()
    }
    return StructType([
        StructField(
            column,
            type_map[data_type],
            True
        )
        for column, data_type in schema["schema"].items()
    ])