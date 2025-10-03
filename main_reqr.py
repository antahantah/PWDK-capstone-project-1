from config.setting import REQR_PATH
from scripts.extract import ekstrak2_csv
from scripts.transform import transform_data

# Command Extract CSV
reqr_df = ekstrak2_csv(REQR_PATH)
# print(reqr_df.head(15))

# print(reqr_df['company_rating'].dtype)

afterTransform = transform_data(reqr_df)
print(afterTransform.tail(10))
# print(afterTransform['company_rating'].tail(10))
# print(afterTransform['job_description'].isnull().sum())