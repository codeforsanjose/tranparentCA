
import pandas as pd
import utils.config as conf

df_counties = pd.read_csv(
    '..\\raw_data\\mock-counties.csv', dtype=conf.COLUMN_DATA_TYPES, na_values=conf.ERROR_VALUES, header=0, names=conf.SALARY_COLUMN_NAMES)


print(df_counties.info())

df_counties.to_csv('output.csv')
