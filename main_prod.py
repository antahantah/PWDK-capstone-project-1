from config.setting import PROD_PATH
from scripts.extract import ekstrak_csv

# Command Extract CSV
prod_df = ekstrak_csv(PROD_PATH)
print(prod_df.head())
