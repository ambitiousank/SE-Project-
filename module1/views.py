from django.shortcuts import render
from .models import SignUp
from .forms import SignUpForm, login
from django.http import HttpResponse

# Create your views here.
def sign(request):
	title= "IIITB"

	#adding a form
	form= SignUpForm(request.POST or None)   #so that validations are done when POST, None so that initially no validations show up
	
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		return render(request,"success.html",{})


	context ={
		"title":title,        #template context variable and value
		"form":form

	}
	return render(request,"sign.html",context)

def login1(request):
	title= "IIITB Login Portal"
	#adding a form
	form= login(request.POST or None)   #so that validations are done when POST, None so that initially no validations show up
	#print msg
	context ={		
		"title":title,        #template context variable and value
		"form":form,
	}
	if form.is_valid():
		instance=form.save(commit=False)
		entry=SignUp.objects.filter(email=instance.email,password=instance.password,role=instance.role,approve='1')
		if not entry:
			context={        #template context variable and value
				"form":form,
				"error":"Login Failed!"
				}
			return render(request,"login_page.html",context)
		else:	
			request.session['role']=entry.values_list('role')[0][0]	
			name= entry.values_list('name')[0][0]		
			context ={
				"role":instance.role,
				"title":name,        #template context variable and value
				}
			if instance.role=='Staff':
				return render(request,"staff_dashboard.html",context)
			if instance.role=='User':
				return render(request,"success.html",context)
			if instance.role=='Admin':
				return render(request,"admin_page.html",context)
	return render(request,"login_page.html",context)
