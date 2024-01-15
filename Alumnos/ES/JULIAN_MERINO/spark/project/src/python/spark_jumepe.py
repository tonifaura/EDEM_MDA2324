# Initialise Spark Session
from pyspark.sql import SparkSession

# Create the session
spark = SparkSession \
        .builder \
        .appName("Window Partitioning") \
        .master("local[*]") \
        .getOrCreate()

spark.version
spark

# For Pandas conversion optimization
spark.conf.set("spark.sql.execution.arrow.enabled", "true")

# Import sql functions
from pyspark.sql.functions import *

utmb_18DF = spark.read.option("header", "true").option("delimiter", ";").csv("/opt/project/resources/utmb_18.csv")
utmb_19DF = spark.read.option("header", "true").option("delimiter", ";").csv("/opt/project/resources/utmb_19.csv")
utmb_21DF = spark.read.option("header", "true").option("delimiter", ";").csv("/opt/project/resources/utmb_21.csv")
utmb_22DF = spark.read.option("header", "true").option("delimiter", ";").csv("/opt/project/resources/utmb_22.csv")
utmb_23DF = spark.read.option("header", "true").option("delimiter", ";").csv("/opt/project/resources/utmb_23.csv")
utmb_18DF.show()
utmb_19DF.show()
utmb_21DF.show()
utmb_22DF.show()
utmb_23DF.show()