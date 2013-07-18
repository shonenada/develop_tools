import sys

from develop_tools.pep8 import pep8
from develop_tools.clean import clean
from develop_tools.search import search


permit_argvs = ['-c', 'clean', '-p', 'pep8', '-s', 'search', '-ss', 'ssearch']


def main():
    def print_info():
        print("clean (-c)\t\tremove *.pyc files.")
        print("pep8 (-c)\t\trun pep8 check.")
        print("search (-s)\t\tsearch partten in files, "
              "example: search ./ py|txt content")
        print("ssearch (-ss)\t\tadvance search partten in files, "
              "example: ssearch ./ ^[a-zA-Z0-9_]+\.(py|txt)& content")

    if len(sys.argv) <= 1 or not sys.argv[1] in permit_argvs:
        print_info()

    if len(sys.argv) > 1:
        for i in range(0, len(sys.argv) - 1):
            argv = sys.argv[i + 1]
            if argv == "-c" or argv == "clean":
                if len(sys.argv) > 2:
                    path = sys.argv[(i + 1) + 1]
                    clean(path)
                else:
                    clean()
            if argv == "-p" or argv == "pep8":
                if len(sys.argv) > 2:
                    path = sys.argv[(i + 1) + 1]
                    pep8(path)
                else:
                    pep8()
            if argv == '-s' or argv == 'search':
                path = sys.argv[(i + 1) + 1]
                suffix = sys.argv[(i + 1) + 2]
                content = sys.argv[(i + 1) + 3]
                file_pattern = r"^[a-zA-Z0-9_]+\.(" + suffix + ")$"
                search(path, file_pattern, content)
            if argv == '-ss' or argv == 'ssearch':
                path = sys.argv[(i + 1) + 1]
                file_pattern = sys.argv[(i + 1) + 2]
                content = sys.argv[(i + 1) + 3]
                search(path, file_pattern, content)


if __name__ == "__main__":
    main()
