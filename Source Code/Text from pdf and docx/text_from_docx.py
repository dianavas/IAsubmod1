# Pentru a extrage textul dintr-un document cu extensia docx vom folosi libraria "textract".
# Pentru a instala aceasta librarie se vor urma urmatorii pasi:
# 1. se deschide cmd ca administrator;
# 2. se ruleaza comanda: "pip install textract";

# Vom crea o functie care primeste ca parametru calea fisierului cu extensia docx care va scrie continutul intr-un fisier text.

import textract
import os


def docx_to_txt(fileName, nume): 
    newFile = os.path.splitext(fileName)[0] + '.txt'
    fileToWrite = open(nume, "w")

    text = textract.process(fileName, encoding = "utf-8")

    fileToWrite.write(text)
