import unittest
import FilesAreEqual
import Test_xmlGenerator

# codTest: aa.bb.cc, unde:
#   a =
#       N - 00 - Substantiv, unde bb =
#               - 00 - comun
#               - 01 - propriu
#               - 10 - masculin
#               - 11 - feminin
#               - 12 - neutru
#               - 20 - singular
#               - 21 - plural
#               - 31 - case ??
#               - 32 - case ??
#               - 33 - case ??
#               - 34 - case ??
#               - 40 - definition: no
#               - 41 - definiton: yes
#       V - 01 - Verb
#       P - 02 - Pronume
#       A - 03 - Adjectiv
#       D - 04 - Determiner
#       A - 05 - Article
#       R - 06 - Adverb
#       S - 07 - Adposition
#       C - 08 - Conjunctie
#       M - 09 - Numeral
#       Q - 10 - Particle
#       I - 11 - Interjectie
#       Y - 12 - Abreviere
#       X - 13 - Residual

class MyTestCase(unittest.TestCase):
    # Test Substantiv, comun, masculin, singular, fara case, Nu definitie
    def test_Noun_common_masculine_singular___No(self):
        Test_xmlGenerator.createXML([[{'word': 'baiat', 'pos': 'Ncms-n', 'lemma': 'baiat'}]],
                                    'files/xmlGenerator/xml_0001_Ncms-n_result.xml')
        Test_xmlGenerator.createXML([[{'word': 'baiat', 'pos': 'Ncms-n', 'lemma': 'baiat'}]],
                                    'files/xmlGenerator/xml_0001_Ncms-n_expected.xml')
        self.assertTrue(FilesAreEqual.compareXMLs("files/xmlGenerator/xml_0001_Ncms-n_result.xml",
                                                  "files/xmlGenerator/xml_0001_Ncms-n_expected.xml"))

    # Test Substantiv, comun, masculin, plural, fara case, Nu definitie
    def test_Noun_common_masculine_plural___No(self):
        Test_xmlGenerator.createXML([[{'word': 'baieti', 'pos': 'Ncmp-n', 'lemma': 'baiat'}]],
                                    'files/xmlGenerator/xml_0002_Ncmp-n_result.xml')
        Test_xmlGenerator.createXML([[{'word': 'baieti', 'pos': 'Ncmp-n', 'lemma': 'baiat'}]],
                                    'files/xmlGenerator/xml_0002_Ncmp-n_expected.xml')
        self.assertTrue(FilesAreEqual.compareXMLs("files/xmlGenerator/xml_0002_Ncmp-n_result.xml",
                                                  "files/xmlGenerator/xml_0002_Ncmp-n_expected.xml"))

    # Test Substantiv, comun, feminin, singular, fara case, Nu definitie
    def test_Noun_common_feminine_singular___No(self):
        Test_xmlGenerator.createXML([[{'word': 'casa', 'pos': 'Ncfs-n', 'lemma': 'casa'}]],
                                        'files/xmlGenerator/xml_0003_Ncfs-n_result.xml')
        Test_xmlGenerator.createXML([[{'word': 'casa', 'pos': 'Ncfs-n', 'lemma': 'casa'}]],
                                        'files/xmlGenerator/xml_0003_Ncfs-n_expected.xml')
        self.assertTrue(FilesAreEqual.compareXMLs("files/xmlGenerator/xml_0003_Ncfs-n_result.xml",
                                                      "files/xmlGenerator/xml_0003_Ncfs-n_expected.xml"))

    # Test Substantiv, comun, feminin, plural, fara case, Nu definitie
    def test_Noun_common_feminine_plural___No(self):
        Test_xmlGenerator.createXML([[{'word': 'case', 'pos': 'Ncfp-n', 'lemma': 'casa'}]],
                                        'files/xmlGenerator/xml_0004_Ncfp-n_result.xml')
        Test_xmlGenerator.createXML([[{'word': 'case', 'pos': 'Ncfp-n', 'lemma': 'casa'}]],
                                        'files/xmlGenerator/xml_0004_Ncfp-n_expected.xml')
        self.assertTrue(FilesAreEqual.compareXMLs("files/xmlGenerator/xml_0004_Ncfp-n_result.xml",
                                                      "files/xmlGenerator/xml_0004_Ncfp-n_expected.xml"))

    # Test Substantiv, propriu, fara gen, singular, fara case, Nu definitie
    def test_Noun_proper___singular___No(self):
        Test_xmlGenerator.createXML([[ { 'word': 'Romania', 'pos': 'Np-s-n', 'lemma': 'Romania' } ]], 'files/xmlGenerator/xml_0000_Np-s-n_result.xml')
        Test_xmlGenerator.createXML([[ { 'word': 'Romania', 'pos': 'Np-s-n', 'lemma': 'Romania'} ]], 'files/xmlGenerator/xml_0000_Np-s-n_expected.xml')
        self.assertTrue(FilesAreEqual.compareXMLs("files/xmlGenerator/xml_0000_Np-s-n_result.xml",
                                                  "files/xmlGenerator/xml_0000_Np-s-n_expected.xml"))


if __name__ == '__main__':
    unittest.main()
