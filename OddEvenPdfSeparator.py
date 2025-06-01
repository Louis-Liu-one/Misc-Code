

import sys
import PyPDF4

helpInfo = '''
Usages:
  python3 OddEvenPdfSeparator.py
    <source>.pdf <odd pages>.pdf <even pages>.pdf
  python3 OddEvenPdfSeparator.py -h/--help

Separate the <source>.pdf to odd and even pages, which are in
<odd pages>.pdf and <even pages>.pdf separately.

All the pages of <even pages>.pdf will be rotated through 180
degrees, and the order of the pages will be reversed. Besides,
a blank page will be added to match each even page to an odd
page.'''

def processPages(sourceName):
    oddPages, evenPages = [], []
    pdfReader = PyPDF4.PdfFileReader(sourceName)
    NumPages = pdfReader.getNumPages()
    for pageNum in range(NumPages):
        pdfReader = PyPDF4.PdfFileReader(sourceName)
        page = pdfReader.getPage(pageNum)
        if pageNum % 2:
            evenPages.append(page.rotateClockwise(180))
        else:
            oddPages.append(page)
        print('\rPage {}/{}'.format(pageNum + 1, NumPages), end='')
    evenPages.reverse()
    size = pdfReader.getPage(0).mediaBox
    width, height = size.getUpperRight_x(), size.getUpperRight_y()
    return oddPages, evenPages, NumPages % 2, width, height


def writePages(pdfWriter, pages):
    for page in pages:
        pdfWriter.addPage(page)


def main(sourceName, oddName, evenName):
    oddPages, evenPages, isOddPages, width, height \
        = processPages(sourceName)
    with open(oddName, 'wb') as oddFile, \
            open(evenName, 'wb') as evenFile:
        pdfWriterOdd = PyPDF4.PdfFileWriter()
        pdfWriterEven = PyPDF4.PdfFileWriter()
        if isOddPages:
            pdfWriterEven.addBlankPage(width, height)
        print('\rSaving ...  ')
        writePages(pdfWriterOdd, oddPages)
        writePages(pdfWriterEven, evenPages)
        pdfWriterOdd.write(oddFile)
        pdfWriterEven.write(evenFile)


if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] in ('-h', '--help'):
        print(helpInfo)
    else:
        main(*sys.argv[1:4])
