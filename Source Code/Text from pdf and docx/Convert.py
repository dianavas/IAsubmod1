#Aceasta functie primeste calea unui folder, care poate contine mai multe fisiere de diferite tipuri. Daca aceste fisiere au
#terminatia .doc, .docx sau .pdf se apeleaza diferite functii, astfel incat, pentru fiecare fisier cu una din terminatiile specificate,
#sa se obtina cate un fisier cu terminatia .txt

#Pentru fisierele .doc si .docx se mai apeleaza o functie care verifica si sterge daca acestea au headere sau footere, pentru ca altfel, ar
#fi imposibil pentru cei din P2 sa faca diferenta dintre headere/footere fata de restul textului din fisierul cu terminatia .txt rezultat

#ATENTIE: se primeste calea unui folder care poate contine mai multe fisiere, si nu calea unui fisier! A se respecta forma din ultimul comentariu

import delete_headersAndFooters_fromDocAndDocx
import text_from_pdf
import text_from_docx
import docx_from_doc
import text_from_text
import os


def ConvertFile(file_path):
    directory = file_path
    files = os.listdir(directory)

    delete_headersAndFooters_fromDocAndDocx.batch_remove(file_path)
    
    for file in files:
        if file.endswith('.docx'):
            text_from_docx.docx_to_txt(file_path + file)
        elif file.endswith('.doc'):
            docx_from_doc.doc_to_docx(file_path + file)
            file = file + 'x'
            text_from_docx.docx_to_txt(file_path + file)
        elif file.endswith('.pdf'):
            text_from_pdf.pdf_to_text(file_path + file)


#ConvertFile('C:\\Users\\Daniell\\Desktop\\Text from pdf and docx\\')
