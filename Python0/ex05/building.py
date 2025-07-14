import sys

argc = len(sys.argv)
argv = sys.argv


def count_characters(text):
    """Counts the number of upper, lower, punctuation, spaces, and digit
    characters.

    Args:
        text: The text to analyze.
    """
    upper = 0
    lower = 0
    punctuation = 0
    spaces = 0
    digit = 0
    for char in text:
        if char.isupper():
            upper += 1
        if char.islower():
            lower += 1
        if (
            ord(char) in range(33, 48)
            or ord(char) in range(58, 65)
            or ord(char) in range(91, 97)
            or ord(char) in range(123, 127)
        ):
            punctuation += 1
        if char.isspace():
            spaces += 1
        if char.isdigit():
            digit += 1
    print(f"The text contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digit} digits")


def main():
    """Analyzes text provided as a command-line argument or standard input."""
    if argc > 2:
        print("AssertionError: more than one argument is provided")
        exit(1)
    elif argc < 2:
        print("What is the text to count?")
        text = sys.stdin.read()
    else:
        text = argv[1]

    count_characters(text)


if __name__ == "__main__":
    main()
