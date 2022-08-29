from django import forms

from BackUpDispatch.models import CFS


class CFSCreateForm(forms.ModelForm):
    class Meta:
        model = CFS
        fields = '__all__'
