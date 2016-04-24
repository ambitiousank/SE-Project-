from django import forms
from django.conf import settings
from staffmodule.models import PersonalDetail,EducationDetails, WorkExperience,\
	AddressDetails,ProgramApplied,PostApplied,UploadDetails,User,SubmitStatus

import os


class PersonalDetailForm(forms.ModelForm):
	class Meta:
		model = PersonalDetail
		fields = [ #"roll_number",
			"full_name",
			"father_name",
			"mother_name",
			"date_of_birth",
			"gender",
			"nationality",
			"category_id",
			"phone_number",
			"pan_card",
			"email_id"]

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		if not (provider == "iiitb.org" or provider == "iiitb.ac.in") :
			raise forms.ValidationError("Please use your iiitb email id")
		return email



class AddressDetailForm(forms.ModelForm):

	roll_number=forms.CharField(widget = forms.HiddenInput(), required = False)
	address_type=forms.CharField(widget = forms.HiddenInput(),required= False)
	class Meta:
		model=AddressDetails
		fields= ["address_type",
			"roll_number",
			"address1",
			"address2",
            "address3",
            "state",
            "city",
            "pincode"
		]



class WorkExperienceForm (forms.ModelForm):
	roll_number=forms.CharField(widget = forms.HiddenInput(), required = False)
	class Meta:
		model = WorkExperience
		fields = ["roll_number",
				  "last_organisation",
				  "position",
				  "job_description",
				  "start_year",
				  "end_year",
				  "duration"
				  ]

		def clean(self):
			start_year=self.cleaned_data.get("start_year")
			end_year=self.cleaned_data.get("end_year")
			duration=self.cleaned_data.get("duration")
			diff= end_year - start_year
			if(diff < 0):
				raise forms.ValidationError("Please check start year and end year. start year can't have a lower value than end year ")
			elif (duration <0 or duration > (diff*12+12)):
				raise forms.ValidationError("Please re-check duration (value should be in months)")
			return self




class ProgramDetailForm (forms.ModelForm):
	roll_number=forms.CharField(widget = forms.HiddenInput(), required = False)

	class Meta:
		model = ProgramApplied
		fields = [#"education_type",
			"roll_number",
			"course_id",
			"exam_name_id",
			"exam_subject_id",
			"program_id",
			"marks_scored"

		]


class FormSubmissionForm(forms.ModelForm):
	roll_number=forms.CharField(widget = forms.HiddenInput(),required = False)
	submission_status=forms.IntegerField(widget = forms.HiddenInput(), required = False)
	class Meta:
		model=SubmitStatus
		fields=[
			"submission_status",
			"roll_number"
			]


class FileUploadForm (forms.ModelForm):
	roll_number=forms.CharField(widget = forms.HiddenInput(), required = False)
	upload_type=forms.Field(widget = forms.HiddenInput(), required = False)
	class Meta:
		model = UploadDetails
		fields = [#"education_type",
			"roll_number",
			"upload_type",
			"upload_path"
		]
	def clean_upload_path(self):
		upFile = self.cleaned_data.get('upload_path')
		fileName = upFile.name
		file_type=self.cleaned_data.get('upload_type')

		print "<<<<<Here is "+str(file_type)+">>>>>"
		file_format='.pdf'
		if file_type == '1' or file_type =='2':
			file_format='.jpg'
		if  not (file_format in fileName):
			raise forms.ValidationError("Please upload a valid image file ("+file_format+")")
		else:
			rollno = self.cleaned_data.get('roll_number')
			upFile.name =file_type+"_"+str(rollno)+file_format

			absoluteName = settings.DOWNLOAD_ROOT+"/"+upFile.name

			if os.path.isfile(absoluteName):
				os.remove(absoluteName)
		return upFile







class JobDetailForm (forms.ModelForm):
	roll_number=forms.CharField(widget = forms.HiddenInput(), required = False)
	class Meta:
		model = PostApplied
		fields=["roll_number", "post"]

class EducationalDetailForm (forms.ModelForm):

	class Meta:
		model = EducationDetails
		fields = [#"education_type",
			"percentage",
			"board_university",
			"institute",
			"year_of_passing"
		]
	def clean_percentage(self):
		percentage = self.cleaned_data.get('percentage')

		if (percentage < 0 or percentage >100):
			raise forms.ValidationError("Please correct the percentage (0-100 is the valid range)")
		return percentage





