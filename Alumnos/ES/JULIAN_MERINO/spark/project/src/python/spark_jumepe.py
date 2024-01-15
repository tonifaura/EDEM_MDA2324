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

''' We have 10 Ultra-Trail du Mont Blanc (UTMB) datasets from 2018 to 2023 (no race in 2020 due to the COVID-19 pandemic), divided in basic info and extra info and obtained 
    from LiveTrail database, we want to find out some insights, such as the performance of those athletes that run the race over the 5 years considered (both by absolute rank and 
    compared to themselves), ranks by country and by team.
'''
# 1. We get the info from the datasets and pass them to DFs

utmb_18DF = spark.read.option("header", "true").option("delimiter", ",").csv("/opt/project/resources/utmb_18.csv")
utmb_19DF = spark.read.option("header", "true").option("delimiter", ",").csv("/opt/project/resources/utmb_19.csv")
utmb_21DF = spark.read.option("header", "true").option("delimiter", ",").csv("/opt/project/resources/utmb_21.csv")
utmb_22DF = spark.read.option("header", "true").option("delimiter", ",").csv("/opt/project/resources/utmb_22.csv")
utmb_23DF = spark.read.option("header", "true").option("delimiter", ",").csv("/opt/project/resources/utmb_23.csv")
utmb_18extraDF = spark.read.option("header", "true").option("delimiter", ",").csv("/opt/project/resources/utmb_18_extra.csv")
utmb_19extraDF = spark.read.option("header", "true").option("delimiter", ",").csv("/opt/project/resources/utmb_19_extra.csv")
utmb_21extraDF = spark.read.option("header", "true").option("delimiter", ",").csv("/opt/project/resources/utmb_21_extra.csv")
utmb_22extraDF = spark.read.option("header", "true").option("delimiter", ",").csv("/opt/project/resources/utmb_22_extra.csv")
utmb_23extraDF = spark.read.option("header", "true").option("delimiter", ",").csv("/opt/project/resources/utmb_23_extra.csv")
utmb_18DF.show()
utmb_19DF.show()
utmb_21DF.show()
utmb_22DF.show()
utmb_23DF.show()
utmb_18extraDF.show()
utmb_19extraDF.show()
utmb_21extraDF.show()
utmb_22extraDF.show()
utmb_23extraDF.show()

# 2. Join and stack the DFs so we have a single DF containing all the results.

# Joins
utmb_23allDF = utmb_23DF.join(utmb_23extraDF, "Rank")
utmb_23allDF.show()
utmb_22allDF = utmb_22DF.join(utmb_22extraDF, "Rank")
utmb_22allDF.show()
utmb_21allDF = utmb_21DF.join(utmb_21extraDF, "Rank")
utmb_21allDF.show()
utmb_19allDF = utmb_19DF.join(utmb_19extraDF, "Rank")
utmb_19allDF.show()
utmb_18allDF = utmb_18DF.join(utmb_18extraDF, "Rank")
utmb_18allDF.show()