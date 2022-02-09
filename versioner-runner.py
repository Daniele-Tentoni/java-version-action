#!/usr/bin/env python3

import sys
from versioner.versioner import get_java_version

if __name__ == '__main__':
  version = get_java_version()
  # Output different if we are in github actions.
  if len(sys.argv) == 2 and sys.argv[1] == "ga":
    print(f"::set-output name=java-version::{version}")
  elif 'help' in sys.argv:
    print("usage: ./versioner-runner.py ga")
    print("Output the least Java version supported for the current Gradle wrapper.")
  else:
    print(version)
