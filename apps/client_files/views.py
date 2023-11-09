from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from .models import UploadedFile, FileUploadForm

class FileListView(ListView):
    model = UploadedFile
    template_name = 'main/file_list.html'
    context_object_name = 'files'

class FileUploadView(View):
    template_name = 'main/add_file.html'

    def get(self, request):
        form = FileUploadForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
        return render(request, self.template_name, {'form': form})

class FileDownloadView(View):
    def get(self, request, file_id):
        uploaded_file = UploadedFile.objects.get(pk=file_id)
        response = HttpResponse(uploaded_file.file, content_type='application/force-download')
        response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
        return response
