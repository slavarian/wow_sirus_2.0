from django.db import models
from django import forms


class UploadedFile(models.Model):
    file = models.FileField(
        verbose_name='название файла',
        upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.file

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']

  