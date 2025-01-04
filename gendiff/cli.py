import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Diff two config files.')
    parser.add_argument('first_file', help='Path to the first file')
    parser.add_argument('second_file', help='Path to the second file')
    parser.add_argument('-f', '--format', help='out format', default="stylish")
    return parser.parse_args()
