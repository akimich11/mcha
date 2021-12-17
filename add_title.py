# This takes a single PDF page from one PDF document and appends it to
# the front of an existing document, saving the new document as a new
# copy in another folder. Requires the pyPDF extension. You will also need to
# tell the script the location of the cover page, the folder that contains the
# PDF files to append it to, and an output folder for the modified files.

import os
import sys
from PyPDF2 import PdfFileReader, PdfFileWriter


if __name__ == '__main__':
	print("Beginning merge....")

	lab_number = sys.argv[1]
	output = PdfFileWriter()
	print("Processing title.pdf....")

	inputFile = f"title/title_lab_{lab_number}.pdf"
	input1 = PdfFileReader(open(inputFile, "rb"))
	output.addPage(input1.getPage(0))

	print("Processing lab.pdf....")
	inputFile = f"lab_{lab_number}.pdf"
	input2 = PdfFileReader(open(inputFile, "rb"))

	# add the rest of the pages to the PDf output
	for i in range(input2.getNumPages()):
		print("Adding page " + str(i) + "...", end='')
		output.addPage(input2.getPage(i))
		print("OK")

	# write the output file - change output folder as needed
	outputFile = f"pdf/ЛР{lab_number} 3к3гр Малыщик.pdf"
	outputStream = open(outputFile, "wb")
	print("Saving result....")
	output.write(outputStream)
	outputStream.close()

	print("Merge complete.")

