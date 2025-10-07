from __future__ import print_function
from random import random
from operator import add
from pyspark.sql import SparkSession
from time import sleep

if __name__ == "__main__":
    spark = SparkSession.builder.appName("PythonPi").getOrCreate()
    n = 100000
    count = spark.sparkContext.parallelize(range(1, n + 1)).map(
        lambda _: 1 if random()**2 + random()**2 < 1 else 0
    ).reduce(add)
    print("Pi is roughly %f" % (4.0 * count / n))
    spark.stop()

    # Keep driver pod alive for 1 hour for testing / port-forward
    sleep(3600)





# # pi.py
# from __future__ import print_function
# from random import random
# from operator import add
# from pyspark.sql import SparkSession
#
# if __name__ == "__main__":
#     spark = SparkSession.builder.appName("PythonPi").getOrCreate()
#     n = 100000
#     count = spark.sparkContext.parallelize(range(1, n + 1)).map(
#         lambda _: 1 if random()**2 + random()**2 < 1 else 0
#     ).reduce(add)
#     print("Pi is roughly %f" % (4.0 * count / n))
#     spark.stop()
#
# mainApplicationFile: local:///opt/spark/examples/src/main/python/pi.py
