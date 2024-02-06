#!/usr/bin/python3
"""
Module defines a function that inserts a line of text to a file,
after each line containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string.
    """
    content = ""
    with open(filename, encoding='utf-8') as f:
        for line in f:
            content += line
            if search_string in line:
                content += new_string
    with open(filename, "w", encoding='utf-8') as f:
        f.write(content)
