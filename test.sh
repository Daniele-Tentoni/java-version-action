#!/usr/bin/env bash

while getopts crx flag
do
    case "${flag}" in
        c) coverage=true;;
        r) report=true;;
        x) xml=true;;
    esac
done

if [[ $coverage = true ]]; then
  coverage run --source src -m unittest discover
fi
if [[ $report = true ]]; then
  coverage report
fi
if [[ $xml = true ]]; then
  coverage xml
fi
if [[ $coverage -ne true && $report -ne true ]]; then
  python3 -m unittest discover
fi
