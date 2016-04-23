from django import forms
from staffmodule.models import PersonalDetail
from staffmodule.models import EducationDetails
from staffmodule.models import AddressDetails
from staffmodule.models import UploadDetails
from staffmodule.models import ProgramApplied
from staffmodule.models import PostApplied
from staffmodule.models import WorkExperience
from staffmodule.models import AdminReference

Status = (  
    (1,'Approve' ),
    (2,'Decline'),
    (3,'Pending')
    
   
)
class validationForm(forms.Form):
	Comments=forms.CharField(widget=forms.Textarea(attrs={'rows': '2','cols':'20'}))
	Action=forms.ChoiceField(choices=Status,required=True)



	def clean_Comments(self):
		print "here"
		validationComments=self.cleaned_data.get('Comments')

		print validationComments
		return validationComments



class adminForm(forms.ModelForm):
	form_submission_date = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
	
	class Meta:
		model=AdminReference
		fields=['form_template','form_submission_date']

	def clean(self):
		return ""



class PersonForm(forms.ModelForm):
	date_of_birth = forms.DateField(widget=forms.DateInput(format = '%d/%m/%Y'), input_formats=('%d/%m/%Y',))
	class Meta:
		model=PersonalDetail
		fields=['roll_number','full_name','father_name','mother_name','date_of_birth','gender','nationality',
		'category_id','phone_number','pan_card','email_id']


class EducationForm(forms.ModelForm):
	class Meta:
		model=EducationDetails
		fields=['percentage','board_university','institute','year_of_passing']


class AddressForm(forms.ModelForm):
	class Meta:
		model=AddressDetails
		fields=['address1','address2','address3','city','pincode','state']
		
	

class ProgramForm(forms.ModelForm):
	class Meta:
		model=ProgramApplied
		fields=['program_id','course_id','exam_name_id','exam_subject_id','marks_scored']
	
class PostForm(forms.ModelForm):
	class Meta:
		model=PostApplied
		fields=['post']

class WorkForm(forms.ModelForm):
	class Meta:
		model=WorkExperience
		fields=['last_organisation','position','job_description','start_year','end_year','duration']


