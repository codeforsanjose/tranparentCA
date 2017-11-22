'''


@author: Maksim Habets
'''
import re

import pandas as pd

import utils.config as config


class RawFile(object):
    '''
    classdocs
    '''

    def __init__(self, full_name):
        '''
        Constructor
        '''

        self.full_name = full_name
        year_pattern = re.compile('20[0-2][0-9]')
        year = year_pattern.match(full_name)
        if year == None:
            # TODO: Use more appropriate exception
            raise IOError('Unable to detect year of the file')
        else:
            self.year = year

        if ('pensions' in self.full_name):
            self.pension_file = True
        else:
            self.pension_file = False

    def get_pandas_dataframe(self):
        if self.pension_file:
            return pd.read_csv(self.full_name, dtype=config.COLUMN_DATA_TYPES,
                               na_values=config.ERROR_VALUES, header=0, names=config.PENSION_COLUMN_NAMES)
        else:
            return pd.read_csv(self.full_name, dtype=config.COLUMN_DATA_TYPES,
                               na_values=config.ERROR_VALUES, header=0, names=config.SALARY_COLUMN_NAMES)
