import unittest
import FilesAreEqual
import textExtractor

# aa = sys.path[0][0:sys.path[0].rfind('\\')] + '\\Source Code' + '\\Text from pdf and docx'
# print aa
# sys.path.insert(0, aa)


class MyTestCase(unittest.TestCase):
    # Test 1
    # def test_T1a_txtResult_is_txtExpected(self):
    #     self.assertTrue(FilesAreEqual.compareFiles("files/textExtractor/txt_T1a_result.txt", "files/textExtractor/txt_T1a_expected.txt"))

    def test_T1b_txtResult_is_txtExpected(self):
        textExtractor.pdf_to_text('files/textExtractor/pdf_T1b_document gol.pdf')
        self.assertTrue(FilesAreEqual.compareFiles("files/textExtractor/pdf_T1b_document gol.txt", "files/textExtractor/pdf_T1b_document gol_expected.txt"))

    # Test 2
    # def test_T2a_txtResult_is_txtExpected(self):
    #     self.assertTrue(FilesAreEqual.compareFiles("files/textExtractor/txt_T2a_result.txt", "files/textExtractor/txt_T2a_expected.txt"))

    def test_T2b_txtResult_is_txtExpected(self):
        textExtractor.pdf_to_text('files/textExtractor/pdf_T2b_un substantiv.pdf')
        self.assertTrue(FilesAreEqual.compareFiles("files/textExtractor/pdf_T2b_un substantiv.txt", "files/textExtractor/pdf_T2b_un substantiv_expected.txt"))

    # Test 3
    # def test_T3a_txtResult_is_txtExpected(self):
    #     self.assertTrue(FilesAreEqual.compareFiles("files/textExtractor/txt_T3a_result.txt", "files/textExtractor/txt_T3a_expected.txt"))

    def test_T3b_txtResult_is_txtExpected(self):
        textExtractor.pdf_to_text('files/textExtractor/pdf_T3b_o propozitie.pdf')
        self.assertTrue(FilesAreEqual.compareFiles("files/textExtractor/pdf_T3b_o propozitie.txt", "files/textExtractor/pdf_T3b_o propozitie_expected.txt"))

    # Test 4
    # def test_T4a_txtResult_is_txtExpected(self):
    #     self.assertTrue(FilesAreEqual.compareFiles("files/textExtractor/txt_T4a_result.txt", "files/textExtractor/txt_T4a_expected.txt"))

    def test_T4b_txtResult_is_txtExpected(self):
        textExtractor.pdf_to_text('files/textExtractor/pdf_T4b_doua propozitii.pdf')
        self.assertTrue(FilesAreEqual.compareFiles("files/textExtractor/pdf_T4b_doua propozitii.txt", "files/textExtractor/pdf_T4b_doua propozitii_expected.txt"))

    # Test 5
    # def test_T5a_txtResult_is_txtExpected(self):
    #     self.assertTrue(FilesAreEqual.compareFiles("files/textExtractor/txt_T5a_result.txt", "files/textExtractor/txt_T5a_expected.txt"))

    def test_T5b_txtResult_is_txtExpected(self):
        textExtractor.pdf_to_text('files/textExtractor/pdf_T5b_doua paragrafe.pdf')
        self.assertTrue(FilesAreEqual.compareFiles("files/textExtractor/pdf_T5b_doua paragrafe.txt", "files/textExtractor/pdf_T5b_doua paragrafe_expected.txt"))

    # # Test 6
    # def test_T6a_txtResult_is_txtExpected(self):
    #     self.assertTrue(FilesAreEqual.compareFiles("files/textExtractor/txt_T6a_result.txt", "files/textExtractor/txt_T6a_expected.txt"))

    def test_T6b_txtResult_is_txtExpected(self):
        textExtractor.pdf_to_text('files/textExtractor/pdf_T6b_header+footer+text.pdf')
        self.assertTrue(FilesAreEqual.compareFiles("files/textExtractor/pdf_T6b_header+footer+text.txt", "files/textExtractor/pdf_T6b_header+footer+text_expected.txt"))

    # Test 7
    # def test_T7a_txtResult_is_txtExpected(self):
    #     self.assertTrue(FilesAreEqual.compareFiles("files/textExtractor/txt_T7a_result.txt", "files/textExtractor/txt_T7a_expected.txt"))

    def test_T7b_txtResult_is_txtExpected(self):
        textExtractor.pdf_to_text('files/textExtractor/pdf_T7b_header+footer.pdf')
        self.assertTrue(FilesAreEqual.compareFiles("files/textExtractor/pdf_T7b_header+footer.txt", "files/textExtractor/pdf_T7b_header+footer_expected.txt"))


if __name__ == '__main__':
    unittest.main()
