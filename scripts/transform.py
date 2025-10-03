import pandas as pd 
import numpy as np #hanya mendeklarasikan Unknown Company Size ke N/A

def transform_data(reqr_df):
    """
    Transform data requirements dan

    return adalah hasil akhir dari transform
    """

    # merapikan column company agar tidak ada value rating
    reqr_df['company'] = reqr_df['company'].str.split('\n').str[0]

    #____________________________________________________________________
    
    # memisahkan kode area dengan location
        # reqr_df['location'] = reqr_df['location'].str.split(', ').str[0]

    # pemisahan value berdasarkan comma dan tambah column area_code, n=1 mendeteksi split hanya untuk satu comma saja
    reqr_df[['location', 'area_code']] = reqr_df['location'].str.split(', ', n=1, expand=True)
    # mitigasi untuk yang tanpa area code, diberikan code Not Applicable
    reqr_df['area_code'] = reqr_df['area_code'].fillna('Not Applicable')

    #____________________________________________________________________
    
    #ambil data currency
    reqr_df['currency'] = reqr_df['salary_estimate'].str[0]

    #____________________________________________________________________

    # cleaning currency dan unused string, disimpan dahulu ke temp column clean_salary
    reqr_df['clean_salary'] = reqr_df['salary_estimate'].str.replace('$', '', regex=False).str.replace(',', '', regex=False)
    reqr_df['clean_salary'] = reqr_df['clean_salary'].str.split(' /').str[0]
    reqr_df['clean_salary'] = reqr_df['clean_salary'].astype(float)

    # menyamakan salary_estimate ke yearly, perubahan dikhususkan ke /hr
    is_hourly = reqr_df['salary_estimate'].str.contains('/hr', case=False, na=False) #case=False agar tidak menghitungkan uppercase lowercase, na=False untuk memberikan boolean False jika tidak menemukan /hr
    reqr_df['salary_estimate'] = reqr_df['clean_salary']

    #deteksi apakah masih berbentuk /hr atau tidak dengan .loc[boolean, column]
    reqr_df.loc[is_hourly, 'salary_estimate'] = reqr_df.loc[is_hourly, 'clean_salary'] * 2000
    reqr_df['salary_estimate'] = reqr_df['salary_estimate'].astype('Int64')

    #drop column clean_salary
    reqr_df.drop(columns='clean_salary', inplace=True)

    #rename salary_estimate menjadi salary_estimate_yearly
    reqr_df = reqr_df.rename(columns={'salary_estimate':'salary_estimate_yr'})

    #____________________________________________________________________

    #tambah column untuk memudahkan sorting company size jadi hanya mengambil angka paling kiri
    reqr_df['comp_size_low'] = reqr_df['company_size'].str.split(' ', n=1).str[0]
    reqr_df['comp_size_low'] = reqr_df['comp_size_low'].str.split('+').str[0]
    reqr_df['comp_size_low'] = reqr_df['comp_size_low'].replace('Unknown', np.nan)
    reqr_df['comp_size_low'] = pd.to_numeric(reqr_df['comp_size_low'], errors='coerce').astype('Int64')

    #____________________________________________________________________

    #tambah column untuk memudahkan sorting company_revenue jadi hanya mengambil angka paling tinggi
    reqr_df['clean_rev'] = reqr_df['company_revenue'].replace('Unknown / Non-Applicable', np.nan)

    reqr_df['rev_int'] = reqr_df['clean_rev'].str.replace('$', '', regex=False).str.replace(' (USD)', '')

    #pengecekan apakah jutaan atau milyaran
    reqr_df['Mil_Bil'] = reqr_df['rev_int'].str.split().str[-1]
    # reqr_df['Mil_Bil'] = reqr_df['Mil_Bil'].replace('Non-Applicable', np.nan)

    #mengambil revenue paling tinggi, untuk 10+ dijadikan 15 kemudian dijadikan int
    reqr_df['rev_int'] = reqr_df['rev_int'].str.split().str[-2]
    reqr_df['rev_int'] = reqr_df['rev_int'].replace('10+','15')
    reqr_df['rev_int'] = reqr_df['rev_int'].astype('Int64')

    #lakukan perkalian atau pencocokan dengan million atau billion pada kolom baru
    reqr_df['mult'] = 1
    reqr_df.loc[reqr_df['Mil_Bil'] == 'million', 'mult'] = 1000000
    reqr_df.loc[reqr_df['Mil_Bil'] == 'billion', 'mult'] = 1000000000

    reqr_df['company_max_rev'] = reqr_df['mult'] * reqr_df['rev_int']

    #drop column clean_rev
    reqr_df.drop(columns=['clean_rev','rev_int','Mil_Bil','mult'], inplace=True)

    #____________________________________________________________________

    #mengubah dates menjadi seragam ke WIB, kemudian timezone dihilangkan agar lebih rapi
    reqr_df['true_time'] = pd.to_datetime(reqr_df['dates'], utc=True)
    reqr_df['jakarta_time'] = reqr_df['true_time'].dt.tz_convert('Asia/Jakarta').dt.tz_localize(None)

    #____________________________________________________________________

    # mengubah column tahun menjadi int64
    reqr_df['company_founded'] = reqr_df['company_founded'].astype('Int64')

    # reqr_df = reqr_df.reset_index(drop=True)

    # return reqr_df
    
    return reqr_df[['company', 'company_rating', 'location', "job_title", "job_description", 'area_code', 'salary_estimate_yr', 
                    'comp_size_low', 'company_size', 'company_type', 'company_sector', 'company_industry', 'company_founded', 
                    'company_max_rev', 'company_revenue', 'jakarta_time' ]]