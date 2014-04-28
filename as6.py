#!/usr/bin/env python
from __future__ import print_function, unicode_literals, absolute_import

# Check Python version
import sys
if sys.version_info[0] < 3:
    raise Exception('Must use Python 3.')
import os
import json
import scripttest
import unittest
import pdb
from utils import (get_netid_from_dirname, build_students, print_results)


ASSIGNMENT_NAME = '../Consonants and Vowels-2'  # Directory name
GRADES_CSV = 'grades.csv'
STUDENTS = {}
GOOD_SCRIPTS = {}
BAD_SCRIPTS = {}
OUTPUTS = {}
FULL_MARK = 10
_d = os.path.join(os.path.dirname(__file__), ASSIGNMENT_NAME)
target = os.path.abspath(_d)
with open('sas6-json.txt') as f:
    sas6 = json.loads(f.read())
    SAS6 = [x for row in sas6 for x in row]


class TestAssignment(unittest.TestCase):

    def setUp(self):
        """Read CSV file and build the student list"""
        filename = os.path.join(target, GRADES_CSV)
        print(filename)
        assert os.path.exists(filename)
        # self.students mapped netids to status
        # -1: not submitted
        # n: grade
        self.students = {}
        build_students(filename, self.students)

    def test_results(self):
        for dirpath, dirnames, filenames in os.walk(target):
            for filename in filenames:
                ext = os.path.splitext(filename)[1]
                if ext == '.py':
                    netid = get_netid_from_dirname(dirpath)
                    assert netid in self.students
                    self.students[netid] = 0
                    script = os.path.join(dirpath, filename)
                    passed_assert = False
                    try:
                        output = ''  # Clear output in case error
                        env = scripttest.TestFileEnvironment('./test-output',
                                                             split_cmd=False)
                        res = env.run('python3', script)
                        output = res.stdout
                        OUTPUTS[netid] = output
                        self.students[netid] = FULL_MARK
                        for word in SAS6:
                            assert word in output
                        passed_assert = True
                    except:
                        # AssertionError and other exception
                        BAD_SCRIPTS[netid] = script
                    print(netid)
                    print("'", script, "'", sep='', end='\n')
                    print('Passed Assert', passed_assert)
                    print(output)
                    print('*' * 79)
                    pdb.set_trace()

    def tearDown(self):
        global STUDENTS
        STUDENTS = self.students


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignment)
    runner = unittest.TextTestRunner()
    runner.run(suite)
    print_results(STUDENTS)
