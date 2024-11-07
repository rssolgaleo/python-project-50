import argparse


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file', help=' ')
    parser.add_argument('second_file', help=' ')
    parser.add_argument('-f', '--format', help='set format of output', default="stylish")
    return parser.parse_args()


if __name__ == "__main__":
    main()
