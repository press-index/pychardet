# coding=utf-8
import unittest
import pychardet


class PyChardetDetectTest(unittest.TestCase):
    def test_detect_bg_iso88595(self):
        encoding = "ISO-8859-5"
        path = "fixtures/bg/ISO-8859-5/wikitop_bg_ISO-8859-5.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_bg_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/bg/UTF-8/wikitop_bg_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_bg_windows1251(self):
        encoding = "WINDOWS-1251"
        path = "fixtures/bg/WINDOWS-1251/wikitop_bg_WINDOWS-1251.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    @unittest.skip('iso-8859-1 is a default 8859 encoding for now')
    def test_detect_cz_iso88592(self):
        encoding = "ISO-8859-2"
        path = "fixtures/cz/ISO-8859-2/wikitop_cz_ISO-8859-2.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_cz_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/cz/UTF-8/wikitop_cz_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_de_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/de/UTF-8/wikitop_de_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_de_windows1252(self):
        encoding = "WINDOWS-1252"
        path = "fixtures/de/WINDOWS-1252/wikitop_de_WINDOWS-1252.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_dk_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/dk/UTF-8/wikitop_dk_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_dk_windows1252(self):
        encoding = "WINDOWS-1252"
        path = "fixtures/dk/WINDOWS-1252/wikitop_dk_WINDOWS-1252.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_el_iso88597(self):
        encoding = "ISO-8859-7"
        path = "fixtures/el/ISO-8859-7/wikitop_el_ISO-8859-7.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_el_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/el/UTF-8/wikitop_el_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_en_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/en/UTF-8/wikitop_en_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_en_windows1252(self):
        encoding = "WINDOWS-1252"
        path = "fixtures/en/WINDOWS-1252/wikitop_en_WINDOWS-1252.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_es_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/es/UTF-8/wikitop_es_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    @unittest.skip('Can not detect spanish encoded with windows-1252')
    def test_detect_es_windows1252(self):
        encoding = "WINDOWS-1252"
        path = "fixtures/es/WINDOWS-1252/wikitop_es_WINDOWS-1252.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_fi_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/fi/UTF-8/wikitop_fi_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_fi_windows1252(self):
        encoding = "WINDOWS-1252"
        path = "fixtures/fi/WINDOWS-1252/wikitop_fi_WINDOWS-1252.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_fr_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/fr/UTF-8/wikitop_fr_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_fr_windows1252(self):
        encoding = "WINDOWS-1252"
        path = "fixtures/fr/WINDOWS-1252/wikitop_fr_WINDOWS-1252.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_he_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/he/UTF-8/wikitop_he_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_he_windows1255(self):
        encoding = "WINDOWS-1255"
        path = "fixtures/he/WINDOWS-1255/wikitop_he_WINDOWS-1255.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_hu_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/hu/UTF-8/wikitop_hu_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_hu_iso55892(self):
        encoding = "ISO-8859-2"
        path = "fixtures/hu/ISO-8859-2/wikitop_hu_ISO-8859-2.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_it_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/it/UTF-8/wikitop_it_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    @unittest.skip('Can not detect italian encoded with windows-1252')
    def test_detect_it_windows1252(self):
        encoding = "WINDOWS-1252"
        path = "fixtures/it/WINDOWS-1252/wikitop_it_WINDOWS-1252.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_nl_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/nl/UTF-8/wikitop_nl_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_nl_windows1252(self):
        encoding = "WINDOWS-1252"
        path = "fixtures/nl/WINDOWS-1252/wikitop_nl_WINDOWS-1252.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_no_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/no/UTF-8/wikitop_no_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_no_windows1252(self):
        encoding = "WINDOWS-1252"
        path = "fixtures/no/WINDOWS-1252/wikitop_no_WINDOWS-1252.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_pl_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/pl/UTF-8/wikitop_pl_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    @unittest.skip('iso-8859-1 is a default 8859 encoding for now')
    def test_detect_pl_iso88592(self):
        encoding = "ISO-8859-2"
        path = "fixtures/pl/ISO-8859-2/wikitop_pl_ISO-8859-2.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_pt_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/pt/UTF-8/wikitop_pt_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_pt_windows1252(self):
        encoding = "WINDOWS-1252"
        path = "fixtures/pt/WINDOWS-1252/wikitop_pt_WINDOWS-1252.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_ru_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/ru/UTF-8/wikitop_ru_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_ru_windows1251(self):
        encoding = "WINDOWS-1251"
        path = "fixtures/ru/WINDOWS-1251/wikitop_ru_WINDOWS-1251.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_ru_ibm855(self):
        encoding = "IBM855"
        path = "fixtures/ru/IBM855/wikitop_ru_IBM855.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_ru_koi8r(self):
        encoding = "KOI8-R"
        path = "fixtures/ru/KOI8-R/wikitop_ru_KOI8-R.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_ru_maccyrillic(self):
        encoding = "MAC-CYRILLIC"
        path = "fixtures/ru/X-MAC-CYRILLIC/wikitop_ru_MACCYRILLIC.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_se_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/se/UTF-8/wikitop_se_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    @unittest.skip('Can not detect sweden encoded with windows-1252')
    def test_detect_se_windows1252(self):
        encoding = "WINDOWS-1252"
        path = "fixtures/se/WINDOWS-1252/wikitop_se_WINDOWS-1252.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_th_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/th/UTF-8/wikitop_th_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    @unittest.skip('Thai in tis-620 is detected as utf-8')
    def test_detect_th_tis620_1(self):
        encoding = "TIS-620"
        path = "fixtures/th/TIS-620/utffool_th_TIS-620.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_th_tis620_2(self):
        encoding = "TIS-620"
        path = "fixtures/th/TIS-620/wikitop_th_TIS-620.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_tr_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/tr/UTF-8/wikitop_tr_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_tr_iso88599(self):
        encoding = "ISO-8859-9"
        path = "fixtures/tr/ISO-8859-9/wikitop_tr_ISO-8859-9.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_zh_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/zh/UTF-8/wikitop_zh_UTF-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_zh_gb18030(self):
        encoding = "GB18030"
        path = "fixtures/zh/GB18030/wikitop_zh_GB18030.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    @unittest.skip('Confusing iso-8859-1 with iso-8859-15')
    def test_detect_da_iso88591(self):
        encoding = "ISO-8859-1"
        path = "fixtures/da/ISO-8859-1/iso-8859-1.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_da_iso885915(self):
        encoding = "ISO-8859-15"
        path = "fixtures/da/ISO-8859-15/iso-8859-15.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_da_utf8(self):
        encoding = "UTF-8"
        path = "fixtures/da/UTF-8/utf-8.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def test_detect_da_windows1252(self):
        encoding = "WINDOWS-1252"
        path = "fixtures/da/WINDOWS-1252/windows-1252.txt"
        self.assertDetectedEncodingEqual(encoding, path)

    def assertDetectedEncodingEqual(self, encoding, fixture_path):
        with open(fixture_path, 'rb') as f:
            text = f.read()

        detected_encoding = pychardet.detect(text)['encoding']
        self.assertEqual(encoding.lower(), detected_encoding.lower())


if __name__ == "__main__":
    unittest.main()
