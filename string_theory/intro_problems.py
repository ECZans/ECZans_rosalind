import os
import sys


def string_slice(input_string, indices):
    """
    Slice a subsequence bounded by (left, right) indices from the provided input string

    :param str input_string: Source string to be sliced
    :param list or tuple indices: Left- and right-hand zero-based indices bounding desired substring
    :return str: Substring
    """
    return input_string[indices[0]:indices[1]+1]


def calc_hypotenuse(a, b):
    """
    Given two integers, calculate the square hypotenuse of the right triangle
    with legs corresponding to a and b

    :param int a: Side of right triangle
    :param int b: Side of right triangle
    :return int: Hypotenuse squared
    """
    if a >= 1000 or b >= 1000:
        raise ValueError('Expected input integers < 1000 but got ({}, {})'.format(a, b))
    return (a ** 2) + (b ** 2)


def even_numbered_lines(input_file, output_file, append=False):
    """
    Read in an input file and write/append even-numbered lines to the specified
    output file

    :param output_file:
    :param append:
    :param str input_file: Path to input text file
    """
    with open(input_file) as filehandle:
        input_lines = filehandle.readlines()
    if not append or not os.path.exists(output_file):
        output_fh = open(output_file, 'w')
    else:
        output_fh = open(output_file, 'a')
    for line_counter in range(0, len(input_lines), 2):
        output_fh.write(input_lines[line_counter])

    output_fh.close()


def dict_word_counter(input_string):
    """
    Count ocurrences of words in a string < 10000 characters exhaustively by iteratively adding to
    counters stored as dict values
    :param input_string:
    :return:
    """
    if len(input_string) > 10000:
        raise ValueError('Input length may not exceed 10000 characters, got {}'.format(len(input_string)))

    list_of_words = input_string.split()

    output_dict = {}

    for word in list_of_words:
        if word not in output_dict:
            output_dict[word] = 1
        else:
            output_dict[word] += 1
    return output_dict


def sum_odds_from_range(a, b):
    """
    Sum all odd integers in range bounded by positive integers [a, b] given a < b < 10000
    :param int a: Positive integer defining lower bound of range
    :param int b: Positive integer defining upper bound of range
    :return int: Sum of odd integers between a and b
    """
    if not a < b < 10000:
        raise ValueError('Expected a < b < 10000 but got a={}, b={}'.format(a, b))
    if a < 0 or b < 0:
        raise ValueError('Expected positive integers but got a={}, b={}'.format(a, b))
    odd_numbers = (num for num in range(a, b) if num % 2 == 1)
    return sum(odd_numbers)


if __name__ == '__main__':
    print(string_slice(input_string=sys.argv[1], indices=[sys.argv[2], sys.argv[3]]))
