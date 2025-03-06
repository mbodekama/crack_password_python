import PyPDF2

pdf_file = open('ANONOPS_The_Press_Release.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)
doc_info = pdf_reader.metadata
for  info in doc_info:
    print(info, doc_info[info])