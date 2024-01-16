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
from pyspark.sql import Window
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

# Stacks
utmb_allDF = utmb_23allDF.union(utmb_22allDF)
utmb_allDF = utmb_allDF.union(utmb_21allDF)
utmb_allDF = utmb_allDF.union(utmb_19allDF)
utmb_allDF = utmb_allDF.union(utmb_18allDF)
utmb_allDF.show(10000)

# Let's now do some analysis: find the top 3 performers by gender and year:

# First thing will be to make sure that columns "Rank", "Year" and "YOB" are integers:
columns_to_int = ["Rank", "Year", "YOB"]
for i in columns_to_int:
  utmb_allDF = utmb_allDF.withColumn(i, col(i).cast("integer"))

# Now we need to create a Window so that it frames the data by Gender and Year:
Window_Gender_Year = Window.partitionBy("Gender", "Year").orderBy(col("Rank"))

# And we pass it all
Top3_byGender_byYearDF = utmb_allDF.withColumn("GenRank", row_number().over(Window_Gender_Year)).filter(col("GenRank") <= 3)
Top3_byGender_byYearDF = Top3_byGender_byYearDF.select("GenRank", *Top3_byGender_byYearDF.columns)#.drop(Top3_byGender_byYearDF.columns[-1])
Top3_byGender_byYearDF.show(30)

# Now, let's see how the top performers (Rank #1) per gender compare, in separate DFs. First, we create an appropriate window:
Window_Rank_Time = Window.partitionBy("GenRank").orderBy(col("Time"))

# Men
Top1_MaleDF = Top3_byGender_byYearDF.filter(col("Gender") == "M").withColumn("WinnerRank", row_number().over(Window_Rank_Time)).filter(col("GenRank") == 1)
#Top1_MaleDF = Top1_MaleDF.select("WinnerRank", *Top1_MaleDF.columns).drop(Top1_MaleDF.columns[-1])
Top1_MaleDF.show()
# Women
Top1_FemaleDF = Top3_byGender_byYearDF.filter(col("Gender") == "F").withColumn("WinnerRank", row_number().over(Window_Rank_Time)).filter(col("GenRank") == 1)
#Top1_FemaleDF = Top1_FemaleDF.select("WinnerRank", *Top1_FemaleDF.columns).drop(Top1_FemaleDF.columns[-1])
Top1_FemaleDF.show()

#POSTGRESQL CONNECTION AND INGESTION
from sqlalchemy import create_engine, Integer
import psycopg2

# Connection parameters
db_params = {
    'host': 'postgres',
    'port': 5432,
    'user': 'postgres',
    'password': 'Welcome01',
    'database': 'postgres',
}

# SQLAlchemy
db_uri = f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"
engine = create_engine(db_uri)


# DF stored in DB
utmb_allDF.to_sql('utmb_all', engine, if_exists='replace', index=False)
Top3_byGender_byYearDF.to_sql('Top3_byGender_byYear', engine, if_exists='replace', index=False)
Top1_MaleDF.to_sql('Top1_Male', engine, if_exists='replace', index=False)
Top1_FemaleDF.to_sql('Top1_Female', engine, if_exists='replace', index=False)