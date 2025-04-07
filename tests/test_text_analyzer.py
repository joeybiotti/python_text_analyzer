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

    def test_empty_text(self):
        sample_text = ""
        expected_result = {
            'word_count': 0,
            'sentence_count': 0,
            'unique_words': 0,
            'word_frequency': []
        }

        result = analyze_text(sample_text)
        
        self.assertEqual(result['word_count'], expected_result['word_count'])
        self.assertEqual(result['sentence_count'], expected_result['sentence_count'])
        self.assertEqual(result['unique_words'], expected_result['unique_words'])
        self.assertEqual(result['word_frequency'], expected_result['word_frequency'])

    def test_special_characters(self):
        sample_text = "Wow!!! This is fun... Right? :)"
        expected_result = {
            'word_count': 5,
            'sentence_count': 4,
            'unique_words': 5,
            'word_frequency': [('wow', 1), ('this', 1), ('is', 1), ('fun', 1), ('right', 1)]
        }

        result = analyze_text(sample_text)
        
        self.assertEqual(result['word_count'], expected_result['word_count'])
        self.assertEqual(result['sentence_count'], expected_result['sentence_count'])
        self.assertEqual(result['unique_words'], expected_result['unique_words'])
        self.assertEqual(result['word_frequency'], expected_result['word_frequency'])

    def test_repeated_words(self):
        sample_text = "Test test test. Test!"
        expected_word_count = 4
        expected_sentence_count = 2
        expected_unique_words = 1
        expected_word_frequency = [('test', 4)]

        result = analyze_text(sample_text)
        
        self.assertEqual(result['word_count'], expected_word_count)
        self.assertEqual(result['sentence_count'], expected_sentence_count)
        self.assertEqual(result['unique_words'], expected_unique_words)
        self.assertEqual(result['word_frequency'], expected_word_frequency)

if __name__ == '__main__':
    unittest.main()