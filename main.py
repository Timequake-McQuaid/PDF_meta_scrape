from PyPDF2 import PdfFileReader

with open('file_name.pdf', 'rb') as file:
    pdf_read = PdfFileReader(file)
    pdf_info = pdf_read.getDocumentInfo()
    print(pdf_info)
