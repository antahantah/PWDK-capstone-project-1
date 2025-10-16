from config.setting import REQR_PATH
from scripts.extract import ekstrak2_csv
from scripts.transform import transform_data

# IMPORTANT -----Command Extract CSV
reqr_df = ekstrak2_csv(REQR_PATH)
print(reqr_df.head(15))


# print Company
# print(reqr_df['company'].head(12))
# print("\n")

# print Location
# print(reqr_df['location'].head(12))
# print("\n")

# print Salary
# print(reqr_df['salary_estimate'].head(12))
# print("\n")

# print Company Size
# print(reqr_df['company_size'].head(12))
# print("\n")

# print Company Size
# print(reqr_df['company_revenue'].head(12))
print("\n")

# print Dates
# print(reqr_df['dates'].head(12))
# print("\n")

# print Company Founded
# print(reqr_df['company_founded'].head(12))
# print("\n")

# print Company Other Detail
# print(reqr_df[['company_size', 'company_type', 'company_sector','company_industry']].head(12))
print("\n")

# print Company Revenue
# print(reqr_df['company_revenue'].head(12))
print("\n")

# IMPORTANT ----- Command Transform
afterTransform = transform_data(reqr_df)


# print Company
# print(afterTransform['company'].head(12))

# print Location dan area code
# print(afterTransform[['location', 'area_code']].head(12))

# print Currency dan Yearly Salary Estimate
# print(afterTransform[['currency', 'salary_estimate_yr']].head(12))

# print Company Size Threshold
# print(afterTransform['comp_size_low'].head(12))

# print Company Max Revenue
# print(afterTransform['company_max_rev'].head(12))

# print Jakarta Time
# print(afterTransform['jakarta_time'].head(12))

# print Company Founded
# print(afterTransform['company_founded'].head(12))

# print Company Other Detail
# print(afterTransform[['company_size', 'company_type', 'company_sector','company_industry']].head(12))

# print Company Revenue
# print(afterTransform['company_revenue'].head(12))


#PRINT ALL
print(afterTransform.head(15))