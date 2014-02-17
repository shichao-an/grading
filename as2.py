#!/usr/bin/env python
from __future__ import print_function, unicode_literals, absolute_import

# Check Python version
import sys
if sys.version_info[0] < 3:
    raise Exception('Must use Python 3.')
import os
import subprocess
import unittest
from utils import get_netid_from_dirname, build_students, print_results


ASSIGNMENT_NAME = '../Input, format, print'  # Directory name
GRADES_CSV = 'grades.csv'
STUDENTS = {}
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
                        popen = subprocess.Popen(['python3', script],
                                                 stdin=subprocess.PIPE,
                                                 stdout=subprocess.PIPE)
                        _output, _ = popen.communicate(bytes('Andrew\n20\n',
                                                             'utf-8'))
                        output = _output.decode('utf-8')
                        try:
                            assert 'Andrew' in output
                            assert '40' in output
                            self.students[netid] = FULL_MARK
                        except AssertionError:
                            print(output)
                    except subprocess.CalledProcessError:
                        pass

    def tearDown(self):
        global STUDENTS
        STUDENTS = self.students


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestAssignment("test_results"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    print_results(STUDENTS)
