#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argc = len(argv)
    s = 0
    if argc != 0:
        for i in range(argc):
            s += int(argv[i])

    print("{}".format(s))
