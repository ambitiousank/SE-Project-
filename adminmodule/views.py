from django.shortcuts import render
from .forms import PersonForm, EducationForm, AddressForm, ProgramForm, WorkForm, PostForm, validationForm, adminForm
from module1.models import SignUp, MatchRef
from staffmodule.models import AdminReference
from django.http import HttpResponsePermanentRedirect
from django.http import HttpResponse

# Create your views here.
def main(request):

	result=validateSession(request)
	if result is "Invalid":
		return HttpResponsePermanentRedirect("/login/")

	entries=AdminReference.objects.all()
	if not entries:
		form = adminForm(request.POST or None) 

		if form.is_valid():
			instance=form.save(commit=False)
			if 'name' in request.session:
				instance.created_by=request.session['name']
			instance.save()

		
		context ={
			"form":form  
		}

	else:
		context ={

		}
	

	return render(request,"admin_page.html",context)




def template(request):
	result=validateSession(request)
	if result is "Invalid":
		return HttpResponsePermanentRedirect("/login/")
	
	return render(request,"admin_templates.html",{})

def userReq(request):
	result=validateSession(request)
	if result is "Invalid":
		return HttpResponsePermanentRedirect("/login/")

	all_entries = SignUp.objects.all()
	name=[p.name for p in all_entries]
	email=[p.email for p in all_entries]
	role=[p.role for p in all_entries]

	for p in all_entries:
		check= MatchRef.objects.filter(email=p.email)
		if not check:
			p.match="Unmatched"
		else:
			p.match="Matched"
		p.save()


	all_entries = SignUp.objects.filter(approve='3')	


	context ={
		"all_entries":all_entries,  
	}
	
	return render(request,"admin_requests.html",context)



def userValidation(request,email):	
	result=validateSession(request)
	if result is "Invalid":
		return HttpResponsePermanentRedirect("/login/")

	entry = SignUp.objects.filter(email=email)
	init_comments=''
	init_status=3

	form=validationForm(request.POST or None,initial={'Comments': init_comments,'Action':init_status})

	if form.is_valid():
		k= request.POST['Action']
		c= request.POST['Comments']
		entry.update(approve=k) 
		entry.update(comment=c) 
		return HttpResponsePermanentRedirect("/admin_req/")


	name=entry.values_list('name')[0][0]
	email=entry.values_list('email')[0][0]
	role=entry.values_list('role')[0][0]
	match=entry.values_list('match')[0][0]

	context={
	"name":name,
	"email":email,
	"role":role,
	"match":match,
	"form":form,
	}
	return render(request,"userDetailForm.html",context)


def users(request):
	result=validateSession(request)
	if result is "Invalid":
		return HttpResponsePermanentRedirect("/login/")

	all_entries = SignUp.objects.all()	
	context ={
		"all_entries":all_entries,
	}
	
	return render(request,"admin_users.html",context)


	

def formTemplate1(request):
	result=validateSession(request)
	if result is "Invalid":
		return HttpResponsePermanentRedirect("/login/")

	title= "User Registration: Admission Template"

	#adding a form
	
	form = PersonForm(request.POST or None, prefix="pers") 
	sub_form1 = AddressForm(request.POST or None, prefix="add")
	sub_form2 = EducationForm(request.POST or None, prefix="edu")
	sub_form3 = ProgramForm(request.POST or None, prefix="prog")
	sub_form4 = WorkForm(request.POST or None, prefix="work") 

	#form.fields.widget.attrs['readonly'] = True


	context ={
		"title":title,        #template context variable and value
		"form1":form,
		"form2":sub_form1,
		"form3":sub_form2,
		"form4":sub_form3,
		"form5":sub_form4,
	}
	return render(request,"admin_template1.html",context)



def formTemplate2(request):
	result=validateSession(request)
	if result is "Invalid":
		return HttpResponsePermanentRedirect("/login/")

	title= "User Registration: Job Template"

	#adding a form
	
	form = PersonForm(request.POST or None, prefix="pers") 
	sub_form1 = AddressForm(request.POST or None, prefix="add")
	sub_form2 = EducationForm(request.POST or None, prefix="edu")
	sub_form3 = PostForm(request.POST or None, prefix="post")
	sub_form4 = WorkForm(request.POST or None, prefix="work") 


	context ={
		"title":title,        #template context variable and value
		"form1":form,
		"form1":form,
		"form2":sub_form1,
		"form3":sub_form2,
		"form4":sub_form3,
		"form5":sub_form4,

	}
	return render(request,"admin_template2.html",context)


#to handle session on logout
def validateSession(request):
	stringName="Admin"
	adminString="Admin"
	try:

		temp=request.session['role']
		stringName=str(temp)

		print "String name is"
		print stringName
	#get it from context
		if stringName == adminString:
			print "Valid"
			return "Valid"
		else:
			print "Invalid"
			return "Invalid" 
	except:
			print "Error"
			return "Invalid"



def logsout(request):
    print "logging out"
    request.session.flush()
    return HttpResponsePermanentRedirect("/login/")
