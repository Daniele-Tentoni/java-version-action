import glob
from os import path
import re
import requests

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
  """java_re = re.compile(r'<td class=\".*\"><p class=\".*\">(\d*)</p></td>')
  java_versions = java_re.findall(r)
  gradle_re = re.compile(r'<td class=\"tableblock halign-left valign-top\"><p class=\"tableblock\">(\d*\.\d*)</p></td>')
  gradle_versions = gradle_re.findall(r)
  """
  java_gradle_re = re.compile(r'<td class=\".*\"><p class=\".*\">(\d*)</p></td>\s<td class=\".*\"><p class=\".*\">(\d*\.\d*)</p></td>')
  java_gradle_versions = java_gradle_re.findall(r)
  # if len(java_versions) != len(gradle_versions):
    # raise ValueError(f"Java Versions {java_versions}, Gradle Versions {gradle_versions}")

  for (e1, e2) in java_gradle_versions:
    if e2 == wrapper_version:
      return e1
  raise ValueError("Gradle version not recognized")
    # return java_gradle_versions.
    # i = gradle_versions.index(wrapper_version)
    # return java_versions[i]

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
  # print("Found wrapper in", text_files[0])
  return text_files[0]

def get_wrapper_version():
  wrapper_file = find_wrapper_file()
  read_mode = 'r'
  with open(wrapper_file, read_mode) as wrapper_content:
    content = wrapper_content.read()
  # print("Contents", content)

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