import pytest
from gendiff.generate_diff import generate_diff


PLAIN = {
    'file1.json': 'tests/fixtures/file1.json',
    'file2.json': 'tests/fixtures/file2.json',
    'file1.yaml': 'tests/fixtures/file1.yaml',
    'file2.yaml': 'tests/fixtures/file2.yaml',
}

NESTED = {
    'file3.json': 'tests/fixtures/file3.json',
    'file4.json': 'tests/fixtures/file4.json',
}

RESULT = {
    'result1': 'tests/fixtures/result1_stylish.txt',
    'result2': 'tests/fixtures/result2_stylish.txt',
    'result3': 'tests/fixtures/result3_plain.txt',
    'result4': 'tests/fixtures/result4_plain.txt',
    'result5': 'tests/fixtures/result5_json.txt',
    'result6': 'tests/fixtures/result6_json.txt',
}


@pytest.mark.parametrize(
    'path1, path2, format, diff',
    [
        (PLAIN['file1.json'], PLAIN['file2.json'], 'stylish', RESULT['result1']),
        (PLAIN['file1.yaml'], PLAIN['file2.yaml'], 'stylish', RESULT['result1']),
        (NESTED['file3.json'], NESTED['file4.json'], 'stylish', RESULT['result2']),
        (NESTED['file3.json'], NESTED['file4.json'], 'plain', RESULT['result3']),
        (PLAIN['file1.json'], PLAIN['file2.json'], 'plain', RESULT['result4']),
        (PLAIN['file1.yaml'], PLAIN['file2.yaml'], 'plain', RESULT['result4']),
        (PLAIN['file1.yaml'], PLAIN['file2.yaml'], 'json', RESULT['result6']),
        (PLAIN['file1.json'], PLAIN['file2.json'], 'json', RESULT['result6']),
        (NESTED['file3.json'], NESTED['file4.json'], 'json', RESULT['result5']),
    ]
)
def test_generate_diff_1(path1, path2, format, diff):
    assert generate_diff(path1, path2, format) == open(diff).read()
