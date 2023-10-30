from docx import Document

doc = Document("bijoy.docx")
text = ""
for paragraph in doc.paragraphs:
    text += paragraph.text + "\n"

with open("bijoy.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(text)
