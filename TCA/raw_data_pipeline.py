'''
Read all raw data, deduplicate and load into database

@author: Maksim Habets
'''

import logging

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


# TODO Create database file if it isn't exist or open
# TODO Create collection of the raw_files_objects
# TODO Calculate signatures for the file
# TODO CHeck presense in the database
# TODO Divide raw data files to salary / pensions
# TODO Sort them by years
# TODO Load into pandas dataframes
# TODO Deduplicate
# TODO Add signatures for each record (source file with hashsum)
# TODO Put into database
# TODO Print statistics
# TODO Check raw_data_pipeline_old for the incorrect values, mappings, etc.
