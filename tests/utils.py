import glob
import os

properties_file_name = "gradle-wrapper.properties"
test_dir_name = "tmp"

def write_properties(gradle_version, tmp_path = ""):
  """
  Write gradle-wrapper.properties file

  Args:
      gradle_version (str): Gradle version to write
      tmp_path (str): Optional tmp_path
  """
  pre_path = os.path.join(".", tmp_path)
  file_path = os.path.join(pre_path, properties_file_name)
  with open(file_path, 'w') as f:
    f.write(f"distributionUrl=https\://services.gradle.org/distributions/gradle-{gradle_version}.2-bin.zip")

def delete_properties():
  """
  Delete gradle-wrapper.properties file.

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
    # Search all test dir and sort them from the deepest.
    dirs=glob.glob(os.path.join("**", test_dir_name), recursive=True)
    dirs.sort(reverse=True)

    # Now we can delete them.
    for dir_name in dirs:
      if os.path.isdir(dir_name):
        os.removedirs(dir_name)
  except FileNotFoundError:
    print("tmp dir not found")
