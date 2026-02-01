#!/usr/bin/env python
# coding: utf-8

import unittest

class MyFirstTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1+2, 3)
    
    def test_2(self):
        self.assertTrue(3 > 2)

if __name__ == "__main__":
    unittest.main()