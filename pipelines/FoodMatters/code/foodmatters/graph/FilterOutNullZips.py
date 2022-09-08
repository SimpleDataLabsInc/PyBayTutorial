from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from foodmatters.config.ConfigStore import *
from foodmatters.udfs.UDFs import *

def FilterOutNullZips(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(col("zip").isNotNull())
