#!/usr/bin/env python
from __future__ import print_function, unicode_literals, absolute_import

# Check Python version
import sys
if sys.version_info[0] < 3:
    raise Exception('Must use Python 3.')
import os
import scripttest
import unittest
from utils import (get_netid_from_dirname, build_students, print_results,
                   check_scripts)


ASSIGNMENT_NAME = '../Bleep Bloop'  # Directory name
GRADES_CSV = 'grades.csv'
STUDENTS = {}
GOOD_SCRIPTS = {}
BAD_SCRIPTS = {}
OUTPUTS = {}
FULL_MARK = 10
_d = os.path.join(os.path.dirname(__file__), ASSIGNMENT_NAME)
target = os.path.abspath(_d)


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
                    try:
                        output = ''  # Clear output in case error
                        env = scripttest.TestFileEnvironment('./test-output',
                                                             split_cmd=False)
                        res = env.run('python3', script)
                        output = res.stdout
                        OUTPUTS[netid] = output
                        self.students[netid] = FULL_MARK

                        lines = output.rstrip('\n').split('\n')
                        # import pdb
                        # pdb.set_trace()
                        for i, line in enumerate(lines, 1):
                            # pdb.set_trace()
                            if i % 3 == 0 and i % 5 == 0:
                                assert line == 'BleepBloop'
                            elif i % 3 == 0:
                                assert line == 'Bleep'
                            elif i % 5 == 0:
                                assert line == 'Bloop'
                            else:
                                assert line == '%d' % i
                        assert len(lines) == 123
                        GOOD_SCRIPTS[netid] = script
                    except:
                        # AssertionError and other exception
                        print('-' * 80)
                        print("'", script, "'", sep='')
                        #print('Output of %s' % netid)
                        #print(output)
                        print('=' * 80)
                        print('Code of %s' % netid)
                        with open(script, 'r') as f:
                            print(f.read())
                        self.students[netid] = 0
                        BAD_SCRIPTS[netid] = script

    def tearDown(self):
        global STUDENTS
        STUDENTS = self.students


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignment)
    runner = unittest.TextTestRunner()
    runner.run(suite)
    print_results(STUDENTS)
    check_scripts(GOOD_SCRIPTS)
    #for netid in OUTPUTS:
        #print('[netid]', netid)
        #print(OUTPUTS[netid])
    print('*' * 80)
    check_scripts(BAD_SCRIPTS)
