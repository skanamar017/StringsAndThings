import unittest
from strings_and_things import StringsAndThings


class TestContainsEqualNumberOfIsAndNot(unittest.TestCase):
    
    def setUp(self):
        self.strings_and_things = StringsAndThings()
    
    def test_equal_is_not_test1(self):
        actual = self.strings_and_things.contains_equal_number_of_is_and_not("This is not")
        self.assertFalse(actual)
    
    def test_equal_is_not_test2(self):
        actual = self.strings_and_things.contains_equal_number_of_is_and_not("This is notnot")
        self.assertTrue(actual)
    
    def test_equal_is_not_test3(self):
        actual = self.strings_and_things.contains_equal_number_of_is_and_not("noisxxnotyynotxisi")
        self.assertTrue(actual)


class TestCountTriple(unittest.TestCase):
    
    def setUp(self):
        self.strings_and_things = StringsAndThings()
    
    def test_count_triple_test1(self):
        expected = 1
        actual = self.strings_and_things.count_triple("abcXXXabc")
        self.assertEqual(expected, actual)
    
    def test_count_triple_test2(self):
        expected = 3
        actual = self.strings_and_things.count_triple("xxxabyyyycd")
        self.assertEqual(expected, actual)
    
    def test_count_triple_test3(self):
        expected = 0
        actual = self.strings_and_things.count_triple("a")
        self.assertEqual(expected, actual)


class TestCountYZ(unittest.TestCase):
    
    def setUp(self):
        self.strings_and_things = StringsAndThings()
    
    def test_count_yz_test1(self):
        input_str = "fez day"
        expected = 2
        actual = self.strings_and_things.count_yz(input_str)
        self.assertEqual(expected, actual)
    
    def test_count_yz_test2(self):
        input_str = "day fez"
        expected = 2
        actual = self.strings_and_things.count_yz(input_str)
        self.assertEqual(expected, actual)
    
    def test_count_yz_test3(self):
        input_str = "day fyyyz"
        expected = 2
        actual = self.strings_and_things.count_yz(input_str)
        self.assertEqual(expected, actual)


class TestGIsHappy(unittest.TestCase):
    
    def setUp(self):
        self.strings_and_things = StringsAndThings()
    
    def test_g_is_happy_test1(self):
        actual = self.strings_and_things.g_is_happy("xxggxx")
        self.assertTrue(actual)
    
    def test_g_is_happy_test2(self):
        actual = self.strings_and_things.g_is_happy("xxgxx")
        self.assertFalse(actual)
    
    def test_g_is_happy_test3(self):
        actual = self.strings_and_things.g_is_happy("xxggyygxx")
        self.assertTrue(actual)


class TestRemoveString(unittest.TestCase):
    
    def setUp(self):
        self.strings_and_things = StringsAndThings()
    
    def test_remove_string_test1(self):
        expected = "He there"
        actual = self.strings_and_things.remove_string("Hello there", "llo")
        self.assertEqual(expected, actual)
    
    def test_remove_string_test2(self):
        expected = "Hllo thr"
        actual = self.strings_and_things.remove_string("Hello there", "e")
        self.assertEqual(expected, actual)
    
    def test_remove_string_test3(self):
        expected = "Hello there"
        actual = self.strings_and_things.remove_string("Hello there", "x")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()