"""Solutions for intro problems!"""
import collections
import os
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


def calc_hypotenuse(a, b):
    """
    Given two integers, calculate the square hypotenuse of the right triangle
    with legs corresponding to a and b

    :param int a: Side of right triangle
    :param int b: Side of right triangle
    :return int: Hypotenuse squared
    """
    # Do no work if we violate assumption that inputs are < 1000
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
    # By using 'with' we create a temporary filehandle that'll automatically close as soon
    # as sub-block is complete
    with open(input_file) as filehandle:
        input_lines = filehandle.readlines()

    # Alternative file operation, with handle that should be manually closed
    if not append or not os.path.exists(output_file):
        # Write mode (destructive)
        output_fh = open(output_file, 'w')
    else:
        # Append mode (non-destructive)
        output_fh = open(output_file, 'a')

    # Range arguments are (start, stop, step)
    for line_counter in range(0, len(input_lines), 2):
        output_fh.write(input_lines[line_counter])

    # Close output filehandle
    output_fh.close()


def dict_word_counter(input_string):
    """
    Count ocurrences of words in a string < 10000 characters exhaustively by iteratively adding to
    counters stored as dict values
    :param input_string:
    :return:
    """
    # Do no work if expectation of <= 10000 character input is violated
    if len(input_string) > 10000:
        raise ValueError('Input length may not exceed 10000 characters, got {}'.format(len(input_string)))

    # str.split arg (delimiter) defaults to 'all whitespace characters'
    list_of_words = input_string.split()

    # Store results
    output_dict = {}

    for word in list_of_words:
        if word not in output_dict:
            output_dict[word] = 1
        else:
            output_dict[word] += 1

    # I said 'exhaustively' in docstring because we can save 4 lines of code (okay, not that exhaustive)
    # by using Counter (or defaultdict) objects from the 'collections' package (which you can install by running
    # 'pip install collections' on command-line) as an alternative to builtin dict. They come with snazzy
    # convenience methods like Counter's most_common. I mean, look at this beautiful thing.
    # Collections changed a fair bit from python2 -> python3, though, which can be a hassle, and there's nothing
    # wrong with sticking with builtins.
    # word_counter = collections.Counter([list_of_words])

    return output_dict


def sum_odds_from_range(a, b):
    """
    Sum all odd integers in range bounded by positive integers [a, b] given a < b < 10000
    :param int a: Positive integer defining lower bound of range
    :param int b: Positive integer defining upper bound of range
    :return int: Sum of odd integers between a and b
    """
    # Do no work if input is not a < b < 10000
    if not a < b < 10000:
        raise ValueError('Expected a < b < 10000 but got a={}, b={}'.format(a, b))
    # Do no work if a or b is negative
    if a < 0 or b < 0:
        raise ValueError('Expected positive integers but got a={}, b={}'.format(a, b))

    # Many strategies are possible, 4 described below.

    # Demonstrating generators and list comprehension here as an alternative to the for loop.

    # Here is an 'exhaustive' option - while loop with counter
    # sum = 0
    # while a <= b:
    #   if a % 2 == 1:
    #       sum += a
    #   a += 1

    # Note: had this -
    # while a <= b:
    #   a += 1
    #   if a % 2 == 1:
    #       sum += a
    # previously. What's wrong with with this version?

    # Here is an example of list comprehension with modulo. List comprehension is
    # faster than a for loop in some scenarios (but slower in others). This iterates over
    # an iterable (or generator, in this case) object much like a for-loop, but builds a list
    # dynamically as it goes. Note that range() returns a generator - more on that below.
    # odd_numbers = [num for num in range(a, b) if num % 2 == 1]

    # This is doing the same thing as above - and while it looks like we're creating a tuple,
    # by doing list comprehension inside () we're actually creating a generator.

    # Generators dynamically return an object from a series when the 'next' method is called
    # (by for-loop i.e. for <x> in <generator>, by dot-notation call to a generator object's '__next__'
    # method, or by calling next(<generator name>). For large objects (e.g. a giant fastq file) this significantly
    # reduces up-front memory costs because a generator isn't storing an entire file's worth of strings.
    # A file handle returned by open(<filename>) is a generator! Iterating over a filehandle with 'for' calls the
    # __next__ method of the filehandle and returns the result (the next line in the file).
    #
    # The downside is that most generators are exhaustible - once an item in the series is accessed, the
    # generator advances and that item can't be recovered. And if you try to advance beyond the end of a
    # series in a generator (i.e. by exhausting it with a 'for' loop and _then_ calling next,
    # you'll catch a StopIteration exception (unpleasant surprise if you've just parsed a massive file)
    # There are workarounds, however.
    odd_numbers = (num for num in range(a, b) if num % 2 == 1)

    # Note that we can sum a generator of numeric objects (float and/or int), since generators are iterable.
    return sum(odd_numbers)


if __name__ == '__main__':
    # Implementing a command-line argument parser is on to-do list
    # usage in this case, to run and print the result of only the string_slice method (since that's
    # all that's in this to-do block):
    # python intro_problems.py 'myinputstring' 2 5
    print(string_slice(input_string=sys.argv[1], indices=[sys.argv[2], sys.argv[3]]))
