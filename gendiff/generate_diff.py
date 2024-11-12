from gendiff.parser import parse
from gendiff.build_gendiff_tree import build_gendiff_tree
from gendiff.formatters.__init__ import diff_formatter


def generate_diff(file_path1, file_path2, format='stylish'):
    file1 = parse(file_path1)
    file2 = parse(file_path2)
    diff = build_gendiff_tree(file1, file2)
    return diff_formatter(diff, format)
