"""Unit test examples"""
# Good import practices as follows:
# Imports of builtin packages come first - this example is unused
import os
# Sub-imports of builtins follow - our interpreter will be aware of the 'TestCase' class and 'main' method from
# unittest, but nothing else. Nothing wrong with just importing 'unittest' instead
from unittest import TestCase
from unittest import main as run_unittests # Re-naming this bc 'main' is ambiguous
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
        storing data for later use (as 'attributes'/variables assigned to 'self'), etc.
        :return:
        """
        self.example_string = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain"

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
        This right here is a test method (testing a positive case). Naming scheme for test methods is usually
        test_<thing_being_tested>_<uniq_id>.
        """
        expected_substring = 'Humpty'
        # You'll see 'arg' and 'kwarg' used a lot in documentation
        # Arguments for 'callable' objects (methods or functions, some classes) can be
        # 'positional' (args) or keyword (kwargs) - here is an example of 'arg' syntax
        actual_substring = string_slice(self.example_string, (22, 27))
        # Bad things happen if these strings aren't equal
        self.assertEqual(expected_substring, actual_substring)

    def test_string_slice_02(self):
        """
        Another positive test case
        """
        expected_substring = 'Dumpty'
        # Keyword argument syntax - any order is fine when every argument is assigned to a keyword
        actual_substring = string_slice(indices=(97, 102), input_string=self.example_string)
        self.assertEqual(expected_substring, actual_substring)

    def test_string_slice_03(self):
        """
        Negative test case
        :return:
        """
        expected_substring = 'HumptyDumptysat'
        # Mix of args and kwargs - args precede kwargs, but overall order must be
        # maintained when the two are mixed
        actual_substring = string_slice(self.example_string, indices=(84, 102))
        self.assertNotEqual(expected_substring, actual_substring)


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