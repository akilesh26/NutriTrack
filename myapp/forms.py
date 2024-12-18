from django import forms
from .models import Food

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'type': 'file',
                'accept': 'image/*',
                'id': 'input-file',
                'hidden': 'true'
            }),
        }