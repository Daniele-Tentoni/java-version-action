import os
import unittest

from utils import delete_properties, write_properties
from versioner import get_java_version

test_dir_name = "tmp"

versions = [['8', '2.0'], ['9', '4.3'], ['10', '4.7'], ['11', '5.0'], ['12', '5.4'], ['13', '6.0'], ['14', '6.3'], ['15', '6.7'], ['16', '7.0'], ['17', '7.3']]

class JavaVersionTestCase(unittest.TestCase):

  def setUp(self):
    delete_properties()

  def test_java_version(self):
    for j_v, g_v in versions:
      # self.subTest(msg="Checking if p1 equals p2", p1=p1, p2=p2):
      with self.subTest():
        write_properties(g_v)
        self.assertEqual(get_java_version(), j_v)

  def test_arbitrary_version_in_another_path(self):
    os.makedirs(test_dir_name)
    write_properties("7.3", test_dir_name)
    self.assertEqual(get_java_version(), "17")

  def test_missing_file(self):
    # delete file
    delete_properties()
    with self.assertRaises(ValueError):
      get_java_version()

  def tearDown(self):
    delete_properties()
    if os.path.isdir(test_dir_name):
      os.rmdir(test_dir_name)

def suite():
  """
  Gather all the tests from this module in a test suite.
  """
  test_suite = unittest.TestSuite()
  test_suite.addTest(unittest.makeSuite(JavaVersionTestCase))
  return test_suite

if __name__ == '__main__':
  tests = suite()
  runner = unittest.TextTestRunner()
  runner.run(tests)
