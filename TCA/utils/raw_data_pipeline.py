import csv
import os
import re

import utils.file_ops as fo


# TODO make default file value with relative path to raw file
# TODO move to the config file
implemented_headers = ['EMPLOYEE_NAME', 'JOB_TITLE', 'BASE_PAY', 'OVERTIME_PAY', 'OTHER_PAY', 'BENEFITS', 'TOTAL_PAY', 'TOTAL_PAY_BENEFITS', 'YEAR', 'NOTES',
                       'AGENCY', 'EMPLOYER', 'PENSION_AMOUNT', 'BENEFITS_AMOUNT', 'DISABILITY_AMOUNT', 'TOTAL_AMOUNT', 'YEARS_OF_SERVICE', 'YEAR_OF_RETIREMENT', 'PENSION_SYSTEM']

money_fields = ['BASE_PAY', 'OVERTIME_PAY', 'OTHER_PAY', 'BENEFITS', 'TOTAL_PAY', 'TOTAL_PAY_BENEFITS',
                'PENSION_AMOUNT', 'BENEFITS_AMOUNT', 'DISABILITY_AMOUNT', 'TOTAL_AMOUNT', 'YEARS_OF_SERVICE']

year_fields = ['YEAR', 'YEAR_OF_RETIREMENT']


class validation_error_logger:
    # Store opened log file handler
    error_log_file_name = None
    error_log_filehandler = None
    # Store csv writer
    csv_writer = None
    # validation errors
    errors = {}
    is_file_opened = False

    def __init__(self, file_name):
        self.error_log_file_name = '..\\output\\raw_data_validation_errors\\' + \
            file_name

    # check if the pair field and field value is already in the log
    # if not add into the log
    def log(self, field, field_value):

        if not self.is_file_opened:
            self.error_log_filehandler = open(
                self.error_log_file_name, 'at', newline='')
            self.csv_writer = csv.writer(self.error_log_filehandler)
            self.csv_writer.writerow(['Field', 'Value'])
            self.is_file_opened = True

        # check is the field already in error log
        if field in self.errors.keys():

            # obtain know incorrect values
            known_errors = self.errors[field]

            # check is the value already in error log
            if field_value in known_errors:

                # if we know it, just return
                return

            # we don't know it, so add
            else:
                self.errors[field].append(field_value)

        # field is not in the error log, so add it with value
        else:
            self.errors[field] = [field_value]

    def close(self):

        if not self.is_file_opened:
            return

        # save collected values
        for field in self.errors.keys():
            for field_value in self.errors[field]:
                self.csv_writer.writerow([field, field_value])

        # save close logger file
        self.error_log_filehandler.close()

# ====================


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

                record_dict[headers[item]] = record[item]

            # adding file name to the each record
            record_dict["FILE"] = file_name

            # return record through the generator
            yield record_dict


def validate_money_field(record, logger):

    for field in money_fields:

        # Pension and salary have different set of fields. To keep this procedure universal
        # we don't care if some fields are not found, just skip iteration
        if field not in record.keys():
            continue

        field_value = record[field]

        # Let 'not provided' to pass. We will handle them at database level
        if field_value == 'Not Provided':
            continue

        # If value looks like 0.0 let it pass
        if re.match('\d+\.?\d*', field_value) != None:
            continue

        # If value is empty it is ok
        if field_value == '':
            continue

        # log all other values
        logger.log(field, field_value)

    return


def validate_year_field(record, logger):
    # See explanation of the algo in the validate_money_field

    for field in year_fields:
        if field not in record.keys():
            continue

        field_value = record[field]

        if field_value == '':
            continue

        if re.match('[1,2][9,0][0-9][0-9]', field_value) != None:
            return

        logger.log(field, field_value)

    return


def validating_error_log(file_name, field, field_value):
    '''If some validation fails, write the record in the aproppriate log file
    '''
    # TODO check existence of error log
    # if not exist- create new with headers
    # if exist - open write and close

    error_log_name = '..\\output\\raw_data_validation_errors\\' + \
        file_name


def get_record(file):
    '''Interface method for pipeline.

    Args:
    file[string]: full file name to read

    Returns: generator
    '''
    fo.check_file_exists(file, False)
    split_name = file.split('\\')
    file_name = (split_name[len(split_name) - 1])
    logger = validation_error_logger(file_name)

    records = read(file)
    for record in records:
        validate_money_field(record, logger)
        validate_year_field(record, logger)

        yield record

    logger.close()
