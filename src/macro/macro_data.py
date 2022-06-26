import pandas as pd


def get_gdp(fred):
    data = fred.get_series('GDP')
    data.rename("GDP",inplace=True)
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