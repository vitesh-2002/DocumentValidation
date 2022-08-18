'''convert PDF into PNG'''
# from pdf2image import convert_from_path
# images = convert_from_path("ViteshW2.pdf")
# for image in images:
#     image.save('W2.png', 'PNG')


import sys
original = sys.argv[1]
target   = original[:-4] + '.cropped.pdf'
left     = int(sys.argv[2])
top      = int(sys.argv[3])
right    = int(sys.argv[4])
bottom   = int(sys.argv[5])

from PyPDF2 import PdfFileWriter, PdfFileReader
pdf = PdfFileReader(('ViteshW2.pdf', 'rb'))
out = PdfFileWriter()
for page in pdf.pages:
  page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x() - right, page.mediaBox.getUpperRight_y() - top)
  page.mediaBox.lowerLeft  = (page.mediaBox.getLowerLeft_x()  + left,  page.mediaBox.getLowerLeft_y()  + bottom)
  out.addPage(page)
ous = (target, 'wb')
out.write(ous)
ous.close()
# if __name__ == '__main__' and len(sys.argv) > 5 and sys.argv[1][-3:].upper() == 'PDF':
#   original = sys.argv[1]
#   target   = original[:-4] + '.cropped.pdf'
#   left     = int(sys.argv[2])
#   top      = int(sys.argv[3])
#   right    = int(sys.argv[4])
#   bottom   = int(sys.argv[5])
#
#   from pyPdf import PdfFileWriter, PdfFileReader
#   pdf = PdfFileReader(('ViteshW2.pdf', 'rb'))
#   out = PdfFileWriter()
#   for page in pdf.pages:
#     page.mediaBox.upperRight = (page.mediaBox.getUpperRight_x() - right, page.mediaBox.getUpperRight_y() - top)
#     page.mediaBox.lowerLeft  = (page.mediaBox.getLowerLeft_x()  + left,  page.mediaBox.getLowerLeft_y()  + bottom)
#     out.addPage(page)
#   ous = (target, 'wb')
#   out.write(ous)
#   ous.close()
#
# else:
#   print('EXAMPLE: pdfcrop.py original.pdf 20 30 20 40')


'''crop margins from PDF file'''
# from pdfCropMargins import crop
# crop(["-p", "20", "-u", "-s", "ViteshW2.pdf"])

# from PDFNetPython3 import *
# from PDFNetPython3.PDFNetPython import PDFDoc, Rect
#
# doc = PDFDoc('ViteshW2.pdf')
# page = doc.GetPage(1)
# page.SetCropBox(Rect(0, 0, 500, 600))


'''convert pdf into grid'''
# from PIL import Image
# im = Image.open(r"C:\Users\vites\pythonProjects\W2_Reader\W2.png")
# im1 = Image.Image.split(im)
# im1[0].show()


'''parse grid section'''
# from PyPDF2 import PdfReader as pdfr
# reader = pdfr("ViteshW2.pdf")
# num_of_pages = len(reader.pages)
# # print(num_of_pages)
# page = reader.pages[0]
# text = page.extract_text()
# print(text)
#
# import nltk
# from nltk.tokenize import word_tokenize
# words = word_tokenize(text)
# # print(words)
#
# import re
#
# address = re.compile(r'''(\w+,+\n+\w+\n+\d\d\d\d\d+\n+\d\d\d+\n+\w+\n+\w+\n+\w
# )
# ''', re.VERBOSE)
# addresses = address.findall(text)
# if (len(addresses) > 0):
#     print('Employee Address: ', addresses[len(addresses)-1]).