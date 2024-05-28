
from django.shortcuts import render, redirect
from .forms import UploadFileForm 
from PyPDF2 import PdfReader, PdfWriter
import os
import glob

  
def handle_uploaded_file(f):   
    with open('app/upload/' +f.name, 'wb+') as destination:   
        for chunk in f.chunks(): 
            destination.write(chunk)   


def input(request): 
    context = {} 
    if request.POST: 
        form = UploadFileForm(request.POST, request.FILES) 
        if form.is_valid(): 
            handle_uploaded_file(request.FILES["file"]) 
            return redirect("waiting_name")
    else: 
        form = UploadFileForm() 
    context['form'] = form 
    return render(request, "index.html", context) 

def waiting(request):
    folder = 'app/upload/'
    
    file = glob.glob(os.path.join(folder, "*.pdf"))
    reader = PdfReader(file[0])
    
    number_of_pages = len(reader.pages)
    
    output = ''
    for i in number_of_pages:
        page = reader.pages[i]
        text = page.extract_text()
        if '.....' in text:
            pass
        else: 
            output = output + text
                
        
