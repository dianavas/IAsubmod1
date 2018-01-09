# Install Python 2.4 or newer. (Python 3 is not supported.)
# Download the PDFMiner source. http://www.unixuser.org/~euske/python/pdfminer/index.html#source
# Unpack it.
# Run setup.py to install: -> python setup.py install


from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import os


def pdf_to_text(fileName):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(fileName, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    newFile = os.path.splitext(fileName)[0] + '.txt'
    file_to_write = open(newFile, "w")
    file_to_write.write(text)

    fp.close()
    device.close()
    retstr.close()
    file_to_write.close()

#pdf_to_text('C:\\Users\\Daniell\\Desktop\\Text from pdf and docx\\lesson2.pdf')
