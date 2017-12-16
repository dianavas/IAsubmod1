#Pentru a extrage textul dintr-un document cu extensia docx vom folosi libraria "textract".
#Pentru a instala aceasta librarie se vor urma urmatorii pasi:
#1. se deschide cmd ca administrator;
#2. se ruleaza comanda: "pip install textract";

#Vom crea o functie care primeste ca parametru calea fisierului cu extensia docx care va scrie continutul intr-un fisier text.

import textract

def docx_to_txt(fileName):
    docx_file = open(fileName, 'r')
    fileToWrite = open("FisierText.txt", "w")
    
    text = textract.process(fileName)

    fileToWrite.write(text)
  

#docx_to_txt('C:\\Users\\Daniell\\Python\\Test\\AI\\demo.docx')