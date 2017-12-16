#Pentru a extrage textul dintr-un document pdf vom folosi libraria PyPDF2 pt Python3.6.2
# pentru a instala libraria PyPDF2 vom urma urmatorii pasi:
#1. deschid cmd ca administrator
#2. rulez comanda pip install PyPDF2

import PyPDF2

#vom crea o functie care primeste ca parametru calea fisierului pdf, si va scrie continutul intr-un fisier text.

def pdf_to_text(file_name):

    pdf_file = open(file_name,'rb')
    file_to_write = open("testfile.txt","w")
    pdfReader = PyPDF2.PdfFileReader(pdf_file)

    for i in range(0,pdfReader.numPages):
        file_to_write.write(pdfReader.getPage(i).extractText())

#print(pdf_to_text('C:\\Users\\ionut\\Documents\\GitHub\\IAsubmod1\\Source Code\\Text from pdf and doc\\Curs-1.pdf'))