'''

Modules stores global constants

@author: Maksim Habets
'''

COLUMN_DATA_TYPES = {'Employee Name': str, 'Job Title': str, 'Base Pay': float, 'Overtime Pay': float,
                     'Other Pay': float, 'Benefits': float, 'Total Pay': float,
                     'Total Pay & Benefits': float, 'Year': int, 'Notes': str, 'Agency': str, 'Employer': str,
                     'Pension Amount': float, 'Total Amount': float, 'Years of Service': float, 'Year of Retirement': int,
                     'Pension system': str}

ERROR_VALUES = ["Aggregate", "Not Provided", "N/A", "Beneficiary"]

SALARY_COLUMN_NAMES = ['Employee Name', 'Job Title', 'Base Pay', 'Overtime Pay',
                       'Other Pay', 'Benefits', 'Total Pay',
                       'Total Pay & Benefits', 'Year', 'Notes', 'Agency']

DEFAULT_RAW_DATA_DIR = '..\\raw_data\\'

DEFAULT_OUTPUT_DIR = '..\\output\\'

PENSION_COLUMN_NAMES = ['Employee Name', 'Job Title', 'Employer',
                        'Pension Amount', 'Benefits',
                        'Disability Amount', 'Total Amount',
                        'Years of Service', 'Year of Retirement',
                        'Year', 'Notes', 'Pension System']
