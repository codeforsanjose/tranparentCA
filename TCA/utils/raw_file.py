'''


@author: Maksim Habets
'''

class RawFile(object):
    '''
    classdocs
    '''
    


    def __init__(self, year, full_name):
        '''
        Constructor
        '''
        self.year = year;
        self.full_name = full_name
        
        if ('pensions' in self.full_name):
            self.pension_file = True
        else:
            self.pension_file = False
    
    def get_pandas_dataframe(self):
        #TODO