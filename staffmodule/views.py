from django.shortcuts import render
from django.db import models
from .models import AdmissionDetail,PersonalDetail,EducationDetails,AddressDetails,WorkExperience,ProgramApplied,ExamRef,CourseRef,ExamSubjectRef,CategoryRef,StateRef,ProgramRef,UploadDetails,AdminReference,PostApplied,UploadTypeRef,PostRef
from .forms import validationForm,validationForm2
from django.http import HttpResponsePermanentRedirect,HttpResponse


# Create your views here.
#function to fetch list of pending records
def fetchPendingRequest(request):
	result=validateSession(request)
	if result is "Invalid":
		return HttpResponsePermanentRedirect("/login/")

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
	result=validateSession(request)
	if result is "Invalid":
		return HttpResponsePermanentRedirect("/login/")

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
	gender=student_entry.gender
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
	master_ref=AdminReference.objects.get(reference_id=1)
	master_decesion=master_ref.form_template
	print master_decesion
	print "is master def"
	address=AddressDetails.objects.get(address_id=student_entry.current_address_id)
	program=None
	post=None
	postDesc=None
	exam=None
	course=None
	subject=None
	program_name=None
	exam_desc=None
	if master_decesion==1:
		program=ProgramApplied.objects.get(roll_number=roll_number)
		exam=ExamRef.objects.get(exam_id=program.exam_name_id)
		course=CourseRef.objects.get(course_id=program.course_id)
		subject=ExamSubjectRef.objects.get(exam_subject_id=program.exam_subject_id)
		program_name=ProgramRef.objects.get(program_id=program.program_id)
		exam_desc=exam.exam_desc
	else:
		post=PostApplied.objects.get(roll_number=roll_number)
		postD=PostRef.objects.get(post_id=post.post)
		postDesc=postD.post_desc


	
	
	category=CategoryRef.objects.get(category_id=student_entry.category_id)
	state=StateRef.objects.get(state_id=address.state)
	
	upload=UploadDetails.objects.filter(roll_number=roll_number)

	uploadObjects=[]

	for k in upload:
		print k.upload_path
		z=parseDownloadString(str(k.upload_path))
		uploadDesc=UploadTypeRef.objects.get(upload_type_id=k.upload_type)
		uploadType=2
		if 'pdf' in str(z):
			uploadType=1


			#temp=UploadContext(uploadType)
			#temp.Uploadpath=upload_path
			#temp.desc=uploadDesc
		print uploadType
		#print k.upload_path
		uploadObjects.append(UploadContext(uploadType,z,uploadDesc.upload_type_desc	))



		#print k.upload_type_id
		#print k.upload_type_id.upload_type_desc
		#nothing
		if gender==1:
			genderDesc="Male"
		elif gender ==2:
			genderDesc="Female"
		else:
			genderDesc="Others"




	vo={
	"roll_no":student_entry.roll_number,
	"personal":student_entry,	
	"form":form,
	"education_details":education_details,
	"address":address,
	"work_ex":work_experience,
	"program":program,
	"post":post,
	"postDesc":postDesc,
	"exam":exam_desc,
	"course":course,
	"subject":subject,
	"category":category.category_desc,
	"state":state.state_desc,
	"program_name":program_name,
	"filename":"downloads/k2.pdf",
	"filename2":"downloads/MT2015020_HIghSchool.pdf",
	"uploadObjects":uploadObjects,
	"gender":genderDesc,



	}
	return render(request,"studentDetailForm.html",vo)
def submitComments(request):
	print comments

	return render(request,"home.html","")

def staffSearch(request):
	result=validateSession(request)
	if result is "Invalid":
		return HttpResponsePermanentRedirect("/login/")

	form=validationForm2(request.POST or None)
	search=[]
	message=False
	if form.is_valid():
		k= request.POST['value']
		m= request.POST['Action']
		r=0
		message=True
		a="1"
		l=int(m)
		print m
		if l==1:
			print "-----here"
			search = AdmissionDetail.objects.filter(roll_number=k)
		elif l==2:
			temp = PersonalDetail.objects.filter(full_name__icontains=k)
			for x in temp:
				print x.roll_number
				r=x.roll_number
				s = AdmissionDetail.objects.filter(roll_number=r)
				for sd in s:
					search.append(sd)



				
		


	vo={
	"searchs":search,
	"form":form,
	"message":message

	}	
	return render(request,"staff_search.html",vo)

class UploadContext:
	#Uploadpath="h"
#desc=""
	def __init__ (self,types, u,k):
		self.types=types
		self.Uploadpath=u
		self.desc=k

def parseDownloadString(string):
	a,b=string.split('downloads/')
	print a
	print b
	new='downloads/'+b
	print new
	return new
def validateSession(request):
	stringName="Staff"
	staffString="Staff"
	try:
		temp=request.session['role']
		stringName=str(temp)

		print "Strig name is"
		print stringName
	#get it from context
		if stringName == staffString:
			print "Valid"
			return "Valid"
		else:
			print "Invalid"
			return "Invalid" 

	except:
		print  "error"
		return "Invalid"




