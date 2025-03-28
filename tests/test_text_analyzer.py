import unittest
from text_analyzer import analyze_text

class TestTextAnalyzer(unittest.TestCase):
    def test_analyze_text(self):
        sample_text = "Hello, world! This is a test. Goodbye!"
        expected_word_count = 7
        expected_sentence_count = 3
        expected_unique_words = 7
        expected_word_frequency = [('hello', 1), ('world', 1), ('this', 1), ('is', 1), ('a', 1), ('test', 1), ('goodbye', 1)]

        result = analyze_text(sample_text)
        
        self.assertEqual(result['word_count'], expected_word_count)
        self.assertEqual(result['sentence_count'], expected_sentence_count)
        self.assertEqual(result['unique_words'], expected_unique_words)
        self.assertEqual(result['word_frequency'], expected_word_frequency)

if __name__ == '__main__':
    unittest.main()