#!/usr/bin/python3

import sys


def main():
    if len(sys.argv[1:]) != 2:
        print("Usage: %s arg1 arg2" % sys.argv[0])
        sys.exit(1)

    print(f"{sys.argv[0]} {sys.argv[1]} {sys.argv[2]}")


if __name__ == "__main__":
    main()
