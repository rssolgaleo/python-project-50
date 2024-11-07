import pytest
from gendiff.generate_diff import generate_diff


PLAIN = {
    'file1.json': 'tests/fixtures/file1.json',
    'file2.json': 'tests/fixtures/file2.json',
}

RESULT = {
    'result1': 'tests/fixtures/result_json.txt'
}


@pytest.mark.parametrize(
    'path1, path2, diff',
    [
        (PLAIN['file1.json'], PLAIN['file2.json'], RESULT['result1'])
    ]
)
def test_generate_diff(path1, path2, diff):
    assert generate_diff(path1, path2) == open(diff).read()
