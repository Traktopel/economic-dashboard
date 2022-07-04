import pandas as pd


def get_gdp(fred):
    data = fred.get_series('GDP')
    data.rename("GDP",inplace=True)
    return data
def get_real_gdp(fred):
    data = fred.get_series('GDPC1')
    data.rename("Real GDP",inplace=True)
    return data

def get_cpi(fred):
    data = fred.get_series('CPIAUCSL')
    data.rename("CPI for all Urban Consumers: All Items in U.S. City Average",inplace=True)
    return data
def get_core_cpi(fred):
    data = fred.get_series('CPILFESL')
    data.rename("CPI for all Urban Consumers: All Items less Food and Energy",inplace=True)
    return data
def get_cpi_components(fred):
    data=pd.DataFrame()
    data['All Items']=(fred.get_series('CPIAUCSL').pct_change(12)*100).tail(1)
    data['Food and Beverages']=(fred.get_series('CPIFABSL').pct_change(12)*100).tail(1)
    data['Housing']=(fred.get_series('CPIHOSSL').pct_change(12)*100).tail(1)
    data['Apparel']=(fred.get_series('CPIAPPSL').pct_change(12)*100).tail(1)
    data['Transportation']=(fred.get_series('CPITRNSL').pct_change(12)*100).tail(1)
    data['Medical Care']=(fred.get_series('CPIMEDSL').pct_change(12)*100).tail(1)
    data['Recreation']=(fred.get_series('CPIRECSL').pct_change(12)*100).tail(1)
    data['Education and communication']=(fred.get_series('CPIEDUSL').pct_change(12)*100).tail(1)
    data['Other good and services']=(fred.get_series('CPIOGSSL').pct_change(12)*100).tail(1)
    data.reset_index(inplace=True)
    data.rename(columns={"index": "Date"},inplace=True)
    
    data=pd.melt(data,id_vars=['Date'],value_vars=['All Items','Food and Beverages','Housing','Apparel',
    'Transportation','Medical Care','Recreation','Education and communication','Other good and services'],
    var_name='Components',value_name='Inflation')

    return data

def get_all_loans(fred):
    data = data = fred.get_series('TOTLL')
    data.rename("LOANS",inplace=True)
    return data

def get_industrial_loans(fred):
    data = data = fred.get_series('TOTCI')
    data.rename("Industrial Loans",inplace=True)
    return data

def get_consumer_loans(fred):
    data = data = fred.get_series('CLSACBW027SBOG')
    data.rename("Consumer Loans",inplace=True)
    return data

def get_re_loans(fred):
    data = data = fred.get_series('RELACBW027SBOG')
    data.rename("Real Estate Loans",inplace=True)
    return data
   

def get_other_loans(fred):
    data = data = fred.get_series('AOLACBW027SBOG')
    data.rename("Other Loans",inplace=True)
    return data

def get_loans_by_type(fred):
    date_from='2015-01-01'
    industrial_loans = get_industrial_loans(fred).to_frame()
    industrial_loans=industrial_loans[(industrial_loans.index > date_from)]
    

    consumer_loans=get_consumer_loans(fred).to_frame()
    consumer_loans=consumer_loans[(consumer_loans.index > date_from)]


    re_loans=get_re_loans(fred).to_frame()
    re_loans=re_loans[(re_loans.index > date_from)]

    other_loans=get_other_loans(fred).to_frame()
    other_loans=other_loans[(other_loans.index > date_from)]
    data=industrial_loans
    data=data.join(consumer_loans)
    data=data.join(re_loans)
    data=data.join(other_loans)

    data=data.reset_index()
    data.rename(columns={"index": "Date"},inplace=True)
    data=pd.melt(data,id_vars=['Date'],value_vars=['Industrial Loans','Consumer Loans','Real Estate Loans','Other Loans'])

    return data