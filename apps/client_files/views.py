from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from .models import UploadedFile, FileUploadForm

class FileListView(ListView):
    model = UploadedFile
    template_name = 'main/file_list.html'
    context_object_name = 'files'


class FileDownloadView(View):
    def get(self, request, file_id):
        try:
            uploaded_file = UploadedFile.objects.get(pk=file_id)
        except UploadedFile.DoesNotExist:
            raise Http404("File does not exist")

      
        if uploaded_file.file and uploaded_file.file.storage.exists(uploaded_file.file.name):
            with uploaded_file.file.open('rb') as file:
                response = HttpResponse(file.read(), content_type='application/force-download')
                response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
                return response
        else:
            raise Http404("File not found.")
        
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
