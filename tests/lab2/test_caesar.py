
import unittest

from src.lab2.caesar import encrypt_caesar, decrypt_caesar


class CaesarTestCase(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(encrypt_caesar("ABC"), "DEF")

    def test_decrypt(self):
        self.assertEqual(decrypt_caesar("DEF"), "ABC")

    def test_end_of_alphabet(self):
        self.assertEqual(encrypt_caesar("XYZ"), "ABC")

    def test_start_of_alphabet(self):
        self.assertEqual(decrypt_caesar("ABC"), "XYZ")

    def test_lowercase(self):
        self.assertEqual(encrypt_caesar("abc"), "def")

    def test_symbols(self):
        self.assertEqual(encrypt_caesar("123!"), "123!")

    def test_encrypt_decrypt(self):
        text = "Python3.6"
        encrypted = encrypt_caesar(text)
        self.assertEqual(decrypt_caesar(encrypted), text)


if __name__ == "__main__":
    unittest.main()
