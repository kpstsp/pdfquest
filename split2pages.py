from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse
import os
import sys


parser=argparse.ArgumentParser(description='Process doc name/path')
parser.add_argument('--file')
parser.add_argument('--parts', type=int, default=2)
args=parser.parse_args()

print(args.file)
if not os.path.exists(args.file):
    sys.exit("Something goes wrong")


infile = args.file
pdf_str_file = open(infile, "rb")
inputpdf = PdfFileReader(pdf_str_file)


parts = args.parts
pagenum = inputpdf.numPages
print("Number of pages in original document = {}".format(pagenum))


#Get filename - "base" name
basename = infile.split(".")[0]


period = pagenum//parts
remns = pagenum % parts
n=0
m=0
cpart=0

def out_part(z, c, cpartp):
    output = PdfFileWriter()

    for i in range(z, c):
        inputpdf = PdfFileReader(pdf_str_file)
        # output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))
        # with open("document-page%s.pdf" % cpartp, "wb") as outputStream:
    # output.write("document-page{}.pdf".format(cpartp))
    with open("{}-{}.pdf".format(basename, cpartp), "wb") as outputStream:
        output.write(outputStream)
            # output.write(outputStream)
            # output.write(outputStream)


# def out_part(z, c, cpartp):
#     output = PdfFileWriter()

#     for i in range(z, c):
#         inputpdf = PdfFileReader(pdf_str_file)
#         # output = PdfFileWriter()
#         output.addPage(inputpdf.getPage(i))
#         # with open("document-page%s.pdf" % cpartp, "wb") as outputStream:
#     # output.write("document-page{}.pdf".format(cpartp))
#     with open("document-page{}.pdf".format(cpartp), "wb") as outputStream:
#         output.write(outputStream)
#             # output.write(outputStream)
#             # output.write(outputStream)



print("Current limit {}".format(pagenum-period))

while m<(pagenum-period):
    n=n+m
    m=m+period
    print("Period {} - {} . Limit is  {}".format(n, m, pagenum-period))
    out_part(n, m, cpart)
    cpart=cpart+1


print("n  {}".format(n))
#print remains
if remns>0:
    out_part(n, pagenum, cpart)


pdf_str_file.close()
