import unittest

from translator import english_to_french, french_to_english

class TestStringMethodsOne(unittest.TestCase):
    def test_null_e2f(self):
        self.assertNotEqual(english_to_french(0),0)
    def test_e2f(self):
        self.assertEqual(english_to_french('Hello'), "Bonjour")
    def test_e2f_2(self):
        self.assertEqual(english_to_french('How are you?'), 'Comment es-tu?')

class TestStringMethodsTwo(unittest.TestCase):
    def test_null_f2e(self):
        self.assertNotEqual(french_to_english(0),0)
    def test_f2e(self):
        self.assertEqual(french_to_english('Bonjour'),"Hello")
    def test_f2e_2(self):
        self.assertEqual(french_to_english('Comment es-tu?'),"How are you?")

if __name__ == '__main__':
    unittest.main()