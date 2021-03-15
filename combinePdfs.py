#!python3
'''
    combinePdfs.py - combina todos os PDFs do diretório de trabalho atual em um único PDF
'''
import PyPDF2, os

pdfFiles = []
path = './combinandoarquivospdf/'
for filename in os.listdir('./combinandoarquivospdf/'):
    if filename.endswith('.pdf'):
        pdfFiles.append(filename)
pdfFiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdfFiles:
    filename = path + filename
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    if pdfReader.isEncrypted and 'Claro' in filename:
        pdfReader.decrypt('85745')
    elif pdfReader.isEncrypted:
        pdfReader.decrypt('857')
    
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    
    pdfFileObj.close()

outputFilename = path + 'recibos.pdf'
pdfOutput = open(outputFilename,'wb')
pdfWriter.write(pdfOutput)

pdfOutput.close()
