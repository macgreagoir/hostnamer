#!/usr/bin/env python

import unittest
from hostnamer import main, vowels


class TestHostnamer(unittest.TestCase):
    def setUp(self):
        pass

    def test_names_count(self):
        self.assertEqual(len(main()), 9)

    def test_name_length(self):
        out = main()
        self.assertEqual(len(out[0]), 6)

    def test_vowel_positions(self):
        out = main()
        self.assertTrue(out[0][1] in vowels)
        self.assertTrue(out[0][2] in vowels)
        self.assertTrue(out[0][5] in vowels)

if __name__ == "__main__":
    unittest.main()
