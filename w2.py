from PyPDF2 import PdfReader as pdfr
reader = pdfr("ViteshW2.pdf")
num_of_pages = len(reader.pages)
# print(num_of_pages)
page = reader.pages[0]
text = page.extract_text()
print(text)

import nltk
from nltk.tokenize import word_tokenize
words = word_tokenize(text)
# print(words)

import re

address = re.compile(r'''(\w+,+\n+\w+\n+\d\d\d\d\d+\n+\d\d\d+\n+\w+\n+\w+\n+\w
)
''', re.VERBOSE)
addresses = address.findall(text)
if (len(addresses) > 0):
    print('Employee Address: ', addresses[len(addresses)-1])





# address = re.compile(r'''(^(\d+) ?([A-Za-z](?= ))? (.*?) ([^ ]+?) ?((?<= )APT)? ?((?<= )\d*)?
# )
# ''', re.VERBOSE)
# address = re.compile(r'''(\d\d\d + \n + (\w+\n+\w+\n+\w)
# )
# ''', re.VERBOSE)

# import fitz
# import pandas as pd
# doc = fitz.open('ViteshW2.pdf')
# page1 = doc[0]
# words = page1.get_text("words")
# print(words)
#
# def make_text(words):
#     line_dict = {}
#     words.sort(key=lambda w: w[0])
#     for w in words:
#         y1 = round(w[3], 1)
#         word = w[4]
#         line = line_dict.get(y1, [])
#         line.append(word)
#         line_dict[y1] = line
#     lines = list(line_dict.items())
#     lines.sort()
#     print("n".join([" ".join(line[1]) for line in lines]))


# address = 'Name'
# address_return = []
# for i in words:
#     if i == address:
#         address_return.append(i)
#
#
# print(address_return)

# import textract
# text2 = textract.process("ViteshW2.pdf")
# print(text2)