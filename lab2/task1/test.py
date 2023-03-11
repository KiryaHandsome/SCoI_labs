import unittest
import statistic_util


class TestCountSentences(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(statistic_util.count_sentences(''), 0, 'Empty text test: result isn\'t zero')

    def test_abbreviations(self):
        text = 'Hello, Mr. Derek. Sample text i.e. and more Ph.D. - it\'s greate text!!'
        self.assertEqual(statistic_util.count_sentences(text), 2, 'Abbreviations test: number of sentences not 2')

    def test_sample_text(self):
        text = 'Oh!!! Thats good idea; Oh no... I forgot my keys in the car. '
        self.assertEqual(statistic_util.count_sentences(text), 3, 'Sample text test: number of sentences not 3')


if __name__ == '__main__':
    unittest.main()
