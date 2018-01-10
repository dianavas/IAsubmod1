#Acest script se foloseste pentru a sterge toate headerele si footerele din toate fisierele cu terminatia .doc si .docx 
#Mentionez faptul ca la ultima linie, se pune path-ul care contine acele fisiere .doc si .docx, si nu path-ul catre un anumit fisier

import os
import win32com
import win32com.client
 

def remove_headers_footers(fname):
    fname = os.path.abspath(fname)
    wapp = win32com.client.gencache.EnsureDispatch('Word.Application')
    wconst = win32com.client.constants
    wapp.Visible = 0
    doc = wapp.Documents.Open(fname)
    for section in wapp.ActiveDocument.Sections:
        section.Headers(wconst.wdHeaderFooterPrimary).Range.Text = ''
        section.Footers(wconst.wdHeaderFooterPrimary).Range.Text = ''
    doc.Save()
    doc.Close()
    wapp.Quit()
 
 
def batch_remove(path, suffix = ('doc', 'docx')):
    for root, dirs, fnames in os.walk(path):
        for name in fnames:
            if not name.startswith('~$') and name.endswith(suffix):
                remove_headers_footers(os.path.join(root, name))
 
 
#batch_remove('C:\\Users\\Daniell\\Desktop\\New folder\\')