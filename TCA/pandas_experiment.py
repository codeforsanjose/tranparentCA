import time

import pandas as pd
import utils.config as config
import utils.misc as misc


file_start_time = time.time()
# importing configuration
data_type = config.COLUMN_DATA_TYPES
error_values = config.ERROR_VALUES
column_names = config.SALARY_COLUMN_NAMES

# load different files in pandas dataframes
df_payroll = pd.read_csv(
    '..\\raw_data\\2011-payroll.csv', dtype=data_type, na_values=error_values, header=0, names=column_names)

df_cities = pd.read_csv(
    '..\\raw_data\\2011-cities.csv', dtype=data_type, na_values=error_values, header=0, names=column_names)

df_counties = pd.read_csv(
    '..\\raw_data\\2011-counties.csv', dtype=data_type, na_values=error_values, header=0, names=column_names)

df_university_system = pd.read_csv(
    '..\\raw_data\\2011-university-system.csv', dtype=data_type, na_values=error_values, header=0, names=column_names)

# concatenate several dataframes into single
df_result = pd.concat(
    objs=[df_payroll, df_cities, df_counties, df_university_system])
file_end_time = time.time()

# print time result
print("Processing time:", misc.formatted_time(file_end_time - file_start_time))

print("Not deduplicated size of dataframe: ", len(df_result))
# print(df_result.info())

df_result.drop_duplicates(['Employee Name', 'Job Title', 'Base Pay', 'Overtime Pay',
                           'Other Pay', 'Benefits', 'Total Pay',
                           'Total Pay & Benefits', 'Year'], inplace=True)  # Inplace should be true or it retruns not duplicated set

print("Deduplicated size of dataframe: ", len(df_result))
print(df_result.info())

#df_grouped = df_result.groupby('Job Title').count()
# df_grouped.to_csv('output.csv')
df_result.to_csv('..\\output\\output.csv')

print("done")
