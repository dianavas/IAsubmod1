Voi scrie aici ce am reusit noi 2 sa facem pana acum:

In fisierele: "text_from_text", "text_from_docx", "text_from_pdf" sunt functii ce primesc ca parametru calea unui fisier si returneaza continutul lui 
intr-un fisier cu extensia txt.

Fisierul "docx_from_doc" contine o functie ce primeste calea unui fisier si converteste un fisier de tip doc intr-un fisier de tip docx

Fisierul "delete_headersAndFooters_fromDocAndDOCX" se foloseste pentru a sterge toate headerele si footerele din fisierele cu terminatia .doc si .docx, pentru ca ar fi imposibil
pentru cei din P2 sa faca asta din fisierul txt pe care noi il dam lor

Fisierul "Convert.py" inglobeaza toate fisierele de mai sus, contine o functie ce primeste ca paramentru calea unui fisier, iar in functie de extensia
acestuia, se apeleaza functiile din fisierele precizate mai sus pentru a transforma acel fisier intr-unul de tip txt

Fisierul "testfile.txt" este rezultatul apelarii functiei din "Convert.py" pe un fisier de tip pdf

In folderul "Exemple" se vor gasi 2 exemple in urma apelarii functiei "convert" pe fisiere cu terminatia .docx si .doc.

