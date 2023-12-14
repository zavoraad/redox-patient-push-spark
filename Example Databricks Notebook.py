# Databricks notebook source
# MAGIC %md # Clinical Summary

# COMMAND ----------

# MAGIC %python 
# MAGIC import json, os, uuid
# MAGIC from pyspark.sql.types import StructType
# MAGIC from pyspark.sql.functions import expr
# MAGIC
# MAGIC
# MAGIC schema = StructType.fromJson(json.load(open("./schemas/clinicalsummary-patientpush.spark.json", "r")))
# MAGIC df = spark.read.option("multiline", True).format("json").schema(schema).load("file:///" + os.getcwd() + "/sampledata/*json") 
# MAGIC
# MAGIC df = df.withColumn("bundleUUID", expr("uuid()"))

# COMMAND ----------

df.select("Meta.Source.*").show()

# COMMAND ----------


df.write.saveAsTable("hls_healthcare.hls_dev.clinical_patient_summary")

#
# Parallel column writes 
#
"""
#                                                                                                                      
# parallel writes to a table                                                                                           
#                                                                                                                      
def copyWrite(df, colName):
    df.select(colName).write.mode("append").parquet(str(colName) +".parquet")

from multiprocessing.pool import ThreadPool
import multiprocessing as mp
pool = ThreadPool(mp.cpu_count()-1)

import time
start = time.time()
list(pool.map(lambda x: copyWrite(df, x), df.columns))
end = time.time()
print(end - start)
"""

# COMMAND ----------

# MAGIC %sql
# MAGIC select explode(encounters) as encounters from hls_healthcare.hls_dev.clinical_patient_summary limit 10;

# COMMAND ----------

# MAGIC %md # Visit Summary 

# COMMAND ----------

#TBD...
