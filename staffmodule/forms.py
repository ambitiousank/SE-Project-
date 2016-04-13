from django import forms


ValidationResult = (  
    (2,'Valid' ),
    (3,'Invalid'),
    (4,'Incompelete'),
    (1,'Pending')
    
   
)

SearchCriteria= (  
    (1,'RollNumber' ),
    
    
   
)


class validationForm(forms.Form):
	Comments=forms.CharField(widget=forms.Textarea(attrs={'rows': '2','cols':'20'}))
	Action=forms.ChoiceField(choices=ValidationResult,required=True)



	def clean_Comments(self):
		print "here"
		validationComments=self.cleaned_data.get('Comments')

		print validationComments
		return validationComments


class validationForm2(forms.Form):
	value=forms.CharField(max_length=32)
	Action=forms.ChoiceField(choices=SearchCriteria,required=True)



	def clean_value(self):
		print "here"
		validationComments=self.cleaned_data.get('value')

		print validationComments
		return validationComments