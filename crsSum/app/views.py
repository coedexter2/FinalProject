
from django.shortcuts import render 
from .forms import UploadFileForm 
  
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
    else: 
        form = UploadFileForm() 
    context['form'] = form 
    return render(request, "index.html", context) 

def waiting(request):
    return render(request, 'wait.html')
