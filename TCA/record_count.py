''' Utility script to measure pipeline efficiency and verify
    that all the records can be processed.
    Script reads all records from all files, count them and
    print results along with time of processing
    
    # TODO: Outdated and can be deleted
    '''

import time

import utils.file_ops as fo
import utils.misc as misc
import utils.raw_data_pipeline_old as pipeline


def stats_print(filename, stats):
    '''Print formatted string with filename and time in (h:m:s) format
    '''

    hour = stats[1][0]
    minutes = stats[1][1]
    seconds = stats[1][2]
    print('{:<35} # {:>18} # {:02d}:{:02d}:{:02d}'.format(
        filename, stats[0], hour, minutes, seconds))

# read all files
result = fo.all_files()

# remember start time for time of reading all files
total_start_time = time.time()

# counter for records from all files
total_records = 0

# statistics dictionary
stats = {}

# print header for result table
print('{:^35} # {:^18} # {:^10}'.format(
    'File name', 'Numb. of records', 'Time'))

# just read the all records in each file, count them and measure time of
# reading
for file in result:

    # get the file name itself
    split_name = file.split('\\')
    file_name = (split_name[len(split_name) - 1])

    # read records, count them and measure time
    records = pipeline.get_record(file)
    file_records = 0
    file_start_time = time.time()
    for rec in records:
        file_records += 1
    file_end_time = time.time()
    total_records += file_records
    duration = misc.formatted_time(file_end_time - file_start_time)

    # put result in the statistics collector
    stats[file_name] = (file_records, duration)
    stats_print(file_name, (file_records, duration))

total_end_time = time.time()
total_duration = misc.formatted_time(total_end_time - total_start_time)

stats["Total"] = (total_records, total_duration)
print("=================")
stats_print('TOTAL', stats["Total"])
