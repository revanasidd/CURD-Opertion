from django import forms
from .models import Employee

class EmpForm(forms.ModelForm):

	class Meta:
		model=Employee
		fields=('fullname','empcode','mobile','position')
		labels={
			'fullname':'FULL NAME',
			'empcode':'EMP CODE'
		}

	def __init__(self,*args,**kwargs):
		super(EmpForm,self).__init__(*args,**kwargs)
		self.fields['position'].empty_label='Select'
		self.fields['empcode'].required=False