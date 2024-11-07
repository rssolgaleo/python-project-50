import argparse


def main():
    parser = argparse.ArgumentParser(description='Diff two config files.')
    parser.add_argument('first_file', help=' ')
    parser.add_argument('second_file', help=' ')
    parser.add_argument('-f', '--format', help='out format', default="stylish")
    return parser.parse_args()


if __name__ == "__main__":
    main()
