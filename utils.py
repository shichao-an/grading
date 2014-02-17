from __future__ import print_function, unicode_literals, absolute_import
import csv
import re
from operator import itemgetter


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


def print_results(students):
    for student, grade in sorted(students.items(), key=itemgetter(1)):
        print(format(student, '11'), end=': ')
        print(format(grade, '2'))


def check_scripts(scripts):
    """
    :param scripts: a dictionary mapping netid to script path
    """
    for netid in scripts:
        print('=' * 80)
        print('[netid]', netid)
        print('[script]', "'", scripts[netid], "'", sep='')
        print()
        with open(scripts[netid], 'r') as f:
            print(f.read())
