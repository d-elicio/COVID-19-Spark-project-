from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col,lit,desc,max as max_

spark=SparkSession.builder.appName("Job1").getOrCreate()
myFile="/home/domenico/spark-3.0.1-bin-hadoop3.2/input/Input-MAR_APR/Input-covid-MARZO_APRILE.csv"
#myFile="/user/domenico/input/inputMarzoOttobre"
myData=spark.read.format("csv").option("header","true").option("inferSchema","true").load(myFile)

confrontDate=myData.agg((max_("date").cast("date")).alias("data2")).collect()[0][0]
myData.select(col("continent"),col("location"),col("total_cases"),col("date")).withColumn("confront_date",lit(confrontDate))\
        .filter(col("date")==col("confront_date"))\
        .groupBy("continent").agg(F.sum("total_cases").cast("int").alias("Number of total cases"))\
        .filter(col("continent")!="null")\
        .orderBy(col("Number of total cases").desc()).show()
spark.stop()
