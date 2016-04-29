from django import forms
from .models import SignUp

class SignUpForm(forms.ModelForm):
	password=forms.CharField(max_length=20, widget=forms.PasswordInput)
	confirmPassword=forms.CharField(max_length=20, widget=forms.PasswordInput)
	class Meta:
		model=SignUp
		fields= ['name','email','password','confirmPassword','role']   #one or more fields from the model


	def clean_email(self):
		email=self.cleaned_data.get('email')
		email_base,provider= email.split("@")

		entries=SignUp.objects.filter(email=email)
				
		#domain, extension= provider.split('.')
		if not  ( provider == "iiitb.org" or provider == "iiitb.ac.in" ):
			raise forms.ValidationError("Please use your iiitb email")
		elif len(entries)>0:
			raise forms.ValidationError("This email has already been registered.")
		return email

		


	def clean(self):
		password1=self.cleaned_data.get('password')
		password2=self.cleaned_data.get('confirmPassword')
		
		if not(password1):
			print
		elif len(password1)<8:
			raise forms.ValidationError("Enter a password of atleast 8 characters")
		if password1!=password2:
			raise forms.ValidationError("Passwords do not match")


class login(forms.ModelForm):
	password=forms.CharField(max_length=20, widget=forms.PasswordInput)
	class Meta:
		model=SignUp
		fields= ['email','password','role']