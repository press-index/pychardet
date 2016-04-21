# coding=utf-8
import six
import unittest
from pychardet import UniversalDetector


class UniversalDetectorTest(unittest.TestCase):
    def setUp(self):
        self.detector = UniversalDetector()
        self.text = six.text_type('hello')
        self.binary_text = self.text.encode()

    def test_feed(self):
        self.detector.feed(self.binary_text)

        self.assertDictEqual({'encoding': 'ascii', 'confidence': 1.},
                             self.detector.result)

    def test_feed_unicode(self):
        with self.assertRaises(TypeError):
            self.detector.feed(self.text)

    def test_close(self):
        self.detector.feed(self.binary_text)
        self.detector.close()

        self.assertDictEqual({'encoding': None, 'confidence': 0.},
                             self.detector.result)

    def test_with_statement_closes_detector(self):
        with self.detector:
            self.detector.feed(self.binary_text)

        self.assertDictEqual({'encoding': None, 'confidence': 0.},
                             self.detector.result)


if __name__ == "__main__":
    unittest.main()
