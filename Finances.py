from pyspark.sql import SparkSession
filePath = f"C:\\Users\\User\\Documents\\Finance - all expences -22_6-01.xlsm"


spark = (SparkSession.builder
.config("spark.jar.packages","com.crealytics.spark.excel_2.11")
.config("")
.getOrCreate())

# print(dir(SparkSession))
# print()
# print(dir(SparkSession.builder))
# print()
# print(dir(spark))
sparkDF = spark.read.format("com.crealytics.spark.excel") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("dataAddress", "'Sheet2'!A1") \
    .load(filePath)


sparkDF.display()