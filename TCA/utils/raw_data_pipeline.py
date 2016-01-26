import csv
import re

import utils.file_ops as fo

# TODO make default file value with relative path to raw file

# TODO move to the config file

implemented_headers = ['EMPLOYEE_NAME', 'JOB_TITLE', 'BASE_PAY', 'OVERTIME_PAY', 'OTHER_PAY', 'BENEFITS', 'TOTAL_PAY', 'TOTAL_PAY_BENEFITS', 'YEAR', 'NOTES',
                       'AGENCY', 'EMPLOYER', 'PENSION_AMOUNT', 'BENEFITS_AMOUNT', 'DISABILITY_AMOUNT', 'TOTAL_AMOUNT', 'YEARS_OF_SERVICE', 'YEAR_OF_RETIREMENT', 'PENSION_SYSTEM']

money_fields = ['BASE_PAY', 'OVERTIME_PAY', 'OTHER_PAY', 'BENEFITS', 'TOTAL_PAY', 'TOTAL_PAY_BENEFITS',
                'PENSION_AMOUNT', 'BENEFITS_AMOUNT', 'DISABILITY_AMOUNT', 'TOTAL_AMOUNT', 'YEARS_OF_SERVICE']

year_fields = ['YEAR', 'YEAR_OF_RETIREMENT']


def read(file):
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

    # process headers to make them uniform
    for item in range(0, num_of_headers):

        # processing rule: university-system.csv has different name for
        # benefits
        if headers[item] == 'total_benefits':
            headers[item] = 'Benefits'

        # processing rule: some university_system.csv has different name for
        # agency
        if headers[item] == 'jurisdiction_name':
            headers[item] = 'Agency'

        # make all headers UPPERCASE and remove inconsistent additional symbols
        headers[item] = headers[item].upper()
        headers[item] = headers[item].replace('&', '')
        headers[item] = headers[item].replace(' ', '_')
        headers[item] = headers[item].replace('__', '_')

        header = headers[item]

        # check that all headers are known
        if header not in implemented_headers:
            print("FILE: " + file)
            raise NotImplementedError('Unknown header value: ' + header)

    # created filename parameter
    split_name = file.split('\\')
    file_name = (split_name[len(split_name) - 1])

    # open csv file
    with open(file) as f:
        csv_f = csv.reader(f)

        # skip headers
        next(csv_f)

        # read data rows from csv file
        for record in csv_f:

            # create empty dictionary for each row
            record_dict = {}

            # iterate over the fields in the raw and put in into dictionary
            # using headers as the keys.

            for item in range(0, num_of_headers):

                # DATA PROCESSING RULES FOR THE RECORD VALUES SHOULD BE PUT
                # HERE

                # TODO: Make debug log for data processing rules: print
                # value and filename to figure out what
                # exactly inside the file

                # some money values contains 'Aggregate', change them to 'Not
                # Provided'
                if record[item].upper() == 'AGGREGATE':
                    record[item] = 'Not Provided'

                # some money values are empty, change them to 'Not Provided'
                if record[item] == '':
                    if headers[item] in money_fields:
                        record[item] = 'Not Provided'

                # money values contain 'Beneficiary'
                if record[item] == 'Beneficiary':
                    if headers[item] in money_fields:
                        record[item] = 'Not Provided'

                # money values contain 'N/A'
                if record[item] == 'N|A':
                    if headers[item] in money_fields:
                        record[item] = 'Not Provided'

                # END OF PROCESSING RULES

                record_dict[headers[item]] = record[item]

            # adding file name to the each record
            record_dict["FILE"] = file_name

            # return record through the generator
            yield record_dict


def validate_money_field(record):

    for field in money_fields:

        # Pension and salary have different set of fields. To keep this procedure universal
        # we don't care if some fields are not found
        if field not in record.keys():
            continue

        field_value = record[field]

        # Let 'not provided' to pass. We will handle them at database level
        if field_value == 'Not Provided':
            continue

        # If value looks like 0.0 let it pass
        if re.match('\d+\.?\d*', field_value) != None:
            continue

        # Some money fields have negative values. Let this values pass
        if float(field_value) < 0:
            continue

        print(record)
        # Otherwise raise exception
        print('FILE: ' + record['FILE'])
        raise NotImplementedError(
            'Incorrect money field value: ' + field_value)
    return


def validate_year_field(record):
    # See explanation of the algo in the validate_money_field

    for field in year_fields:
        if field not in record.keys():
            continue

        field_value = record[field]

        if re.match('[1,2][9,0][0-9][0-9]', field_value) != None:
            return

        print(record)
        print('FILE: ' + record['FILE'])
        raise NotImplementedError('Incorrect year field value: ' + field_value)

    return


def get_record(file):
    '''Interface method for pipeline.

    Args:
    file[string]: file name (without path) to read

    Returns: generator
    '''
    fo.check_file_exists(file, False)
    records = read(file)
    for record in records:
        validate_money_field(record)
        validate_year_field(record)

        yield record
