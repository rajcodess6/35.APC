from PyPDF2 import PdfMerger

m = PdfMerger()
m.append("file1.pdf")
m.append("file2.pdf")
m.write("merged.pdf")
m.close()

print("PDFs merged successfully!")