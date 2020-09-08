from django import forms
from.models import Questions
class AddQFrm(forms.ModelForm):
    class Meta:
        model=Questions
        fields=[
            'qs_no',
            'course',
            'paper',
            'questions',
            'answers',
            'option_a',
            'option_b',
            'option_c',
            'option_d',

        ]
