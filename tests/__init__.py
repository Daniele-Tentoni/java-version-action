import glob
import os
import unittest
from unittest import runner
import src.main as main

versions = [['8', '2.0'], ['9', '4.3'], ['10', '4.7'], ['11', '5.0'], ['12', '5.4'], ['13', '6.0'], ['14', '6.3'], ['15', '6.7'], ['16', '7.0'], ['17', '7.3']]

properties_file_name = "gradle-wrapper.properties"
test_dir_name = "tmp"

def write_properties(gradle_version, tmp_path = ""):
  """Write gradle-wrapper.properties file

  Args:
      gradle_version (str): Gradle version to write
      tmp_path (str): Optional tmp_path
  """
  pre_path = os.path.join(".", tmp_path)
  file_path = os.path.join(pre_path, properties_file_name)
  with open(file_path, 'w') as f:
    f.write("version=" + gradle_version)
    
def delete_properties():
  """Delete gradle-wrapper.properties file.

  Args:
      tmp_path (str): Optional tmp_path
  """
  file_path = os.path.join(".", "**", "gradle-wrapper.properties")
  for file_name in glob.glob(file_path, recursive = True):
    if os.path.isfile(file_name):
      os.remove(file_name)
    else:
      print("Missing wrapper test file.")
  try:
    if os.path.isdir(test_dir_name):
      os.rmdir(test_dir_name)
  except FileNotFoundError:
    print("tmp dir not found")

class JavaVersionTestCase(unittest.TestCase):
  
  def setUp(self):
    delete_properties()
      
  def test_java_version(self):
    for j_v, g_v in versions:
      # self.subTest(msg="Checking if p1 equals p2", p1=p1, p2=p2):
      with self.subTest():
        write_properties(g_v)
        self.assertEqual(main.get_java_version(), j_v)
        
  def test_arbitrary_version_in_another_path(self):
    os.makedirs(test_dir_name)
    write_properties("7.3", test_dir_name)
    self.assertEqual(main.get_java_version(), "17")

  def test_missing_file(self):
    # delete file
    delete_properties()
    with self.assertRaises(ValueError):
      main.get_java_version()
      
  def tearDown(self):
    delete_properties()
    
def suite():
  """Gather all the tests from this module in a test suite.
  """
  test_suite = unittest.TestSuite()
  test_suite.addTest(unittest.makeSuite(JavaVersionTestCase))
  return test_suite

if __name__ == '__main__':
  tests = suite()
  runner = unittest.TextTestRunner()
  runner.run(tests)