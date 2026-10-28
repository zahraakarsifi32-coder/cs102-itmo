
import unittest

from src.lab2.rsa import (
    is_prime,
    gcd,
    multiplicative_inverse,
    generate_keypair,
)


class RSATestCase(unittest.TestCase):

    def test_prime_two(self):
        self.assertTrue(is_prime(2))

    def test_prime_eleven(self):
        self.assertTrue(is_prime(11))

    def test_not_prime_one(self):
        self.assertFalse(is_prime(1))

    def test_not_prime_twelve(self):
        self.assertFalse(is_prime(12))

    def test_gcd(self):
        self.assertEqual(gcd(12, 15), 3)

    def test_gcd_coprime(self):
        self.assertEqual(gcd(3, 7), 1)

    def test_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    def test_inverse_error(self):
        with self.assertRaises(ValueError):
            multiplicative_inverse(2, 40)

    def test_invalid_phi(self):
        with self.assertRaises(ValueError):
            multiplicative_inverse(3, 1)

    def test_generate_keypair(self):
        public, private = generate_keypair(17, 19)

        e, n = public
        d, private_n = private

        self.assertEqual(n, 323)
        self.assertEqual(private_n, 323)
        self.assertEqual((e * d) % 288, 1)

    def test_non_prime_numbers(self):
        with self.assertRaises(ValueError):
            generate_keypair(4, 19)

    def test_equal_primes(self):
        with self.assertRaises(ValueError):
            generate_keypair(17, 17)


if __name__ == "__main__":
    unittest.main()
