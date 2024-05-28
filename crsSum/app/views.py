
from django.shortcuts import render, redirect
from .forms import UploadFileForm 
from PyPDF2 import PdfReader
import os
import glob
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def handle_uploaded_file(f):   
    with open('app/upload/' +f.name, 'wb+') as destination:   
        for chunk in f.chunks(): 
            destination.write(chunk)   


def input(request): 
    file = glob.glob(os.path.join('app/upload/', "*.pdf"))
    
    if file:
        try:
            os.remove(file[0])
        except FileNotFoundError:
            pass
        
    context = {} 
    if request.POST: 
        form = UploadFileForm(request.POST, request.FILES) 
        if form.is_valid(): 
            handle_uploaded_file(request.FILES["file"]) 
            return redirect("results_name")
    else: 
        form = UploadFileForm() 
    context['form'] = form 
    return render(request, "index.html", context) 

def results(request):
    file = glob.glob(os.path.join('app/upload/', "*.pdf"))
    
    with open(file[0], 'rb') as pdf_file:
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
        
        
    token = ''
    login = token
    tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it", token=login)
    model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2b-it",
    torch_dtype=torch.bfloat16, token=login)

    
    input_text ='summerize: ' + new_string
    
    input_ids = tokenizer(input_text, return_tensors="pt")

    outputs = model.generate(**input_ids,
        max_length=30000)
    
    summary = tokenizer.decode(outputs[0])
    
    prompt_length = len(input_text)
    
    output_without_prompt = summary[prompt_length:] if len(summary) > prompt_length else ""
    return render(request, 'results.html', {'summary': summary})




    

        
