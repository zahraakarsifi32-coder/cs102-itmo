"""Educational RSA key generation using basic number theory."""

# pylint: disable=invalid-name

import random
from typing import Tuple


def is_prime(n: int) -> bool:
    """Return True when n is prime.

    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(12)
    False
    >>> is_prime(1)
    False
    """
    if n < 2:
        return False
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False
    return True


def gcd(a: int, b: int) -> int:
    """Find the greatest common divisor using Euclid's algorithm.

    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while b:
        a, b = b, a % b
    return abs(a)


def multiplicative_inverse(e: int, phi: int) -> int:
    """Find d such that (d * e) % phi is 1.

    >>> multiplicative_inverse(7, 40)
    23
    """
    if phi <= 1:
        raise ValueError("phi must be greater than one")
    old_r, remainder = e, phi
    old_x, coefficient = 1, 0
    while remainder:
        quotient = old_r // remainder
        old_r, remainder = remainder, old_r - quotient * remainder
        old_x, coefficient = coefficient, old_x - quotient * coefficient
    if old_r != 1:
        raise ValueError("e and phi must be coprime")
    return old_x % phi


def generate_keypair(p: int, q: int) -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """Generate public and private toy RSA keys from distinct primes.

    >>> public, private = generate_keypair(17, 19)
    >>> public[1] == private[1] == 323
    True
    >>> (public[0] * private[0]) % 288
    1
    """
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    if p == q:
        raise ValueError("p and q cannot be equal")

    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    d = multiplicative_inverse(e, phi)
    return (e, n), (d, n)
