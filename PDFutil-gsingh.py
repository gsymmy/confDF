#Program to combine the 7th page of every PDF in a directory.
#author- Gursimran Singh (gsingh@gatech.edu) / https://github.com/gursimransingh93


#Requirements:

#Install PyPDF2 module for Python(3) (Mac users: pip install PyPDF2 on Terminal)
#A blank.pdf blank file has been uplaoded with this program. Keep that file in the same directory.


#Instructions:

#Save this program in the same directory where the PDFs are stored.
#Change the directory location in the program where --/add/your/directory/location/here-- is written.
#Run the program
#Multiple 7th page PDFs will be created, ignore them or delete after running the program.
#Open combined.pdf

import os
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
directory = '/Users/gursimransingh/Desktop/testpdf'
for filename in os.listdir(directory):
    if filename.endswith(".pdf"):
        try:
            inputpdf = PdfFileReader(open(filename, "rb"))
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(6))
            with open("pg07%sgsingh.pdf" % filename[:-4], "wb") as outputStream:
                output.write(outputStream)
        except:
            continue
    else:
        continue

merger = PdfFileMerger()
merger.append(PdfFileReader(open("blank.pdf", 'rb')))
for file in os.listdir(directory):
    if file.endswith("gsingh.pdf"):
        try:
            merger.append(PdfFileReader(open(file, 'rb')))
        except:
            continue
    else:
        continue

merger.write("combined.pdf")





