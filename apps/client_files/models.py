from django.db import models
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UploadedFile(models.Model):
    file = models.FileField(
        verbose_name='название файла',
        upload_to=''
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='uploaded_files',
        verbose_name='загружено пользователем',
    )

    def __str__(self):
        return str(self.file)

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']
        widgets = {
            'uploaded_by': forms.HiddenInput(),  # Скрываем поле от пользователя
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(FileUploadForm, self).__init__(*args, **kwargs)
        if user:
            self.initial['uploaded_by'] = user