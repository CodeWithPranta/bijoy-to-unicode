from docx import Document

with open("unicode.txt", "r", encoding="utf-8") as txt_file:
    text = txt_file.read()

doc = Document()
doc.add_paragraph(text)

doc.save("unicode.docx")
