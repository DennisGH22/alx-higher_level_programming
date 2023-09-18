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
        text = text.replace(i, i + "\n\n")

    print(text, end="")
