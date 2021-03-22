import unittest
from methods import Methods


class test(unittest.TestCase):
    def basic(self):
      testcase = "LoveLace, Ada"
      expected = "Ada LoveLace"
      self.assertEqual(Methods.rearrage_name(testcase), expected)

unittest.main()
