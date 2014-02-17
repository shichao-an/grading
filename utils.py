import csv
import re


def get_netid_from_dirname(dirname):
    m = re.search('\(([a-z]+[0-9]+)\)', dirname)
    if m:
        return m.group(1)


def build_students(filename, students):
    """
    :param filename: absolute path to the CSV file
    :param students: dictionary of students
    """
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
        for i, row in enumerate(data):
            if len(row) > 0:
                if re.search('^[a-z]+[0-9]+$', row[0]):
                    netid = row[0]
                    students[netid] = -1
