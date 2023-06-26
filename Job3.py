from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col,lit,desc,avg,count,max as max_

spark=SparkSession.builder.appName("Job2").getOrCreate()
myFile="/home/domenico/spark-3.0.1-bin-hadoop3.2/input/Input-MAR_APR/Input-covid-MARZO_APRILE.csv"
#myFile="/user/domenico/input/inputMarzoOttobre"
myData=spark.read.format("csv").option("header","true").option("inferSchema","true").load(myFile)

myDataCorrected=myData.fillna({"icu_patients":"0"}).fillna({"hosp_patients":"0"})
a=myDataCorrected.select(col("date"),col("icu_patients"),col("hosp_patients"))\
.withColumn("Total_patients",col("icu_patients")+ col("hosp_patients")).groupBy("date")\
.agg(F.sum("Total_patients").cast("int").alias("Total num of patients"))\
.orderBy(col("Total num of patients").desc()).show(5)
spark.stop()
