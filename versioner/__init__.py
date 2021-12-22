import glob
from os import path
import re
import requests
import sys

def fetch_gradle_compatibility(wrapper_version):
  """
  Return the Java Version compatible with given wrapper version.

  Args:
      wrapper_version (double): the current wrapper version.

  Raises:
      ValueError: Gradle versions number different from Java versions number.
      ValueError: Gradle version not recognized.

  Returns:
      double: Java version returned.
  """
  url = 'https://docs.gradle.org/current/userguide/compatibility.html'
  r = requests.get(url, allow_redirects=True).text
  java_re = re.compile(r'<td class=\"tableblock halign-left valign-top\"><p class=\"tableblock\">(\d*)</p>')
  java_versions = java_re.findall(r)
  gradle_re = re.compile(r'<td class=\"tableblock halign-left valign-top\"><p class=\"tableblock\">(\d*\.\d*)</p></td>')
  gradle_versions = gradle_re.findall(r)
  if len(java_versions) != len(gradle_versions):
    raise ValueError()

  try:
    i = gradle_versions.index(wrapper_version)
    return java_versions[i]
  except ValueError:
    raise ValueError("Gradle version not recognized")

def find_wrapper_file() -> str:
  """
  Return a list of paths matching the gradle-wrapper.properties file name.

  Raises:
      ValueError: Too many or missing gradle-wrapper.properties files.

  Returns:
      str: Path to the found gradle-wrapper.properties file.
  """
  file_path = path.join(".", "**", "gradle-wrapper.properties")
  text_files = glob.glob(file_path, recursive = True)
  if len(text_files) != 1:
    raise ValueError("Too many or missing gradle-wrapper file", text_files)
  print("Found wrapper in", text_files[0])
  return text_files[0]

def get_wrapper_version():
  wrapper_file = find_wrapper_file()
  read_mode = 'r'
  with open(wrapper_file, read_mode) as wrapper_content:
    content = wrapper_content.read()

  # Search for the line where is defined the distribution url
  wrapper_re = re.compile(r'distributionUrl=.*-(\d*\.\d*).*\.zip')
  wrapper_version = wrapper_re.search(content)
  if wrapper_version == None:
    raise ValueError("Wrapper version not found")

  return wrapper_version.group(1)

def get_java_version():
  wrapper_version = get_wrapper_version()
  # Here we are sure to have the wrapper version
  return fetch_gradle_compatibility(wrapper_version)

if __name__ == '__main__':
  version = get_java_version()
  # Output different if we are in github actions.
  if len(sys.argv) == 2 and sys.argv[1] == "ga":
    print(f"::set-output name=java-version::{version}")
  else:
    print(version)
