import pandas as pd 

def ekstrak_csv(path):
    """

    Meng-extract file csv sesuai path yang dituju, index column di-exclude

    path = lokasi file csv
    return = hasil extract 

    """
    df = pd.read_csv(path, index_col=0)
    return df

def ekstrak2_csv(path):
    """

    Meng-extract file csv sesuai path yang dituju, index column di-exclude, usecols untuk mengambil data

    path = lokasi file csv
    return = hasil extract 

    """
    
    usecols = ["company", "company_rating", "location", "job_title", "job_description",	"salary_estimate", "company_size", "company_type", "company_sector", "company_industry", "company_founded", "company_revenue", "dates"]
    df = pd.read_csv(path, index_col=0, usecols = usecols)

    return df