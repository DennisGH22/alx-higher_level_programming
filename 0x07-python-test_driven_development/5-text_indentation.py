#!/usr/bin/python3
"""
Print text with two new lines after each of the characters
'.', '?', and ':'.
"""


def text_indentation(text):
    """
    Print text with two new lines after each of the characters
    '.', '?', and ':'.

    :param text: The input text (a string).
    :raises TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""

    for char in text:
        line += char

        if char in ('.', '?', ':'):
            print(line.strip(), end="")

            print()
            print()

            line = ""

    if line:
        print(line.strip())
