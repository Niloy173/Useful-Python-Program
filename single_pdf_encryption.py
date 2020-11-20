# a single file encryption

# .pdf and .py file needs to be the same path

import PyPDF2

pdfReader = PyPDF2.PdfFileReader(open("new_.pdf","rb"))

pdfwriter = PyPDF2.PdfFileWriter()

for page in range(pdfReader.numPages):
    pdfwriter.addPage(pdfReader.getPage(page))

pdfwriter.encrypt("1234")

result = open("encrypt_new_.pdf","wb")
pdfwriter.write(result)
result.close()
