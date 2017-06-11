#!/usr/bin/env bash
rm -f test_cases/sample_output
rm -f test_cases/custom_output
cat test_cases/sample_input | python3 src/run.py > test_cases/sample_output
cat test_cases/custom_input | python3 src/run.py > test_cases/custom_output

