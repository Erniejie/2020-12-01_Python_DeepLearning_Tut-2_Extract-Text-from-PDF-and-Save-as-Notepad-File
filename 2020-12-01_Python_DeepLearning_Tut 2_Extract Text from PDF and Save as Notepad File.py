      # install pip-pymuPDF, first, to activate , fitz,

""" HOW TO EXTRACT TEXT FROM PDF AND SAVE AS NOTEPAD FILE: """
import fitz

pdf = fitz.open("RetireYoungRetireRich.pdf")
print(pdf.pageCount)

page = pdf.loadPage(27)
text = page.getText("text")

with open("pypage17.txt","w")as file:
    file.write(text.replace("\t",""))
pdf.close()
