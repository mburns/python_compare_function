import unittest

from main import compare


class CompareTest(unittest.TestCase):
    def test_deep_compare(self):
        a = {"hello": "world"}
        b = {"hello": "goodbye"}
        c = {"first": {"second": {"third": "level"}}}
        d = {"first": {"second": {"third": 42}}}

        self.assertEqual(compare(a, a), True)
        self.assertEqual(compare(b, b), True)
        self.assertEqual(compare(c, c), True)
        self.assertEqual(compare(d, d), True)

        self.assertEqual(compare(a, b), False)
        self.assertEqual(compare(c, d), False)

    def test_shallow_compare(self):
        a = {"hello": "world", "numbers": [1, 2, 3, 4, 5]}
        b = {"hello": "goodbye", "word": "Banana"}

        self.assertEqual(compare(a, a, True), True)
        self.assertEqual(compare(b, b, True), True)
        self.assertEqual(compare(a, b, True), False)


if __name__ == "__main__":
    unittest.main()
