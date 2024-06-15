#!/usr/bin/env python3

import sys
from pdf2image import convert_from_path

#images = convert_from_path(file, poppler_path=r"C:\Python\poppler\poppler-23.07.0\Library\bin")

if __name__ == '__main__':
    pdfFilePath = sys.argv[1]
    if not pdfFilePath.endswith('.pdf'):
        print("invalid pdf file:%s" % pdfFilePath)
        sys.exit

    images = convert_from_path(pdfFilePath)

    filePrefix = pdfFilePath[0:-4]
    for i in range(len(images)):
        images[i].save(f'./%s_{i+1}.png' % filePrefix, 'PNG')
