import xml.etree.ElementTree as ET

inputTextEx = [
                [
                    {'word': 'Ana', 'pos': 'Np', 'lemma': 'Ana'},
                    {'word': 'are', 'pos': 'Vmip3s', 'lemma': 'avea'},
                    {'word': 'mere', 'pos': 'Ncfp-n', 'lemma': 'mar'},
                    {'word': '.', 'pos': 'SENT', 'lemma': '.'}
                ],
                [
                    {'word': 'Cate', 'pos': 'Dw3fpr', 'lemma': 'cat'},
                    {'word': 'mere', 'pos': 'Ncfp-n', 'lemma': 'mar'},
                    {'word': 'are', 'pos': 'Vmip3s', 'lemma': 'avea'},
                    {'word': 'Ana', 'pos': 'Np', 'lemma': 'Ana'},
                    {'word': '?', 'pos': 'SENT', 'lemma': '?'}
                ]
            ]

# Generator function
def Generator(inputText):
    parsePOSLib = ET.parse('POSroLib.xml')
    rootInput = parsePOSLib.getroot()

    rootOutput = ET.Element("POS_Output")
    idS = 0
    # Sentence identification number idS

    for sentence in inputText:
        idS = idS +1
        tagS = []
        tagS.append(ET.SubElement(rootOutput,'S',{'id' : str(idS),'offset' : str(0)}))
        # Creating a list of sentence tags
        idW = 0
        # Word identification number idW
        for word in sentence:
            idW = idW + 1
            for types in rootInput[1]:
                if types.get('{http://www.w3.org/XML/1998/namespace}id') == word['pos']:
                    atributes = types.get('feats')
                    # Getting the Feats from the POS types file
            atributeList = []
            atributeList = atributes.split(' ')
            # Getting the atributs from POS form character by character
            names = []
            values = []
            for atribute in atributeList:
                for child in rootInput[0]:
                    if  '#'+child.get('{http://www.w3.org/XML/1998/namespace}id') == atribute:
                        names.append(child.get('name'))
                        values.append(child[0].get('value'))
            # Getting the Name : Value Pair from the POS atributs list
            names.append("word")
            values.append(word['word'])
            names.append("Lemma")
            values.append(word['lemma'])
            names.append('POS')
            values.append(word['pos'])
            # Adding received information : the word / the lemma / the POS
            dictionary = dict(zip(names,values))
            ET.SubElement(tagS[len(tagS)-1], 'W', dictionary).text = word['word']
            # Creating the tags for Words
    output = ET.ElementTree(rootOutput)
    output.write("output.xml")
# Creating the output.xml

Generator(inputTextEx)
# call