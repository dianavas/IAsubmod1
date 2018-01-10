#Aceasta functie primeste calea unui folder, care poate contine mai multe fisiere de diferite tipuri. Daca aceste fisiere au
#terminatia .doc, .docx sau .pdf se apeleaza diferite functii, astfel incat, pentru fiecare fisier cu una din terminatiile specificate,
#sa se obtina cate un fisier cu terminatia .txt. Fisierele txt vor fi numite "filex", unde x este numarul fisierului care poate avea una din terminatiile specificate.
#Dupa ce se obtin fisiere txt pentru toate fisierele cu terminatiile specificate, se creeaza un nou folder numit "txtFiles" in care sunt mutate toate fisierele
#cu terminatia .txt

#Pentru fisierele .doc si .docx se mai apeleaza o functie care verifica si sterge daca acestea au headere sau footere, pentru ca altfel, ar
#fi imposibil pentru cei din P2 sa faca diferenta dintre headere/footere fata de restul textului din fisierul cu terminatia .txt rezultat

#ATENTIE: se primeste calea unui folder care poate contine mai multe fisiere, si nu calea unui fisier! A se respecta forma path-ului de pe randul 21
#Pe randul 21 se adauga path-ul dorit

import delete_headersAndFooters_fromDocAndDocx
import text_from_pdf
import text_from_docx
import docx_from_doc
import text_from_text
import shutil
import os


file_path = 'C:\\Users\\Daniell\\Desktop\\Text from pdf and docx\\'
directory = file_path
folder = 'txtFiles'


def ConvertFile(file_path): 
    files = os.listdir(directory)
    
    if not os.path.exists(folder):
        os.makedirs(folder)

    nr = 1
    name = 'file'
    

    delete_headersAndFooters_fromDocAndDocx.batch_remove(file_path)
    
    for file in files:
        if file.endswith('.docx'):
            text_from_docx.docx_to_txt((file_path + file), (name + str(nr) + '.txt'))
            nr += 1
        elif file.endswith('.doc'):
            docx_from_doc.doc_to_docx(file_path + file)
            file = file + 'x'
            text_from_docx.docx_to_txt((file_path + file), (name + str(nr) + '.txt'))
            nr += 1
            os.remove(file_path + file)
        elif file.endswith('.pdf'):
            text_from_pdf.pdf_to_text((file_path + file), (name + str(nr) + '.txt'))
            nr += 1
    

ConvertFile(file_path)


files = os.listdir(directory)
for file in files:
        if file.endswith('.txt'):
            shutil.move((file_path + file), (file_path + folder)) 


