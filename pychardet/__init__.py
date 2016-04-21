# coding=utf-8
import six
from pychardet.universal_detector import UniversalDetector


__name__ = "pychardet"
__version__ = "0.0.1"


def detect(byte_str):
    """
    :param six.binary_type byte_str: Byte string with unknown encoding
    :return Detected encoding with confidence
    :rtype: dict
    """
    if isinstance(byte_str, six.text_type):
        return {'encoding': six.text_type('unicode'), 'confidence': 1.}

    with UniversalDetector() as detector:
        detector.feed(byte_str)
        return detector.result
