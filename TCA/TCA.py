'''
Read all raw data, deduplicate and load into database

@author: Maksim Habets
'''

import logging

import pandas as pd
import utils.file_ops as fo
import utils.raw_file as rf


# set up logging system
logger = logging.getLogger("raw_data_pipeline")
logger.setLevel(logging.DEBUG)

# create file handler
fh = logging.FileHandler('debug.log')
fh.setLevel(logging.DEBUG)

# create console handler
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


# TODO: Create database file if it isn't exist or open
#database = database()
# TODO: Create collection of the raw_files_objects

# TODO: Calculate signatures for the file - should be done by file object
# TODO: CHeck presense in the database - should be done by database object
# TODO: Divide raw data files to salary / pensions - should be done by file
# object

# TODO: Load into pandas dataframes - should be done in file object

# build the list of the full file names
all_files_list = fo.all_files()
logger.info("All files: " + str(all_files_list))
# create empty data frames
salary_frame = pd.DataFrame
pension_frame = pd.DataFrame

# load data to the dataframes
for file_name in all_files_list:
    logger.debug('File name: ' + str(file_name))
    raw_file = rf.RawFile(file_name)  # TODO: How to import without prefix

    if raw_file.pension_file:
        pension_frame = pd.concat(
            objs=[pension_frame, raw_file.get_pandas_dataframe()])
        logger.debug('Pension')
    else:
        salary_frame = pd.concat(
            objs=[salary_frame, raw_file.get_pandas_dataframe()])
        logger.debug('Salary')

logger.info('Finished iteration')
# TODO: Extract column set into configuration
salary_frame.drop_duplicates(['Employee Name', 'Job Title', 'Base Pay', 'Overtime Pay',
                              'Other Pay', 'Benefits', 'Total Pay',
                              'Total Pay & Benefits', 'Year'], inplace=True)  # Inplace should be true or it retruns not duplicated set
# TODO: Deduplicate -pension frame

salary_frame.to_csv(('..\\output\\consolidated_salary.csv'))

# TODO: Add signatures for each record (source file with hashsum)
# TODO: Put into database
# TODO: Print statistics
# TODO: Check raw_data_pipeline_old for the incorrect values, mappings, etc.
