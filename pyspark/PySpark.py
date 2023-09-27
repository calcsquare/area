from pyspark.sql import SparkSession
from pyspark.sql.functions import collect_list
import pandas as pd

# Создадим сессию Spark
spark = SparkSession.builder.appName("ProductCategories").getOrCreate()

# Генерируем случайные данные для продуктов и категорий с использованием pandas
product_data = {
    "product_id": range(1, 11),
    "product_name": ["Product{}".format(i) for i in range(1, 11)]
}

category_data = {
    "category_id": range(1, 6),
    "category_name": ["Category{}".format(i) for i in range(1, 6)]
}

# Создаем pandas датафрейм для продуктов и категорий
products_df = pd.DataFrame(product_data)
categories_df = pd.DataFrame(category_data)

# Создаем PySpark датафрейм из pandas датафрейм
products_df_spark = spark.createDataFrame(products_df)
categories_df_spark = spark.createDataFrame(categories_df)

# Отображаем сгенерированные данные
products_df_spark.show()
categories_df_spark.show()

# Присоединим продукты и категории по соответствующим столбцам
joined_df = products_df.join(categories_df, products_df.product_id == categories_df.product_id, "left")

# Группируем данные по имени продукта и собераем список категорий
result_df = joined_df.groupBy("product_name").agg(collect_list("category_name").alias("categories"))

# Добавим продукты без категорий (с пустым списком категорий)
result_df = result_df.union(
    products_df.join(categories_df, products_df.product_id == categories_df.product_id, "left_anti")
        .select("product_name")
        .withColumn("categories", list([]))  # Добавляем пустой список категорий
)

# Завершаем сессию
spark.stop()
