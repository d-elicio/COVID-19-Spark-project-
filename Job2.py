from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import col,lit,desc,avg,count,max as max_

spark=SparkSession.builder.appName("Job2").getOrCreate()
myFile="/home/domenico/spark-3.0.1-bin-hadoop3.2/input/Input-MAR_APR/Input-covid-MARZO_APRILE.csv"
# myFile="/user/domenico/input/inputMarzoOttobre"
myData=spark.read.format("csv").option("header","true").option("inferSchema","true").load(myFile)

newTestsCorrected=myData.fillna({"new_tests":"0"})
newTestsCorrected.select(col("location"),col("new_tests"))\
.groupBy("location").agg((avg("new_tests").cast("int")).alias("Average number of new tests"))\
.orderBy(col("location")).show(newTestsCorrected.count())

spark.stop()
