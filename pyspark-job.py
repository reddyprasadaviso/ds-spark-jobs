from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("MySparkJob").getOrCreate()

# Sample DataFrame
data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
columns = ["Name", "Age"]

df = spark.createDataFrame(data, columns)
df.show()

# Some transformations
df_filtered = df.filter(df.Age > 30)
df_filtered.show()

# Save output (optional)
df_filtered.write.csv("/tmp/output.csv")

spark.stop()
