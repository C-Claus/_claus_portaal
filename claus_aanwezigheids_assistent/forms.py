from django import forms
from django.forms import ModelForm
from django.forms import DateTimeInput
from bootstrap_datepicker_plus import DatePickerInput

from claus_aanwezigheids_assistent.models import Aanwezigheid

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class AanwezigheidsForm(ModelForm):

    class Meta:
        model = Aanwezigheid
        fields = [  
                    
                    'datum',
                    'begintijd',
                    'eindtijd',
                    'status',
                    'persoon',
                    ]

        widgets = {'datum':DateInput(), 'begintijd':TimeInput(),'eindtijd':TimeInput()}  