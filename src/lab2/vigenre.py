"""Vigenere cipher using a repeating English-letter keyword."""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """Encrypt text with a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    if not keyword or not keyword.isascii() or not keyword.isalpha():
        raise ValueError("Keyword must contain English letters")

    ciphertext = ""
    for index, char in enumerate(plaintext):
        shift = ord(keyword[index % len(keyword)].upper()) - ord("A")
        if "A" <= char <= "Z":
            ciphertext += chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
        elif "a" <= char <= "z":
            ciphertext += chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
        else:
            ciphertext += char
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """Decrypt text encrypted with a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    if not keyword or not keyword.isascii() or not keyword.isalpha():
        raise ValueError("Keyword must contain English letters")

    plaintext = ""
    for index, char in enumerate(ciphertext):
        shift = ord(keyword[index % len(keyword)].upper()) - ord("A")
        if "A" <= char <= "Z":
            plaintext += chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
        elif "a" <= char <= "z":
            plaintext += chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
        else:
            plaintext += char
    return plaintext
