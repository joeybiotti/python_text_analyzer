import unittest
from readability import analyze_reading_level

class TestReadabilityAnalyzer(unittest.TestCase):
    def test_analyze_readability(self):
        sample_text = "This is a simple sentence. It is used for testing readability analysis."
        expected_flesch_kincaid = 8.38

        result = analyze_reading_level(sample_text)

        self.assertAlmostEqual(result['flesch_kincaid'], expected_flesch_kincaid, places=1)

if __name__ == '__main__':
    unittest.main()