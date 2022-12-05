#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv) - 1
    if i == 0:
        print("{} arguments.".format(i))
    elif i == 1:
        print("{} argument:".format(i))
    else:
        print("{} arguments:".format(i))

    if i >= 1:
        count = 0
        for arg in sys.argv:
            if i != 0:
                print("{}: {}".format(count, arg))
            count += 1
