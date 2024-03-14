from django import forms
from .models import BatteryData,CellInformation

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = BatteryData
        fields = ['csv_file']

class CellInformationForm(forms.ModelForm):
    class Meta:
        model = CellInformation
        fields = '__all__'