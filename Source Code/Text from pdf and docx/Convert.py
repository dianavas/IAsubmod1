#Aceasta functie primeste calea unui fisier, iar in functie de extensia pe care o are, se apeleaza functiile create pentru a returna un fisier cu extensia txt

import delete_headersAndFooters_fromDocAndDocx
import text_from_pdf
import text_from_docx
import docx_from_doc
import text_from_text
import os


def ConvertFile(file_path):

    #Pe urmatoarea linie de cod, intre paranteze, se va pune path-ul folderului care contine fisierul respectiv
    delete_headersAndFooters_fromDocAndDocx.batch_remove('C:\\Users\\Daniell\\Desktop\\IAsubmod1\\Source Code\\Text from pdf and docx\\')

    extension = os.path.splitext(file_path)[-1].lower()

    if extension == ".pdf":
        text_from_pdf.pdf_to_text(file_path)
    elif extension == ".docx":
        text_from_docx.docx_to_txt(file_path)
    elif extension == ".txt":
        text_from_text.txt_to_txt(file_path)
    elif extension == ".doc":
        docx_from_doc.doc_to_docx(file_path)
        file_path = file_path + 'x'
        text_from_docx.docx_to_txt(file_path)
    else:
        return exit(1)

#ConvertFile('C:\\Users\\Daniell\\Desktop\\IAsubmod1\\Source Code\\Text from pdf and docx\\edited.docx')
#ConvertFile('C:\\Users\\ionut\\Documents\\GitHub\\IAsubmod1\\Sample Files\\GeneralBiology.pdf')
#ConvertFile('C:\\Users\\Daniell\\Python\\Test\\AI\\sample.doc')
#ConvertFile('C:\\Users\\Daniell\\Python\\Test\\AI\\fisierText.txt')

