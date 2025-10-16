from config.setting import REQR_PATH
from scripts.extract import ekstrak2_csv
from scripts.transform import transform_data

# IMPORTANT -----Command Extract CSV
reqr_df = ekstrak2_csv(REQR_PATH)
# print(reqr_df.head(15))


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

# print Company Revenue
# print(reqr_df['company_revenue'].head(12))
# print("\n")

# print Dates
# print(reqr_df['dates'].head(12))
# print("\n")

# print Company Founded
# print(reqr_df['company_founded'].head(12))
# print("\n")

# print Company Other Detail
# print(reqr_df[['company_size', 'company_type', 'company_sector','company_industry']].head(12))
# print("\n")

# print Company Revenue
# print(reqr_df['company_revenue'].head(12))
# print("\n")

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

# ---- DATA DEMOGRAPHIC

print("\nberapa banyak row dan columns: ")
print(afterTransform.shape) 

#cek berapa count location yang bisa remote
print("\n\n\n\n\n\nberapa banyak yang bisa remote: ")
remoote = afterTransform['location'].str.contains('Remote').sum()
print(remoote)

# print(remote_no_salary[['company','company_rating', 'location', 'job_title', 'salary_estimate_yr' ]])

print("\n\n\n\n\n\nCompany Sector yang tidak diisi (N/A) adalah: ")
print(afterTransform["company_sector"].isnull().sum())

print("\n\n\n\n\n\nPerusahaan dengan code area CA ")
code_area_CA= afterTransform[afterTransform['area_code'] == 'CA']

CA_Rating_summary = code_area_CA['company_rating'].agg(['count', 'min', 'max', 'mean', 'median'])


print(code_area_CA[['company','company_rating', 'location', 'area_code', 'job_title']])

print("\n\n\n\n\n\nData aggregation pada Rating perusahaan dengan code area CA ")
print(CA_Rating_summary)


print("\n\n\n\n\n\nPerusahaan paling kaya (pendapatan 1 milyar lebih): ")
really_rich_company = afterTransform[afterTransform['company_max_rev'] > 1000000000]
print(really_rich_company[['company','company_rating', 'location', 'area_code', 'job_title','currency', 'salary_estimate_yr', 'company_revenue',]])

print("\n\n\n\n\n\ngaji tertinggi dari Perusahaan paling kaya (pendapatan 1 milyar lebih): ")
sorted_salary = really_rich_company.sort_values(by='salary_estimate_yr', ascending=False)
print(sorted_salary[['company','company_rating', 'location', 'area_code', 'job_title','currency', 'salary_estimate_yr', 'company_revenue',]].head(12))


print("\n\n\n\n\n\nPerusahaan code area WA yang employeenya paling banyak 1000:")

mini_WA =afterTransform[(afterTransform['comp_size_low'] < 1000) & (afterTransform['area_code'] == 'WA')]
print(mini_WA[['company','company_rating', 'location', 'area_code', 'job_title', 'company_size', 'company_founded']])