from django import forms
from .models import Tasklist

class TaskForm(forms.ModelForm):
    class Meta:
        model = Tasklist
        fields = ['item', 'ended']

class UploadFileForm(forms.Form):
    file = forms.FileField()
    file.widget.attrs['class'] = 'form-control-file'