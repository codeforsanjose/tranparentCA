import time

import pandas as pd


def formated_time(seconds_total):
    ''' convert number of seconds in the tuple (hours, minutes, seconds)
    '''
    minutes, seconds = divmod(seconds_total, 60)
    hours, minutes = divmod(minutes, 60)
    seconds = round(seconds)
    minutes = round(minutes)
    hours = round(hours)

    return (hours, minutes, seconds)


file_start_time = time.time()

data_type = {'Employee Name': str, 'Job Title': str, 'Base Pay': float, 'Overtime Pay': float,
             'Other Pay': float, 'Benefits': float, 'Total Pay': float,
             'Total Pay & Benefits': float, 'Year': int, 'Notes': str, 'Agency': str}

error_values = ["Aggregate", "Not Provided", "N/A"]

column_names = ['Employee Name', 'Job Title', 'Base Pay', 'Overtime Pay',
                'Other Pay', 'Benefits', 'Total Pay',
                'Total Pay & Benefits', 'Year', 'Notes', 'Agency']

df_payroll = pd.read_csv(
    '..\\raw_data\\2011-payroll.csv', dtype=data_type, na_values=error_values, header=0, names=column_names)

df_cities = pd.read_csv(
    '..\\raw_data\\2011-cities.csv', dtype=data_type, na_values=error_values, header=0, names=column_names)

df_counties = pd.read_csv(
    '..\\raw_data\\2011-counties.csv', dtype=data_type, na_values=error_values, header=0, names=column_names)

df_university_system = pd.read_csv(
    '..\\raw_data\\2011-university-system.csv', dtype=data_type, na_values=error_values, header=0, names=column_names)

df_result = pd.concat(
    objs=[df_payroll, df_cities, df_counties, df_university_system])
file_end_time = time.time()
print(formated_time(file_end_time - file_start_time))
print(len(df_result))
# print(df_result.info())
df_result.drop_duplicates(['Employee Name', 'Job Title', 'Base Pay', 'Overtime Pay',
                           'Other Pay', 'Benefits', 'Total Pay',
                           'Total Pay & Benefits', 'Year'], inplace=True)  # Inplace should be true or it retruns not duplicated set
print(len(df_result))
#df_grouped = df_result.groupby('Job Title').count()
# df_grouped.to_csv('output.csv')
df_result.to_csv('output.csv')
print("done")

''' 

2. memory consuptions
3. deduplication (see 13.14 in the cookbook)

'''
