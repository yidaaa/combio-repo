from django import forms 
from .models import *
  
class UploadForm(forms.ModelForm): 
  
    class Meta: 
        model = User 
        fields = ['photo'] 