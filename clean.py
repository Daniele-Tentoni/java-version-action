#!/usr/bin/env python3

import os

files_to_delete = [".coverage", "coverage.xml"]

for file in files_to_delete:
  try:
    os.remove(file)
  except OSError as e:
    print(f"Error: {file}: {e.strerror}")

directories_to_delete = ["tmp", "htmlcov"]
for dir_path in directories_to_delete:
  try:
    os.rmdir(dir_path)
  except OSError as e:
    print(f"Error: {dir_path}: {e.strerror}")
