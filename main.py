from PyPDF2 import PdfReader
import json

reader = PdfReader("table.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
# print(text)
jsDic = json.dumps(text)
jso = json.loads(jsDic)
print(type(jso))
# print(json_object)