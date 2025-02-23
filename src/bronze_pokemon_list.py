# Databricks notebook source
df = spark.read.json("/Volumes/raw/pokemon/pokemon_raw/pokemons_list/")

(df.distinct()
 .coalesce(1)
 .write
 .format("delta")
 .mode("overwrite")
 .saveAsTable("bronze.pokemon.pokemon_list")
 )

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT * FROM bronze.pokemon.pokemon_list
