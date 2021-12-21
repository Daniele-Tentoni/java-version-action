import glob
from os import path
import re
import requests
import sys

def fetch_gradle_compatibility(wrapper_version):
  """Return the Java Version compatible with given wrapper version.

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

def get_java_version():
  file_path = path.join(".", "**", "gradle-wrapper.properties")
  text_files = glob.glob(file_path, recursive = True)
  if len(text_files) != 1:
    raise ValueError("Too many or missing gradle-wrapper file")
  
  with open(text_files[0], 'r') as wrapper_content:
    content = wrapper_content.read()

  wrapper_re = re.compile(r'version=(\d*\.\d*)')
  wrapper_version = wrapper_re.findall(content)
  if len(wrapper_version) != 1:
    raise ValueError("Wrapper version not found", wrapper_version)
  
  return fetch_gradle_compatibility(wrapper_version[0])

if __name__ == '__main__':
  version = get_java_version()
  if len(sys.argv) == 2 and sys.argv[1] == "ga":
    print(f"::set-output name=java-version::{version}")
  else:
    print(version)
