from django import forms
from myapp.models import *

class AttributeForm(forms.ModelForm):
    class Meta:
        model=ProductAttribute
        fields='__all__'