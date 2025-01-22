# forms.py
from django import forms


class ExcelFileUploadForm(forms.Form):
    excel_file = forms.FileField(label='选择Excel文件')


class ImportFileForm(forms.Form):
    excel_file = forms.FileField(label='选择Excel文件')
