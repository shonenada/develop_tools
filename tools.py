import sys

from develop_tools.pep8 import pep8
from develop_tools.clean import clean


permit_argvs = ['-c', 'clean', '-p', 'pep8']


def main():
    def print_info():
        print("-c\t\tremove *.pyc files.")
        print("clean\t\tremove *.pyc files.")
        print("-p\t\trun pep8 check.")
        print("pep8\t\trun pep8 check.")

    if len(sys.argv) <= 1 or not sys.argv[1] in permit_argvs:
        print_info()

    if len(sys.argv) > 1:
        for i in range(0, len(sys.argv) - 1):
            argv = sys.argv[i + 1]
            if argv == "-c" or argv == "clean":
                clean()
            if argv == "-p" or argv == "pep8":
                pep8()


if __name__ == "__main__":
    main()
