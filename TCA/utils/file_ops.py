import csv
import os
import re


# TODO: Document list_file, grammar check, add unit test
def list_files(directory="..\\raw_data\\"):
    """This function returns the sorted list of all csv files in a directory.

    It doesn't perform recursive subdirectory search.

    Args:
       directory(Optional[string]): Should be a path to the directory with
       the raw transparentCA data. It uses default project layout if
       there is no argument provided.

    Returns:
        Dictionary:
        key - year as integer
        value - list of full absolute csv filenames as string
    """
    full_path = os.path.realpath(directory)

    check_file_exists(full_path, True)
    csv_files = [name for name in os.listdir(full_path)
                 if name.endswith(".csv")]
    if len(csv_files) == 0:
        raise FileNotFoundError("Csv files haven't been found")

    year_matcher = re.compile("[0-9]{4}")

    result = {}
    year_list = []

    # iterate through the file list
    for name in csv_files:
        if year_matcher.search(name) != None:
            full_filename = full_path + "\\" + name
            year = int((year_matcher.search(name).group(0)))

            if year in result:
                year_list = result[year]
            else:
                year_list = []

            year_list += [full_filename]

            result[year] = year_list

    if len(result) == 0:
        raise FileNotFoundError("Suitable files haven't been found")

    return result


def read_headers(full_filename):
    """ Open given file as csv and return first line of the file
    
    Args:
        full_filename - absolute path to csv file

    Returns:
        Records of the first line of file as list of strings

    """

    check_file_exists(full_filename, False)
    with open(full_filename, "rt") as file:
        file_csv = csv.reader(file)
        headers = next(file_csv)
        return headers


def check_file_exists(full_path, is_directory):
    # TODO: Document it
    """ Check if given full_path exists and
    it is correct type of file system instance"""
    if not os.path.exists(full_path):
        raise FileNotFoundError("Path doesn't exist")

    if (is_directory) and (not os.path.isdir(full_path)):
        raise FileNotFoundError("Target is not a directory")

    if (not is_directory) and (os.path.isdir(full_path)):
        raise FileNotFoundError("Target is not a file")
