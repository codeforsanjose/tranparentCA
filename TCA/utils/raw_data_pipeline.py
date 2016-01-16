import csv

import utils.file_ops as fo

# TODO make default file value with relative path to raw file


def read(file='E:\\git.projects\\TransparentCA\\raw_data\\2010-counties.csv'):
    """This function a generator reading csv file with raw data.

    Args:
       file[string]: Should be a full path to the csv path.
       The function makes the following assumptions:
       - file exists;
       - file is a correct csv with headers;

    Returns:
        generator with dictionary contains records from csv file
        key - column name
        value - current record value in the column
    """
    # read headers from csv file
    headers = fo.read_headers(file)
    num_of_headers = len(headers)

# TODO move to the config file
    implemented_headers = ['EMPLOYEE_NAME', 'JOB_TITLE', 'BASE_PAY', 'OVERTIME_PAY', 'OTHER_PAY', 'BENEFITS', 'TOTAL_PAY', 'TOTAL_PAY_BENEFITS', 'YEAR', 'NOTES',
                           'AGENCY', 'EMPLOYER', 'PENSION_AMOUNT', 'BENEFITS_AMOUNT', 'DISABILITY_AMOUNT', 'TOTAL_AMOUNT', 'YEARS_OF_SERVICE', 'YEAR_OF_RETIREMENT', 'PENSION_SYSTEM']

    for item in range(0, num_of_headers):

        # processing rule: university-system.csv has different name for
        # benefits
        if headers[item] == 'total_benefits':
            headers[item] = 'Benefits'

        # processing rule: some university_system.csv has different name for
        # agency
        if headers[item] == 'jurisdiction_name':
            headers[item] = 'Agency'

        # process headers to make them uniform
        headers[item] = headers[item].upper()
        headers[item] = headers[item].replace('&', '')
        headers[item] = headers[item].replace(' ', '_')
        headers[item] = headers[item].replace('__', '_')

        header = headers[item]

        # check that all headers are known
        if header not in implemented_headers:
            print("FILE: " + file)
            raise NotImplementedError('Unknown header value:' + header)

    with open(file) as f:
        csv_f = csv.reader(f)
        next(csv_f)  # skip headers
        for record in csv_f:
            record_dict = {}
            for item in range(0, num_of_headers):
                record_dict[headers[item]] = record[item]

            yield record_dict
