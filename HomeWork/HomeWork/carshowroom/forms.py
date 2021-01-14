from django import forms
from .models import Supplier

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'