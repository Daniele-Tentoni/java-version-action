#!/usr/bin/env bash

# Get Options:
# c) execute coverage
# r) produce report
# x) produce xml
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

if [[ -z ${coverage+x} && -z ${report+x} && -z ${xml+x} ]]; then
  python3 -m unittest discover
fi
