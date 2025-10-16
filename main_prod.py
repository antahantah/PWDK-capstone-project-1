from config.setting import PROD_PATH
from scripts.extract import ekstrak_csv
from scripts.transform import transform_fit

# Command Extract CSV
prod_df = ekstrak_csv(PROD_PATH)
# print(prod_df.head(15))

afterTransform = transform_fit(prod_df)
print(afterTransform.head(15))

checkDataTypes = afterTransform.dtypes
# print(f" Jenis-jenis tipe data:\n{checkDataTypes}")

# print(afterTransform.iloc[200:215][['ratings','no_of_ratings','currency','final_price']])

print(afterTransform.iloc[200:215])