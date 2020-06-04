"""Unit test examples"""
# Good import practices as follows:
# Imports of builtin packages come first
import os
# Sub-imports of builtins follow - our interpreter will be aware of the 'TestCase' class and 'main' method from
# unittest, but nothing else. Nothing wrong with just importing 'unittest' instead
from unittest import TestCase
from unittest import main as run_unittests # Re-naming this bc 'main' is ambiguous
# Finally, we import our own code (in same order, package then object imports)
# Anything with an '__init__.py' is considered a 'module' of the 'package' ECZans_rosalind. We use
# dot notation to traverse objects and their sub-objects, and the importer treats packages as objects.
from ECZans_rosalind.string_theory import intro_problems


class TestIntroProblems(TestCase):
    """
    Test methods for intro problem solutions
    """
    def setUp(self):
        """
        TestCase.setUp methods perform any necessary prerequisite tasks, e.g. writing supporting files,
        storing data for later use (as 'attributes'/variables assigned to 'self'), etc.
        :return:
        """
        self.example_string = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain"
        self.multiline_input = 'test_data/multiline.txt'
        self.multiline_output = 'test_data/even_numbered_out.tmp'
        intro_problems.even_numbered_lines(self.multiline_input, self.multiline_output)
        with open(self.multiline_output) as even_out:
            self.multiline_output_lines = even_out.readlines()

    def tearDown(self):
        """
        TestCase.tearDown methods perform cleanup tasks after all test methods are run, e.g. removing unneeded
        files from the file system.
        :return:
        """
        os.remove(self.multiline_output)

    def test_string_slice_01(self):
        """
        This right here is a test method (testing a positive case). Naming scheme for test methods is usually
        test_<thing_being_tested>_<uniq_id>.
        """
        expected_substring = 'Humpty'
        # You'll see 'arg' and 'kwarg' used a lot in documentation
        # Arguments for 'callable' objects (methods or functions, some classes) can be
        # 'positional' (args) or keyword (kwargs) - here is an example of 'arg' syntax
        actual_substring = intro_problems.string_slice(self.example_string, (22, 27))
        # Bad things happen if these strings aren't equal
        self.assertEqual(expected_substring, actual_substring)

    def test_string_slice_02(self):
        """
        Another positive test case
        """
        expected_substring = 'Dumpty'
        # Keyword argument syntax - any order is fine when every argument is assigned to a keyword
        actual_substring = intro_problems.string_slice(indices=(97, 102), input_string=self.example_string)
        self.assertEqual(expected_substring, actual_substring)

    def test_string_slice_03(self):
        """
        Negative test case
        :return:
        """
        expected_substring = 'HumptyDumptysat'
        # Mix of args and kwargs - args precede kwargs, but overall order must be
        # maintained when the two are mixed
        actual_substring = intro_problems.string_slice(self.example_string, indices=(84, 102))
        self.assertNotEqual(expected_substring, actual_substring)

    def test_calc_hypotenuse_01(self):
        """
        Test that the correct value is returned
        """
        expected_value = 13
        actual_value = intro_problems.calc_hypotenuse(2, 3)
        self.assertEqual(expected_value, actual_value)

    def test_calc_hypotenuse_02(self):
        """
        Test that the expected exception is raised if bad input is provided
        """
        with self.assertRaises(ValueError):
            intro_problems.calc_hypotenuse(a=2, b=2000)

    def test_even_numbered_lines_01(self):
        """
        Test that expected number of even-numbered lines are captured
        """
        expected_line_count = 4
        actual_line_count = len(self.multiline_output_lines)
        self.assertEqual(expected_line_count, actual_line_count)

    def test_even_numbered_lines_02(self):
        """
        Test that 2nd line in even_numbered_lines output is what we expected
        """
        expected_line = 'He was not afraid to die, O brave Sir Robin'
        # Strip method of str removes whitespace characters including carriage returns by default
        actual_line = self.multiline_output_lines[1].strip()
        self.assertEqual(expected_line, actual_line)

    def test_dict_word_counter(self):
        """
        Test that output is correct
        """
        expected_output = {'dog': 1, 'cat': 2, 'ball': 3}

        # Join n=value occurrences of dict keys together into one string
        input_string = ''
        for key, value in expected_output.items():
            input_string += (key + ' ') * value

        actual_output = intro_problems.dict_word_counter(input_string)

        self.assertEqual(expected_output, actual_output)

    def sum_odds_from_range_01(self):
        """
        Test that the sum value returned is correct
        """
        a, b = 2, 11
        expected_sum = 3 + 5 + 7 + 9 + 11
        actual_sum = intro_problems.sum_odds_from_range(a, b)
        self.assertEqual(expected_sum, actual_sum)

    def sum_odds_from_range_02(self):
        """
        Test that the expected exception is raised if bad input is given
        """
        # Suggest a change and write what should go here!


# When this script is called, the interpreter will read this source file and 'initialize' (read & store) some objects
# in its 'scope' (as in R). One of these objects is the variable __name__. The string '__main__' will be assigned
# to variable __name__ for this script (since it's the script we ran), but _not_ to anything we import here.
#
# I imported the package 'os' above (which, fyi, has the functionality of 'ls', 'mv', 'chmod', 'cd', 'pwd',
# and many others)
#
# In the interpreter's scope, the object representing this script is named '__main__', but 'os' is also
# contained in-scope after we import it. It also has a __name__ variable, containing the string 'os'.
# If I imported a file called 'foo.py' as 'foo', that module's in-scope __name__ would be 'foo'.
#
# If the 'foo.py' script _also_ was meant to be run from the command-line (contained "if __name__ == '__main__':",
# and some tasks to do in case that 'if' statement evaluated to True), nothing following the 'if' in 'foo.py'
# would be run on importing 'foo' here. That's thanks to this 'if' statement, and the variable __name__!
#
# You can test this out - instructions below
if __name__ == '__main__':
    # This is the unittest.main() method. When this script is run, unittest will search for any
    # classes that are 'descendents' or 'children' of its TestCase class (which we 'sub-class'
    # to tell unittest 'hey here's a container full of test cases I want you to run!). It'll
    # do some setup steps, and then run the setup, test case, and tear down methods of those
    # descendent classes, and tell us all about the mistakes that we have made (fun!).
    run_unittests()


# Copy the following to two scripts
# p.s. note string method 'format', accessed with dot-notation. We initialized a string "I'm..." but didn't store it
# as a named variable - nevertheless, we can access and use the methods that belong to it as a string (specifically,
# an 'instance' of the builtin python class 'str') as if we had! str.format is used to substitute a placeholder in
# one string with another object - there's another syntax that uses '%' to mark places for substitutions, but I find that
# less readable
# p.p.s. I think this should work, but if not, could be fun to debug :D

# if __name__ == '__main__':
#   print("I'm the script that's running, and my name is {script_name}".format(script_name=__name__))

# Put at the top of one script (the one you intend to run):
# import <name of other script, without the .py>

# Put at the top of imported script:
# print("I've just been imported, my name is {}".format(__name__))

# And run!