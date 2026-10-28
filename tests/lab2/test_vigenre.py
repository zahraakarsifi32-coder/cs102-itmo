
import unittest

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere


class VigenereTestCase(unittest.TestCase):

    def test_encrypt(self):
        self.assertEqual(
            encrypt_vigenere("ATTACKATDAWN", "LEMON"),
            "LXFOPVEFRNHR"
        )

    def test_decrypt(self):
        self.assertEqual(
            decrypt_vigenere("LXFOPVEFRNHR", "LEMON"),
            "ATTACKATDAWN"
        )

    def test_keyword_a(self):
        self.assertEqual(
            encrypt_vigenere("PYTHON", "A"),
            "PYTHON"
        )

    def test_lowercase(self):
        self.assertEqual(
            encrypt_vigenere("python", "a"),
            "python"
        )

    def test_repeating_keyword(self):
        self.assertEqual(
            encrypt_vigenere("AAAA", "BC"),
            "BCBC"
        )

    def test_symbols(self):
        self.assertEqual(
            encrypt_vigenere("123!", "KEY"),
            "123!"
        )

    def test_encrypt_decrypt(self):
        text = "Hello World!"
        encrypted = encrypt_vigenere(text, "KEY")
        self.assertEqual(
            decrypt_vigenere(encrypted, "KEY"),
            text
        )

    def test_empty_keyword(self):
        with self.assertRaises(ValueError):
            encrypt_vigenere("HELLO", "")

    def test_invalid_keyword(self):
        with self.assertRaises(ValueError):
            decrypt_vigenere("HELLO", "123")


if __name__ == "__main__":
    unittest.main()
