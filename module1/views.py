from django.shortcuts import render

from .forms import SignUpForm, login
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
	title= "IIITB"

	#adding a form
	form= login(request.POST or None)   #so that validations are done when POST, None so that initially no validations show up



	context ={
		"title":title,        #template context variable and value
		"form":form

	}
	return render(request,"login_page.html",context)