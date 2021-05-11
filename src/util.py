import os
import csv

def exist_file(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)

def write_value(file_path, list_value):
    exist_file(file_path)
    with open(file_path, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["key", "propety", "value"])
        writer.writerows(list_value)