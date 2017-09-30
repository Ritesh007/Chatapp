"""
Unit test case for accessFiles.py Library.
"""

import unittest
from Chatapp.utilities.accessFiles import AccessFiles
import os


# TODO write a successful testcase
class AccessFilestest(unittest.TestCase):

# every testcase functon name should start with test_

    def test_storetexts(self):
        AccessFiles.store_texts("\n This is a test line ---> ignore this \n")
        dir = os.path.dirname(__file__)
        filename = os.path.join(dir, '..\\files\\chat.txt')
        store_file = open(filename, "r")
        for i in store_file:
            if i == "This is a test line ---> ignore this":
              self.assertEqual(i,"This is a test line ---> ignore this")
              store_file.close()
              break
            return False
        store_file.close()


"""def main():
  accessfilestest = AccessFilestest()
  accessfilestest(runTest)

main()"""