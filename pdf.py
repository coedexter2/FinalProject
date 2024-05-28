from PyPDF2 import PdfReader

reader = PdfReader("C:/Users/coede/OneDrive/Documents/GitHub/FinalProject/R48075.pdf")
page = reader.pages[6]
text = page.extract_text()

print(text)