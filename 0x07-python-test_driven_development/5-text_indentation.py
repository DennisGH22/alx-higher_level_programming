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

    delimiters = ".?:"

    for i in delimiters:
        text = (i + "\n\n").join(
            [line.strip(" ") for line in text.split(i)])

    print(text, end="")
