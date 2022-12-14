from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from foodmatters.config.ConfigStore import *
from foodmatters.udfs.UDFs import *

def CountFarmersMarketsByZip(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("zip"))

    return df1.agg(count(lit(1)).alias("num_farmers_markets"))
