'''
Miscellaneous scripts

@author: Maksim Habets
'''


def formatted_time(seconds_total):
    ''' convert number of seconds in the tuple (hours, minutes, seconds)
    '''
    minutes, seconds = divmod(seconds_total, 60)
    hours, minutes = divmod(minutes, 60)
    seconds = round(seconds)
    minutes = round(minutes)
    hours = round(hours)

    return (hours, minutes, seconds)
