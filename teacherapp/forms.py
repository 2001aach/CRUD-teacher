from django import forms

from teacherapp.models import teacher

class DateInput(forms.DateInput):
    input_type='date'

class teacherform(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model=teacher
        exclude=('__all__',)