
# Vom crea o functie care primeste ca parametru calea fisierului cu extensia txt care va scrie continutul intr-un fisier text.


def txt_to_txt(fileName):
    docx_file = open(fileName, 'r')
    fileToWrite = open("FisierText.txt", "w")
    
    for line in docx_file.readlines():
        fileToWrite.write(line)