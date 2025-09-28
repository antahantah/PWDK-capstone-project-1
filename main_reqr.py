from config.setting import REQR_PATH
from scripts.extract import ekstrak2_csv

# Command Extract CSV
reqp_df = ekstrak2_csv(REQR_PATH)
print(reqp_df.head(15))