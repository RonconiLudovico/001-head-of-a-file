import unittest
import subprocess

class Test01(unittest.TestCase):
    def test_standard_ten_lines(self):
        '''
        Here we will test the basic functioning of the script, printing the first ten lines of the file
        '''

        result = subprocess.check_output(["python3", "script.py", "example.txt"], text=True)
        data = f"Line 1: This is the first line.\nLine 2: This is the second line.\nLine 3: This is the third line.\nLine 4: This is the fourth line.\nLine 5: This is the fifth line.\nLine 6: This is the sixth line.\nLine 7: This is the seventh line.\nLine 8: This is the eighth line.\nLine 9: This is the ninth line.\nLine 10: This is the tenth line.\n"
        self.assertEqual(result, data)


class Test02(unittest.TestCase):
    def test_num_lines(self):
        '''
        Here we will test the basic functioning of the script, printing the first ten lines of the file
        '''

        result = subprocess.check_output(["python3", "script.py", "-n", "5", "example.txt"], text=True)
        data = f"Line 1: This is the first line.\nLine 2: This is the second line.\nLine 3: This is the third line.\nLine 4: This is the fourth line.\nLine 5: This is the fifth line.\n"
        self.assertEqual(result, data)


class Test03(unittest.TestCase):
    def test_num_lines_with_header(self):
        '''
        Here we will test the basic functioning of the script, printing the first ten lines of the file
        '''

        result = subprocess.check_output(["python3", "script.py", "-v", "-n", "5", "example.txt"], text=True)
        data = f"====> example.txt <====\nLine 1: This is the first line.\nLine 2: This is the second line.\nLine 3: This is the third line.\nLine 4: This is the fourth line.\nLine 5: This is the fifth line.\n"
        self.assertEqual(result, data)
