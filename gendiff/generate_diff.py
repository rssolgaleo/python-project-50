from gendiff.parser import parse
from gendiff.build_gendiff_tree import build_gendiff_tree
from gendiff.formatters.__init__ import diff_formatter


def generate_diff(path1: str, path2: str, format: str = 'stylish') -> dict:
    file1 = parse(path1)
    file2 = parse(path2)
    diff = build_gendiff_tree(file1, file2)
    return diff_formatter(diff, format)
