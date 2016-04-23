from django.shortcuts import render
from .forms import PersonForm, EducationForm, AddressForm, ProgramForm, WorkForm, PostForm, validationForm, adminForm
from module1.models import SignUp, MatchRef

# Create your views here.
def main(request):
	
	form = adminForm(request.POST or None) 

	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()

	context ={
		"form":form   
	}

	return render(request,"admin_page.html",context)


def template(request):
	
	return render(request,"admin_templates.html",{})

def users(request):

	all_entries = SignUp.objects.all()
	name=[p.name for p in all_entries]
	email=[p.email for p in all_entries]
	role=[p.role for p in all_entries]
	form = validationForm(request.POST or None) 

	for p in all_entries:
		check= MatchRef.objects.filter(email=p.email)
		if not check:
			p.match="Unmatched"
		else:
			p.match="Matched"
		p.save()


	all_entries = SignUp.objects.all()
	
	if request.method == 'POST':
		print "valid"
		k= request.POST.getlist('Action')
		c= request.POST.getlist('Comments')
		print k
		all_entries.update(approve=k)
		#return render(request,"staff","")


	context ={
		"all_entries":all_entries,
		"form":form   
	}
	
	return render(request,"admin_requests.html",context)
	

def formTemplate1(request):
	title= "User Registration: Admission Template"

	#adding a form
	
	form = PersonForm(request.POST or None, prefix="pers") 
	sub_form1 = AddressForm(request.POST or None, prefix="add")
	sub_form2 = EducationForm(request.POST or None, prefix="edu")
	sub_form3 = ProgramForm(request.POST or None, prefix="prog")
	sub_form4 = WorkForm(request.POST or None, prefix="work") 

	#form.fields.widget.attrs['readonly'] = True

	
	'''
	if form.is_valid() and sub_form1.is_valid() and sub_form2.is_valid() and sub_form3.is_valid() and sub_form4.is_valid():
		personal=form.save(commit=False)
		address=sub_form1.save(commit=False)
		education=sub_form2.save(commit=False)
		program=sub_form3.save(commit=False)
		work=sub_form4.save(commit=False)
		
		#handle dependencies between the tables
		address.roll_number=personal.roll_number		
		personal.current_address_id=address.save()   #add foreign key
		personal.save()
		education.roll_number=personal.roll_number
		education.save()
		program.roll_number=personal.roll_number
		program.save()
		work.roll_number=personal.roll_number
		work.save()

		return render(request,"success.html",{})
	'''


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
