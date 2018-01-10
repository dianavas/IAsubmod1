Contribuitori: Bivol Daniel-Silviu si Lungeanu Ionut

Pentru a apela toata munca noastra, se intra in fisierul convert.py care inglobeaza toate celelalte fisiere .py. Pe randul 21 
se pune path-ul unui folder care poate contine mai multe fisiere cu terminatii diferite. Daca aceste fisiere au terminatia .doc, .docx sau .pdf, sunt apelate functiile descrise mai jos astfel incat sa se obtina fisiere txt. Fisierele txt vor fi numite "filex", unde x este numarul fisierului citit care poate avea una din terminatiile specificate. Dupa ce se obtin fisiere txt pentru toate fisierele cu terminatiile specificate, se creeaza un nou folder numit "txtFiles" in care sunt mutate toate fisierele cu terminatia .txt.

ATENTIE: nu se pune path-ul unui fisier, ci path-ul unui folder care contine acel fisier, astfel incat, daca acel folder contine mai multe fisiere, sa se obtina fisiere .txt pentru fiecare din acele fisiere

EXEMPLU: daca intr-un folder vom avea 2 fisiere: unu.docx si doi.pdf, in urma apelarii functiei din convert.py, tot in acel folder se va crea un nou folder numit: "txtFiles" in care vor aparea "file1.txt" si "file2.txt"

In fisierele: "text_from_text", "text_from_docx", "text_from_pdf" sunt functii ce primesc ca parametru calea unui fisier si returneaza continutul lui intr-un fisier cu extensia txt.

Fisierul "docx_from_doc" contine o functie ce primeste calea unui fisier si converteste un fisier de tip doc intr-un fisier de tip docx

Fisierul "delete_headersAndFooters_fromDocAndDOCX" se foloseste pentru a sterge toate headerele si footerele din fisierele cu terminatia .doc si .docx, pentru ca ar fi imposibil
pentru cei din P2 sa faca asta din fisierul txt pe care noi il dam lor

Fisierul "testfile.txt" este rezultatul apelarii functiei din "Convert.py" pe un fisier de tip pdf

In folderul "Exemple" se vor gasi 3 foldere cu exemple, iar ca un exemplu final, se gaseste in folderul Exemplu_Final in care sunt alte 2
foldere: Before si After. In folderul Before sunt 3 fisiere cu terminatiile: .doc, .docx si .pdf, iar in fisierul After sunt fisierele 
rezultate in urma apelarii functiei convert pe fisierul Before.

Aceasta parte din proiect a fost realizata in python, versiunea 2.7.14, 32 biti