from django import forms
import datetime
from .models import All_Data, HDC_Data, Precious, Descente

class AllDataSurvey(forms.ModelForm):
    model=All_Data
    errors = None
    fields = ('location')

class HdcDataSurvey(forms.ModelForm):
    model=HDC_Data
    errors = None
    fields = ('location')

class PreciousDataSurvey(forms.ModelForm):
    model=Precious
    errors = None
    fields = ('location')

class DescenteDataSurvey(forms.ModelForm):
    model=Descente
    errors = None
    fields = ('location')

