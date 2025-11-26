from pyspark.sql import SparkSession
spark1=spark.withColumn("new_column",spark["existing_column"]*2)
spark.display()