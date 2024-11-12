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
    'result1': 'tests/fixtures/result1.txt',
    'result2': 'tests/fixtures/result2.txt',
}


@pytest.mark.parametrize(
    'path1, path2, diff',
    [
        (PLAIN['file1.json'], PLAIN['file2.json'], RESULT['result1']),
        (PLAIN['file1.yaml'], PLAIN['file2.yaml'], RESULT['result1']),
        (NESTED['file3.json'], NESTED['file4.json'], RESULT['result2']),
    ]
)
def test_generate_diff(path1, path2, diff):
    assert generate_diff(path1, path2) == open(diff).read()
