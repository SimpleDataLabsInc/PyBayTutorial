from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from foodmatters.config.ConfigStore import *
from foodmatters.udfs.UDFs import *
from prophecy.utils import *
from foodmatters.graph import *

def pipeline(spark: SparkSession) -> None:
    df_IRSZipCodesSource = IRSZipCodesSource(spark)
    df_FilterOutBadZips = FilterOutBadZips(spark, df_IRSZipCodesSource)
    df_CastDataTypes = CastDataTypes(spark, df_FilterOutBadZips)
    df_SumIncomeBracketsByZip = SumIncomeBracketsByZip(spark, df_CastDataTypes)
    df_CalcIsHighIncome = CalcIsHighIncome(spark, df_SumIncomeBracketsByZip)
    df_FarmersMarketSource = FarmersMarketSource(spark)
    df_FilterOutNullZips = FilterOutNullZips(spark, df_FarmersMarketSource)
    df_CountFarmersMarketsByZip = CountFarmersMarketsByZip(spark, df_FilterOutNullZips)
    df_JoinFarmersMarketsAndIncome = JoinFarmersMarketsAndIncome(
        spark, 
        df_CountFarmersMarketsByZip, 
        df_CalcIsHighIncome
    )
    df_CalcHasFm = CalcHasFm(spark, df_JoinFarmersMarketsAndIncome)
    df_CalcCases = CalcCases(spark, df_CalcHasFm)
    Target_1(spark)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "3154/pipelines/FoodMatters")
    MetricsCollector.start(spark = spark, pipelineId = "3154/pipelines/FoodMatters")
    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
