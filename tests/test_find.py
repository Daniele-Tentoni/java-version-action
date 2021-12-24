import os
import unittest

from utils import delete_properties, write_properties
from versioner import find_wrapper_file

test_dir_name: str = "tmp"

class TestFindWrapperFile(unittest.TestCase):
  def setUp(self) -> None:
    delete_properties()
    return super().setUp()

  def test_without_files(self):
    with self.assertRaises(ValueError):
      find_wrapper_file()

  def test_only_one_file(self):
    write_properties("some")
    file = find_wrapper_file()
    self.assertEqual(file, "./gradle-wrapper.properties")

  def test_many_files(self):
    os.makedirs(test_dir_name)
    write_properties("7.3", test_dir_name)
    second_dir_name: str = os.path.join(test_dir_name, test_dir_name)
    os.makedirs(second_dir_name)
    write_properties("7.3", second_dir_name)
    with self.assertRaises(ValueError):
      find_wrapper_file()

  def tearDown(self) -> None:
    delete_properties()
    return super().tearDown()

def suite():
  suite = unittest.TestSuite()
  suite.addTest(TestFindWrapperFile("test_without_files"))
  suite.addTest(TestFindWrapperFile("test_many_files"))
  return suite

if __name__ == '__main__':
  runner = unittest.TextTestRunner()
  runner.run(suite())