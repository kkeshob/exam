from django import forms
from.models import User
from admin_dash.models import Questions

ANS_CHOICES= [
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ]

class RegistrationForm(forms.ModelForm):
    roll=forms.CharField(widget=forms.TextInput(attrs={'class':'','id':'roll','placeholder':'Roll Number'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'class':'phone','id':'phone','placeholder':'Phone Number'}))
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'name','id':'name','placeholder':'Full Name'}))
    class Meta:
        model=User
        fields=[
			'roll',
            'name',
            'phone',
            'course',

        ]
class LoginForm(forms.Form):
	roll=forms.CharField(widget=forms.TextInput(attrs={'class':'','id':'roll','placeholder':'Roll Number'}))
	phone=forms.CharField(widget=forms.TextInput(attrs={'class':'phone','id':'phone','placeholder':'Phone Number'}))

	def clean(self,*args,**kwargs):
		phone=self.cleaned_data.get('phone')
		roll=self.cleaned_data.get('roll')
		return super(LoginForm,self).clean(*args,**kwargs)

class ExamChoiceFrm(forms.ModelForm):
    class Meta:
        model=Questions
        fields=[
            'paper',
        ]
class AnsChoice(forms.Form):
    ans= forms.CharField(label='Select a oprion', widget=forms.RadioSelect(choices=ANS_CHOICES))
    def clean(self,*args,**kwargs):
        ans=self.cleaned_data.get('ans')
        return super(AnsChoice,self).clean(*args,**kwargs)