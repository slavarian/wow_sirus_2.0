from django.shortcuts import render, redirect
from .models import FileUploadForm

def upload_file(request):
    template_name = 'main/add_file.html'


    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = FileUploadForm()
    return render(request, template_name, {'form': form})
