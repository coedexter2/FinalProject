from PyPDF2 import PdfReader


path= 'C:/Users/coede/OneDrive/Documents/GitHub/FinalProject/R47390.pdf'

with open(path, 'rb') as pdf_file:
    reader = PdfReader(pdf_file)

    full_text = ""
    
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text = page.extract_text()
        if 'https://crsreports.congress.gov' in text or '.............................' in text:
            pass
            
        elif 'Appendix.' in text:
            break
        else:
            full_text += text + "\n"
       
    lines = full_text.splitlines(keepends=True)     
    new_Lines = []
    

    for line in lines:
        if 'Congressional Research Service' not in line or 'Source:' not in line or 'Note:':
           new_Lines.append(line)
           
    new_string = " ".join(new_Lines)
    print(new_string)
        
