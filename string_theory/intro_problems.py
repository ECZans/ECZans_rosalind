"""Solutions for intro problems!"""
import sys


def string_slice(input_string, indices):
    """
    Slice a subsequence bounded by (left, right) indices from the provided input string
    :param str input_string: Source string to be sliced
    :param list or tuple indices: Left- and right-hand zero-based indices bounding desired substring
    :return str: Substring
    """
    # We assume left index is zero-based but right index is not, therefore we add +1.
    return input_string[indices[0]:indices[1]+1]


if __name__ == '__main__':
    # Implementing a commandline argument parser is on to-do list
    print(string_slice(input_string=sys.argv[1], indices=sys.argv[2]))
