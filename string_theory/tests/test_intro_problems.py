"""Unit test examples"""
# Good import practices as follows:
# Imports of builtin packages come first - this example is unused
import os
# Sub-imports of builtins follow - our interpreter will be aware of the 'TestCase' class and 'main' method from
# unittest, but nothing else
from unittest import TestCase
from unittest import main as run_unittests
# Finally, we import our own code (in same order, package then object imports)
# Anything with an '__init__.py' is considered a 'module' of the 'package' ECZans_rosalind. We use
# dot notation to traverse objects and their sub-objects, and the importer treats packages as objects.
from ECZans_rosalind.string_theory.intro_problems import string_slice


class TestIntroProblems(TestCase):
    """
    Test methods for intro problem solutions
    """
    def setUp(self):
        """
        TestCase.setUp methods perform any necessary prerequisite tasks, e.g. writing supporting files,
        storing data as attributes of 'self', etc.
        :return:
        """
        self.example_string = """
        HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain
        """

    def tearDown(self):
        """
        TestCase.tearDown methods perform cleanup tasks after all test methods are run, e.g. removing supporting
        files from the file system. No tear-down is needed at this time.

        Note: usually a function requires some content to avoid a syntax error. But functions are objects!
        This docstring will be stored as an attribute of the function's 'self'. The python compiler
        considers storing a docstring as 'doing something', and therefore there is no syntax error.
        :return:
        """

    def test_string_slice_01(self):
        """
        This right here is a test method (testing a positive case) Naming scheme for test methods is usually
        test_<thing_being_tested>_<uniq_id>.
        """
        expected_substring = 'Humpty'
        # Arguments can be 'positional' (args) or key-word (kwargs) - here is an example of 'arg' syntax
        actual_substring = string_slice(self.example_string, (22, 27))
        # Bad things happen if these strings aren't equal
        self.assertEqual(expected_substring, actual_substring)

    def test_string_slice_02(self):
        """
        Another positive test case
        """
        expected_substring = 'Dumpty'
        # Keyword argument syntax
        actual_substring = string_slice(input_string=self.example_string, indices=(97, 102))
        self.assertEqual(expected_substring, actual_substring)

    def test_string_slice_03(self):
        """
        Negative test case
        :return:
        """
        expected_substring = 'HumptyDumptysat'
        # Mix of args and kwargs
        actual_substring = string_slice(self.example_string, indices=(84, 102))
        self.assertNotEqual(expected_substring, actual_substring)


if __name__ == '__main__':
    run_unittests()
