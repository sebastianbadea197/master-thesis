import numpy as np
import pandas as pd
import os

def select_timeseries(company_shortname, feature_list):
    """Create a timeseries dataframe for a given company and feature list

    Args:
        company_shortname (string): The shortname of the company from the clean data
        feature_list (list): the list of features to include in the dataframe

    Returns:
        dataframe: the resulting timeseries dataframe
    """
    dfs = []

    if "Date" not in feature_list:
        feature_list.append("Date")

    for file in os.listdir('../clean_data'):
        if file.endswith('.csv'):
            df = pd.read_csv('../clean_data/' + file)
            df = df[df['ShortName'] == company_shortname]
            df = df[feature_list]
            dfs.append(df)
    
    df = pd.concat(dfs, axis=0)
    df['Date'] = pd.to_datetime(df['Date'])
    df.sort_values(by='Date', inplace=True)
    df.reset_index(drop=True, inplace=True)

    return df