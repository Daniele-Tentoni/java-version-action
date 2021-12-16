import glob
from os import path
import re
import requests

def get_java_version():
  file_path = path.join(".", "**", "gradle-wrapper.properties")
  text_files = glob.glob(file_path, recursive = True)
  if len(text_files) != 1:
    raise ValueError("Too many or missing gradle-wrapper file")
  
  with open(text_files[0], 'r') as wrapper_content:
    content = wrapper_content.read()

  url = 'https://docs.gradle.org/current/userguide/compatibility.html'
  r = requests.get(url, allow_redirects=True).text
  java_re = re.compile(r'<td class=\"tableblock halign-left valign-top\"><p class=\"tableblock\">(\d*)</p>')
  java_versions = java_re.findall(r)
  gradle_re = re.compile(r'<td class=\"tableblock halign-left valign-top\"><p class=\"tableblock\">(\d*\.\d*)</p></td>')
  gradle_versions = gradle_re.findall(r)
  
  if len(java_versions) != len(gradle_versions):
    raise ValueError()
  
  wrapper_re = re.compile(r'version=(\d*\.\d*)')
  wrapper_version = wrapper_re.findall(content)
  if len(wrapper_version) != 1:
    raise ValueError("Wrapper version not found", wrapper_version)
    
  try:
    i = gradle_versions.index(wrapper_version[0])
    return java_versions[i]
  except ValueError:
    raise ValueError("Gradle version not recognized")

if __name__ == '__main__':
  print(get_java_version())