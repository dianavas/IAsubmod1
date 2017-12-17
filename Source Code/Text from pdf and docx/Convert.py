import text_from_pdf
import text_from_docx
import os


def ConvertFile(file_path):
    extension = os.path.splitext(file_path)[-1].lower()

    if extension == ".pdf":
        text_from_pdf.pdf_to_text(file_path)
    elif extension == ".docx":
        text_from_docx.docx_to_txt(file_path)
    # de adaugat doc_to_txt si txt_to_txt..
    else:
        return exit(1)

ConvertFile('C:\\Users\\ionut\\Documents\\GitHub\\IAsubmod1\\Sample Files\\GeneralBiology.pdf')
