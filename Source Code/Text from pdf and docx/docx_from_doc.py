# Vom crea o functie care primeste ca parametru calea fisierului cu extensia doc, care il va converti intr-un fisier cu extensia docx
# Pentru aceasta va fi nevoie de libraria pywin32

# Pentru a instala aceasta librarie se vor urma urmatorii pasi:
# 1. se deschide cmd ca administrator;
# 2. se ruleaza comanda: "pip install pypiwin32";


import win32com.client
import os


def doc_to_docx(filePath):

    wrd = win32com.client.Dispatch("Word.Application")
    wrd.visible = 0
    wb = wrd.Documents.Open(filePath)

    filePath = filePath + 'x'

    wb.SaveAs(filePath, FileFormat = 12)

    wb.Close()
    wrd.Quit()


#doc_to_docx('C:\\Users\\Daniell\\Python\\Test\\AI\\sample.doc')

