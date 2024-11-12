import argparse
from gendiff.generate_diff import generate_diff


def main():
    parser = argparse.ArgumentParser(description='Diff two config files.')
    parser.add_argument('first_file', help='Path to the first JSON file')
    parser.add_argument('second_file', help='Path to the second JSON file')
    parser.add_argument('-f', '--format', help='out format', default="stylish")
    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
