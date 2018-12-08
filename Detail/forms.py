from django import forms
from .models import Actor, Movie, Producer
class DateInput(forms.DateInput):
    input_type = 'date'

class ActorForm(forms.ModelForm):
	#dob = forms.DateField()
	class Meta:
		model = Actor
		fields = ['name', 'sex','dob', 'bio']
		widgets = {
            'dob': DateInput()
        }
class ProducerForm(forms.ModelForm):
	#dob = forms.DateField()
	class Meta:
		model = Producer
		fields = ['name', 'sex','dob', 'bio']
		widgets = {
            'dob': DateInput()
        }
class MovieForm(forms.ModelForm):
	#year_of_release = forms.DateField()
	class Meta:
		model = Movie
		fields = ['Name', 'Year_of_Release','producer', 'Plot', 'poster']
		widgets = {
            'Year_of_Release': DateInput()
        }