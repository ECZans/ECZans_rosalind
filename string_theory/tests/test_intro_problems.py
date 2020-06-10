import os
from unittest import TestCase
from unittest import main as run_unittests
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
        actual_substring = intro_problems.string_slice(self.example_string, (22, 27))
        self.assertEqual(expected_substring, actual_substring)

    def test_string_slice_02(self):
        """
        Another positive test case
        """
        expected_substring = 'Dumpty'
        actual_substring = intro_problems.string_slice(indices=(97, 102), input_string=self.example_string)
        self.assertEqual(expected_substring, actual_substring)

    def test_string_slice_03(self):
        """
        Negative test case
        :return:
        """
        expected_substring = 'HumptyDumptysat'
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
        actual_line = self.multiline_output_lines[1].strip()
        self.assertEqual(expected_line, actual_line)

    def test_dict_word_counter(self):
        """
        Test that output is correct
        """
        expected_output = {'dog': 1, 'cat': 2, 'ball': 3}
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


if __name__ == '__main__':
    run_unittests()
