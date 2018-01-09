import unittest
import FilesAreEqual


class MyTestCase(unittest.TestCase):
    # Test 1
    def test_T1a_txtResult_is_txtExpected(self):
        self.assertTrue(FilesAreEqual.compareXMLs("files/textExtractor/txt_T1a_result.txt", "files/textExtractor/txt_T1a_expected.txt"))

    def test_T1b_txtResult_is_txtExpected(self):
        self.assertTrue(FilesAreEqual.compareXMLs("files/textExtractor/txt_T1b_result.txt", "files/textExtractor/txt_T1b_expected.txt"))

    # Test 2
    def test_T2a_txtResult_is_txtExpected(self):
        self.assertTrue(FilesAreEqual.compareXMLs("files/textExtractor/txt_T2a_result.txt", "files/textExtractor/txt_T2a_expected.txt"))

    def test_T2b_txtResult_is_txtExpected(self):
        self.assertTrue(FilesAreEqual.compareXMLs("files/textExtractor/txt_T2b_result.txt", "files/textExtractor/txt_T2b_expected.txt"))

    # Test 3
    def test_T3a_txtResult_is_txtExpected(self):
        self.assertTrue(FilesAreEqual.compareXMLs("files/textExtractor/txt_T3a_result.txt", "files/textExtractor/txt_T3a_expected.txt"))

    def test_T3b_txtResult_is_txtExpected(self):
        self.assertTrue(FilesAreEqual.compareXMLs("files/textExtractor/txt_T3b_result.txt", "files/textExtractor/txt_T3b_expected.txt"))

    # Test 4
    def test_T4a_txtResult_is_txtExpected(self):
        self.assertTrue(FilesAreEqual.compareXMLs("files/textExtractor/txt_T4a_result.txt", "files/textExtractor/txt_T4a_expected.txt"))

    def test_T4b_txtResult_is_txtExpected(self):
        self.assertTrue(FilesAreEqual.compareXMLs("files/textExtractor/txt_T4b_result.txt", "files/textExtractor/txt_T4b_expected.txt"))

    # Test 5
    def test_T5a_txtResult_is_txtExpected(self):
        self.assertTrue(FilesAreEqual.compareXMLs("files/textExtractor/txt_T5a_result.txt", "files/textExtractor/txt_T5a_expected.txt"))

    def test_T5b_txtResult_is_txtExpected(self):
        self.assertTrue(FilesAreEqual.compareXMLs("files/textExtractor/txt_T5b_result.txt", "files/textExtractor/txt_T5b_expected.txt"))

    # Test 6
    def test_T6a_txtResult_is_txtExpected(self):
        self.assertTrue(FilesAreEqual.compareXMLs("files/textExtractor/txt_T6a_result.txt", "files/textExtractor/txt_T6a_expected.txt"))

    def test_T6b_txtResult_is_txtExpected(self):
        self.assertTrue(FilesAreEqual.compareXMLs("files/textExtractor/txt_T6b_result.txt", "files/textExtractor/txt_T6b_expected.txt"))

    # Test 7
    def test_T7a_txtResult_is_txtExpected(self):
        self.assertTrue(FilesAreEqual.compareXMLs("files/textExtractor/txt_T7a_result.txt", "files/textExtractor/txt_T7a_expected.txt"))

    def test_T7b_txtResult_is_txtExpected(self):
        self.assertTrue(FilesAreEqual.compareXMLs("files/textExtractor/txt_T7b_result.txt", "files/textExtractor/txt_T7b_expected.txt"))


if __name__ == '__main__':
    unittest.main()
