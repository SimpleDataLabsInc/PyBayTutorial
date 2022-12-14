from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from foodmatters.config.ConfigStore import *
from foodmatters.udfs.UDFs import *

def FilterOutBadZips(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter(
        (((col("zipcode") != lit("00000")) & (col("zipcode") != lit("99999"))) & col("zipcode").isNotNull())
    )
