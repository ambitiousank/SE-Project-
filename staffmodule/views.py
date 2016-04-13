from django.shortcuts import render
from django.db import models
from .models import AdmissionDetail,PersonalDetail,EducationDetails,AddressDetails,WorkExperience,ProgramApplied,ExamRef,CourseRef,ExamSubjectRef,CategoryRef,StateRef,ProgramRef,UploadDetails
from .forms import validationForm,validationForm2
from django.http import HttpResponsePermanentRedirect


# Create your views here.
#function to fetch list of pending records
def fetchPendingRequest(request):
	all_entries = AdmissionDetail.objects.filter(status_of_request__in=[1,4])

	for i in all_entries:
		print i.roll_number

	context={
		"title":"a",
		"form":"k",

	}
	return render(request,"staff_dashboard.html",{'Students':all_entries})
	#return render(request,"base.html",{'Students':all_entries})


def studentValidation(request,admission_id):
	print "here"
	print admission_id
	roll_number=0
	init_comments=''
	init_status=1
	

	all_entries = AdmissionDetail.objects.filter(admission_id=admission_id)
	for i in all_entries:
		print i.roll_number
		roll_number=i.roll_number
		init_comments=i.validation_comments
		init_status=i.status_of_request

	form=validationForm(request.POST or None,initial={'Comments': init_comments,'Action':init_status})

	student_entry=PersonalDetail.objects.get(roll_number=roll_number)
	print student_entry.full_name
	if form.is_valid():
		print "valid"
		k= request.POST['Action']
		c= request.POST['Comments']
		#admit=AdmissionDetail(admission_id=admission_id)
		all_entries.update(status_of_request=k,validation_comments=c)
		#return render(request,"staff","")
		return HttpResponsePermanentRedirect("/staff/")
		#admit.save()
	
	education_details=EducationDetails.objects.filter(roll_number=roll_number)
	work_experience=WorkExperience.objects.filter(roll_number=roll_number)

	address=AddressDetails.objects.get(address_id=student_entry.current_address_id)
	program=ProgramApplied.objects.get(roll_number=roll_number)
	exam=ExamRef.objects.get(exam_id=program.exam_name_id)
	course=CourseRef.objects.get(course_id=program.course_id)
	subject=ExamSubjectRef.objects.get(exam_subject_id=program.exam_subject_id)
	category=CategoryRef.objects.get(category_id=student_entry.category_id)
	state=StateRef.objects.get(state_id=address.state)
	program_name=ProgramRef.objects.get(program_id=program.program_id)
	upload=UploadDetails.objects.filter(roll_number=roll_number)

	for k in upload:
		print k.upload_path
		print k.upload_type_id
		print k.upload_type_id.upload_type_desc





	vo={
	"roll_no":student_entry.roll_number,
	"personal":student_entry,	
	"form":form,
	"education_details":education_details,
	"address":address,
	"work_ex":work_experience,
	"program":program,
	"exam":exam.exam_desc,
	"course":course.course_desc,
	"subject":subject.exam_subject_desc,
	"category":category.category_desc,
	"state":state.state_desc,
	"program_name":program_name.program_desc,
	"filename":"downloads/k2.pdf",
	"filename2":"downloads/MT2015020_HIghSchool.pdf",
	"upload":upload



	}
	return render(request,"studentDetailForm.html",vo)
def submitComments(request):
	print comments

	return render(request,"home.html","")

def staffSearch(request):
	form=validationForm2(request.POST or None)
	search=[]
	message=False
	if form.is_valid():
		k= request.POST['value']
		message=True
		search = AdmissionDetail.objects.filter(roll_number=k)

	vo={
	"searchs":search,
	"form":form,
	"message":message

	}	
	return render(request,"staff_search.html",vo)



