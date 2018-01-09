import xml.etree.ElementTree as ET



def createXML(inputText, outputFile):
    idS = 0

    rootOutput = ET.Element("POS_Output")

    for sentence in inputText:
        idS = idS + 1
        tagS = []
        tagS.append(ET.SubElement(rootOutput, 'S', {'id': str(idS), 'offset': str(0)}))

        # Creating a list of sentence tags
        idW = 0

        # Word identification number idW
        for word in sentence:
            idW = idW + 1
            names = []
            values = []

            # Getting the Name : Value Pair from the POS atributs list
            names.append("word")
            values.append(word['word'])
            names.append("Lemma")
            values.append(word['lemma'])
            names.append('POS')
            values.append(word['pos'])

            # Adding received information : the word / the lemma / the POS
            dictionary = dict(zip(names, values))
            ET.SubElement(tagS[len(tagS) - 1], 'W', dictionary).text = word['word']

            # Creating the tags for Words
    output = ET.ElementTree(rootOutput)
    output.write(outputFile)


# createXML([
#
#            [ { 'word': 'cuvant', 'pos': 'Ncns-n', 'lemma': 'cuvant' } ]
#
#
# ], "files/xmlGenerator/cuvant.xml")