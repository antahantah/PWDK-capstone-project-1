import pandas as pd 

def ekstrak_csv(path):
    """

    Meng-extract file csv sesuai path yang dituju, filenya adalah fitness_accessories.csv
    index column di-exclude

    path = lokasi file csv
    df : mengambil data hasil extract
    return = hasil extract 

    """
    df = pd.read_csv(path, index_col=0)
    return df

def ekstrak2_csv(path):
    """

    Meng-extract file csv sesuai path yang dituju, filenya adalah data_requirements.csv
    index column di-exclude 
    usecols untuk mengambil data seluruh column selain unnamed

    path : lokasi file csv
    df : mengambil data hasil extract
    index_col=0 : menghilangkan index pada column default sebelah kiri
    usecols : mengambil semua column selain unnamed : 0 akibat kurang sempurna export to csv sebelumnya
    return : hasil extract 

    """
    
    usecols = [
        "company",
        "company_rating", 
        "location", 
        "job_title", 
        "job_description",	
        "salary_estimate", 
        "company_size", 
        "company_type", 
        "company_sector", 
        "company_industry", 
        "company_founded", 
        "company_revenue", 
        "dates"
    ]
    df = pd.read_csv(path, usecols = usecols)
    # df = pd.read_csv(path, index_col=0, usecols = usecols)

    return df