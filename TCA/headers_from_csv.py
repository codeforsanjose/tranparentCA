import csv

import utils.rawdata


try:
    with open("..\\output\\headers.csv", 'w') as ofile:
        ofile_csv = csv.writer(ofile)

        files = utils.rawdata.list_files()
        for year in files:
            for file in files[year]:
                name_split = file.split("\\")
                name = name_split[len(name_split) - 1]
                output = [name] + utils.rawdata.read_headers(file)
                ofile_csv.writerow(output)

except FileNotFoundError as e:
    print("Some error")
    print(e)
