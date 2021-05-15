from django import forms
from django.forms import ModelForm
from django.forms import DateTimeInput
from bootstrap_datepicker_plus import DatePickerInput

from claus_planning.models import Planning

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class PlanningForm(ModelForm):

    class Meta:
        model = Planning
        fields = [  'persoon',
                    'project',
                    'projecttaak',
                    'datum',
                    'begintijd',
                    'eindtijd',
                    'status',
                    ]

        widgets = {'datum':DateInput(), 'begintijd':TimeInput(),'eindtijd':TimeInput()}  


class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )


     

    


    
