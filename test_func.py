#!/usr/bin/env python
import unittest
from app import string_ccat

class Testing(TestCase):

    def test_concat(self):
        self.assertEqual(string_ccat("a", "b"), "ab")
