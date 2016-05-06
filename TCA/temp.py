'''
Created on May 5, 2016

@author: max
'''

import pandas as pd
import utils.config as conf

df_counties = pd.read_csv(
    '..\\raw_data\\2011-counties.csv', dtype=conf.COLUMN_DATA_TYPES, na_values=conf.ERROR_VALUES, header=0, names=conf.SALARY_COLUMN_NAMES)

df_university_system = pd.read_csv(
    '..\\raw_data\\2011-university-system.csv', dtype=conf.COLUMN_DATA_TYPES, na_values=conf.ERROR_VALUES, header=0, names=conf.SALARY_COLUMN_NAMES)

print(df_counties.info())

print("===================")

print(df_university_system.info())
