# content of test_sysexit.py
import filecmp
import pytest

from sequence_trimming_app import trimming

def test_trimming():
    input_file = "./tests/resources/sequence_sample.txt"
    output_file = "./tests/resources/output.txt"
    expected_output_file = "./tests/resources/expected_output.txt"
    trimming(input_file, output_file)
    assert filecmp.cmp(output_file, expected_output_file)

def test_bad_output():
    input_file = "./tests/resources/sequence_sample.txt"
    output_file = "./tests/resources/output.txt"
    expected_output_file = "./tests/resources/bad_output.txt"
    trimming(input_file, output_file)
    assert not filecmp.cmp(output_file, expected_output_file)
