import unittest

from api.score_filter import parse_score_filter


class ParseScoreFilterTests(unittest.TestCase):
    def test_missing_filter_disables_filtering(self):
        self.assertIsNone(parse_score_filter(None))

    def test_valid_numeric_thresholds_are_parsed(self):
        self.assertEqual(parse_score_filter("8"), 8.0)
        self.assertEqual(parse_score_filter(" 7.25 "), 7.25)
        self.assertEqual(parse_score_filter("-1.5"), -1.5)

    def test_malformed_thresholds_are_rejected(self):
        for value in ("", " ", "high", "8,5"):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "valid number"):
                    parse_score_filter(value)

    def test_non_finite_thresholds_are_rejected(self):
        for value in ("NaN", "Infinity", "-Infinity", "1e309"):
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "finite number"):
                    parse_score_filter(value)


if __name__ == "__main__":
    unittest.main()
