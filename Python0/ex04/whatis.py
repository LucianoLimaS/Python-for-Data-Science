import sys

argc = len(sys.argv)
argv = sys.argv

if __name__ == "__main__":
    if argc < 2:
        exit(1)
    if argc != 2:
        print("AssertionError: more than one argument is provided")
        exit(1)
    try:
        argv[1] = int(argv[1])
    except ValueError:
        print("AssertionError: argument is not an integer")
        exit(1)

    if argv[1] % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
    exit(0)
