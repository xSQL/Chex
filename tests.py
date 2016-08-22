#!/usr/bin/env python3
import unittest
from chex import Chex


class TestChex(unittest.TestCase):
    """LordKey testing."""
    def test_alphabet_and_size(self):
        """When specified the size and the alphabet."""
        lk = Chex(phrase='abcde', size=3)

        self.assertEqual(lk[2], 'aac')
        self.assertEqual(lk['aac'], 2)

        self.assertEqual(lk[96], 'deb')
        self.assertEqual(lk['deb'], 96)

        self.assertEqual(lk[120], 'eea')
        self.assertEqual(lk['eea'], 120)

    def test_alphabet_without_size(self):
        """When specified only alphabet."""
        lk = Chex(phrase='abcde')

        self.assertEqual(lk[2], 'aaaaaaac')
        self.assertEqual(lk['c'], 2)

        self.assertEqual(lk[17], 'aaaaaadc')
        self.assertEqual(lk['dc'], 17)

        self.assertEqual(lk[120], 'aaaaaeea')
        self.assertEqual(lk['eea'], 120)

    def test_defaults_settings(self):
        """Use default settings."""
        lk = Chex()
        self.assertEqual(lk[1][-1], lk.phrase[1])

    def test_exceptions_bad_alphabet(self):
        """The alphabet should be only a str and have not char duplicates."""
        with self.assertRaises(TypeError):
            Chex(phrase=['a', 'b', 'c'])

        with self.assertRaises(ValueError):
            Chex(phrase='abca')

    def test_exceptions_bad_size(self):
        """The size can be None or an integer greater than zero."""
        with self.assertRaises(TypeError):
            Chex(size=2.7)

        with self.assertRaises(ValueError):
            Chex(size=0)

    def test_exceptions_large_id(self):
        """Index outside of sequence length."""
        lk = Chex(phrase='abcde', size=3)
        with self.assertRaises(KeyError):
            lk[1024]

    def test_exceptions_negative_id(self):
        """Negative ID - the ID can be from 0 to N."""
        lk = Chex(phrase='abcde', size=3)
        with self.assertRaises(KeyError):
            lk[-1]

    def test_exceptions_wrong_key(self):
        """The key contains characters that are not in the alphabet."""
        lk = Chex(phrase='abcde', size=3)
        with self.assertRaises(ValueError):
            lk['zzz']


if __name__ == '__main__':
    unittest.main()
