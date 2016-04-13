from django.shortcuts import render
from django.db import transaction
from django import forms
from .forms import PersonalDetailForm,\
    EducationalDetailForm, WorkExperienceForm,AddressDetailForm,ProgramDetailForm,JobDetailForm,\
    PhotoUploadForm,SigUploadForm,XmUploadForm
from django.http import HttpResponseRedirect

#from .models import User
from staffmodule.models import AdmissionDetail,PersonalDetail,EducationDetails, \
    AddressDetails,WorkExperience,ProgramApplied,ExamRef,CourseRef, \
    ExamSubjectRef,CategoryRef,StateRef,ProgramRef,UploadDetails,\
    AdminReference,PostApplied,PhotoFiles,SignatureFiles,XthMarksheets


# Create your views here.


# here we have to validate roll_number of a user in the url as well only then we'll allow access

#admin_ref =AdminReference.objects.get(reference_id=1)

admin_ref =1


"""

To Show all the information provided by the candidate, we collect information from different tables and present it as an
html page. A candidate can verify how his/her information will look once the form is submitted

"""
def homeView(request, roll_number):

    PERMANENT_ADDRESS_TYPE=0
    CURRENT_ADDRESS_TYPE=1

    personal_details = PersonalDetail.objects.get(roll_number=roll_number)
    category_details= CategoryRef.objects.get(category_id = personal_details.category_id)
    educational_details=EducationDetails.objects.filter(roll_number=roll_number)
    permanentAddress=AddressDetails.objects.get(roll_number=roll_number,address_type=PERMANENT_ADDRESS_TYPE)
    currentAddress=AddressDetails.objects.get(roll_number=roll_number,address_type=CURRENT_ADDRESS_TYPE)
    work_experience=WorkExperience.objects.filter(roll_number=roll_number)

    #if institute is offering admission
    if admin_ref.offer_id==1:
        program_applied=ProgramApplied.objects.get(roll_number=roll_number)
        program=ProgramRef.objects.get(program_id=program_applied.program_id)
        exam_details=ExamRef.objects.get(exam_id=program_applied.exam_name_id)
        exam_subject_details=ExamSubjectRef.objects.get(exam_subject_id=program_applied.exam_subject_id)
        course_details=CourseRef.objects.get(course_id=program_applied.course_id)
        context= {
            "program":program_applied,
            "exam":exam_details.exam_desc,
            "course":course_details.course_desc,
            "subject":exam_subject_details.exam_subject_desc,
            "program_name":program.program_desc,
        }

    #if institute is offering a job
    elif admin_ref.offer_id==2:
         post=PostApplied.objects.get(roll_number=roll_number)
         context= {"post":post}

    context.update({
        "roll_number": roll_number,
        "personal":personal_details,
        #"form":form,
        "education_details":educational_details,
        "permanent_address":permanentAddress,
        "current_address":currentAddress,
        "work_ex":work_experience,
        "category":category_details.category_desc,
        "adminRef":admin_ref,
        #"filename":"downloads/k2.pdf",
        #"filename2":"downloads/MT2015020_HIghinstitute.pdf",
        #"upload":upload
        })
    return render (request, "home.html",context)


def fileUploadView(request,roll_number):
    title= "File Upload List"
    context={
        "title" : title,
        "roll_number" : roll_number
    }

    return render(request, "candidate_file_upload_details.html",  context)


def photoUploadView(request, roll_number):

      title= "Photograph Upload Details"
      photoEntries=PhotoFiles.objects.filter(roll_number=roll_number,)

      if photoEntries:
        for pe in photoEntries:
            ph=pe.photograph_file

        phForm=PhotoUploadForm(request.POST or None, initial={"photograph_file":ph})
      else:
        phForm=PhotoUploadForm(request.POST or None)

      context={
        "title" : title,
        "phForm" :phForm,
        "roll_number": roll_number,
        "adminRef":admin_ref
      }
      print ">>>before valid "
      print request.POST
      if phForm.is_valid():

        print "hello in phFormsView"
        req=request.POST
        print req
        ph=req.getlist('photograph_file')[0]

        if photoEntries:

            photoEntries.update(photograph_file=ph,roll_number=roll_number)
        else:
            instance= phForm.save(commit=False)
            instance.roll_number= roll_number
            instance.photograph_file=ph

            instance.save()

        transaction.commit()

      return render(request, "candidate_photo_upload_details.html",  context)


def signUploadView(request, roll_number):
      title= "Document Upload Details"
      signEntries=SignatureFiles.objects.filter(roll_number=roll_number,)

      if signEntries:
        for se in signEntries:
            si=se.signature_file

        signForm=SigUploadForm(request.POST or None, initial={"signature_file":si})
      else:
        signForm=SigUploadForm(request.POST or None)

      context={
        "title" : title,
        "signForm" :signForm,
        "roll_number": roll_number,
        "adminRef":admin_ref
      }

      if signForm.is_valid():
        req=request.POST
        print req
        ph=req.getlist('signature_file')[0]

        if signEntries:
            signEntries.update(photograph_file=ph,roll_number=roll_number)
        else:
            instance= signForm.save(commit=False)
            instance.roll_number= roll_number
            instance.photograph_file=ph

            instance.save()

        transaction.commit()
        return render(request, "candidate_file_upload_details.html", context)

def xmUploadView(request, roll_number):
      title= "Document Upload Details"
      xmEntries=XthMarksheets.objects.filter(roll_number=roll_number,)

      if xmEntries:
        for xe in xmEntries:
            xm=xe.xth_marksheet

        xmForm=XmUploadForm(request.POST or None, initial={"xth_marksheet":xm})
      else:
        xmForm=XmUploadForm(request.POST or None)

      context={
        "title" : title,
        "xmForm" :xmForm,
        "roll_number": roll_number,
        "adminRef":admin_ref
      }

      if xmForm.is_valid():
        req=request.POST
        print req
        xm=req.getlist('xth_marksheet')[0]

        if xmEntries:

            xmEntries.update(xth_marksheet=xm,roll_number=roll_number)
        else:
            instance= xmForm.save(commit=False)
            instance.roll_number= roll_number
            instance.xth_marksheet=xm

            instance.save()

        transaction.commit()
        return render(request, "candidate_file_upload_details.html", context)

# def xcUploadView(request, roll_number):
#       title= "Document Upload Details"
#       xcEntries=UploadedFiles.objects.filter(roll_number=roll_number,)
#
#       if xcEntries:
#         for pe in xcEntries:
#             ph=pe.photograph_file
#
#         phForm=PhotoUploadForm(request.POST or None, innitial={"photograph_file":ph})
#       else:
#         phForm=PhotoUploadForm(request.POST or None)
#
#       context={
#         "title" : title,
#         "phForm" :phForm,
#         "roll_number": roll_number,
#         "adminRef":admin_ref
#       }
#
#       if phForm.is_valid():
#         req=request.POST
#         print req
#         ph=req.getlist('photograph_file')[0]
#
#         if xcEntries:
#
#             xcEntries.update(photograph_file=ph,roll_number=roll_number)
#         else:
#             instance= phForm.save(commit=False)
#             instance.roll_number= roll_number
#             instance.photograph_file=ph
#
#             instance.save()
#
#         transaction.commit()
#         return render(request, "candidate_file_upload_details.html", context)
#
# def photoUploadView(request, roll_number):
#       title= "Document Upload Details"
#       photoEntries=UploadedFiles.objects.filter(roll_number=roll_number,)
#
#       if photoEntries:
#         for pe in photoEntries:
#             ph=pe.photograph_file
#
#         phForm=PhotoUploadForm(request.POST or None, innitial={"photograph_file":ph})
#       else:
#         phForm=PhotoUploadForm(request.POST or None)
#
#       context={
#         "title" : title,
#         "phForm" :phForm,
#         "roll_number": roll_number,
#         "adminRef":admin_ref
#       }
#
#       if phForm.is_valid():
#         req=request.POST
#         print req
#         ph=req.getlist('photograph_file')[0]
#
#         if photoEntries:
#
#             photoEntries.update(photograph_file=ph,roll_number=roll_number)
#         else:
#             instance= phForm.save(commit=False)
#             instance.roll_number= roll_number
#             instance.photograph_file=ph
#
#             instance.save()
#
#         transaction.commit()
#         return render(request, "candidate_file_upload_details.html", context)
#
# def photoUploadView(request, roll_number):
#       title= "Document Upload Details"
#       photoEntries=UploadedFiles.objects.filter(roll_number=roll_number,)
#
#       if photoEntries:
#         for pe in photoEntries:
#             ph=pe.photograph_file
#
#         phForm=PhotoUploadForm(request.POST or None, innitial={"photograph_file":ph})
#       else:
#         phForm=PhotoUploadForm(request.POST or None)
#
#       context={
#         "title" : title,
#         "phForm" :phForm,
#         "roll_number": roll_number,
#         "adminRef":admin_ref
#       }
#
#       if phForm.is_valid():
#         req=request.POST
#         print req
#         ph=req.getlist('photograph_file')[0]
#
#         if photoEntries:
#
#             photoEntries.update(photograph_file=ph,roll_number=roll_number)
#         else:
#             instance= phForm.save(commit=False)
#             instance.roll_number= roll_number
#             instance.photograph_file=ph
#
#             instance.save()
#
#         transaction.commit()
#         return render(request, "candidate_file_upload_details.html", context)
#
# def photoUploadView(request, roll_number):
#       title= "Document Upload Details"
#       photoEntries=UploadedFiles.objects.filter(roll_number=roll_number,)
#
#       if photoEntries:
#         for pe in photoEntries:
#             ph=pe.photograph_file
#
#         phForm=PhotoUploadForm(request.POST or None, innitial={"photograph_file":ph})
#       else:
#         phForm=PhotoUploadForm(request.POST or None)
#
#       context={
#         "title" : title,
#         "phForm" :phForm,
#         "roll_number": roll_number,
#         "adminRef":admin_ref
#       }
#
#       if phForm.is_valid():
#         req=request.POST
#         print req
#         ph=req.getlist('photograph_file')[0]
#
#         if photoEntries:
#
#             photoEntries.update(photograph_file=ph,roll_number=roll_number)
#         else:
#             instance= phForm.save(commit=False)
#             instance.roll_number= roll_number
#             instance.photograph_file=ph
#
#             instance.save()
#
#         transaction.commit()
#         return render(request, "candidate_file_upload_details.html", context)
#


# def fileUploadView(request, roll_number):
#     PHOTO=1
#     SIGN=2
#     X_MARKSHEET=3
#     X_CERTIFICATE=4
#     XII_MARKSHEET=5
#     XII_CERTIFICATE=6
#     GRAD_MARKSHEET=7
#     GRAD_CERTIFICATE=8
#
#     title= "Document Upload Details"
#     photoEntry=UploadDetails.objects.filter(roll_number=roll_number, upload_type_id=PHOTO)
#     signEntry=UploadDetails.objects.filter(roll_number=roll_number, upload_type_id=SIGN)
#     xmEntry=UploadDetails.objects.filter(roll_number=roll_number, upload_type_id=X_MARKSHEET)
#     xcEntry=UploadDetails.objects.filter(roll_number=roll_number, upload_type_id=X_CERTIFICATE)
#     xiimEntry=UploadDetails.objects.filter(roll_number=roll_number, upload_type_id=XII_MARKSHEET)
#     xiicEntry=UploadDetails.objects.filter(roll_number=roll_number, upload_type_id=XII_CERTIFICATE)
#     gmEntry=UploadDetails.objects.filter(roll_number=roll_number, upload_type_id=GRAD_MARKSHEET)
#     gcEntry=UploadDetails.objects.filter(roll_number=roll_number, upload_type_id=GRAD_CERTIFICATE)
#
#     photoForm=initiateUploadForm(request, roll_number, PHOTO, photoEntry)
#     signForm=initiateUploadForm(request, roll_number, SIGN, signEntry)
#     xmForm=initiateUploadForm(request, roll_number, X_MARKSHEET, xmEntry)
#     xcForm=initiateUploadForm(request, roll_number, X_CERTIFICATE, xcEntry)
#     xiimForm=initiateUploadForm(request, roll_number, XII_MARKSHEET, xiimEntry)
#     xiicForm=initiateUploadForm(request, roll_number, XII_CERTIFICATE, xiicEntry)
#     gmForm=initiateUploadForm(request, roll_number, GRAD_MARKSHEET, gmEntry)
#     gcForm=initiateUploadForm(request, roll_number, GRAD_CERTIFICATE, gcEntry)
#
#     context={
#         "title" : title,
#         "photoForm":photoForm,
#         "signForm":signForm,
#         "xmForm": xmForm,
#         "xcForm":xcForm,
#         "xiimForm":xiimForm,
#         "xiicForm":xiicForm,
#         "gmForm":gmForm,
#         "gcForm":gcForm,
#         "roll_number":roll_number,
#         "adminRef":admin_ref
#     }
#     return render(request,"candidate_file_upload_details.html", context)
#
# def initiateUploadForm(request, roll_number, file, fileEntry):
#
#     if fileEntry:
#         for fe in fileEntry:
#             fp=fe.upload_path
#             ft=fe.upload_type_id
#             rn=fe.roll_number
#
#         fileUploadForm= UploadDetailsForm(request.POST or None, initial={
#             "upload_path":fp,
#             "upload_type_id":ft,
#             "roll_number":rn
#         })
#     else:
#         fileUploadForm=UploadDetailsForm(request.POST or None, initial={
#             "roll_number":roll_number
#         })
#     return fileUploadForm
#
#
# def saveUploadForm(request, roll_number, file_type_id, fileUploadForm, fileEntry):
#
#     if fileUploadForm.is_valid():
#
#         up=request.POST.getlist('upload_path')[file_type_id]
#         ut=request.POST.getlist('upload_type_id')[file_type_id]
#         rn=request.POST.getlist('roll_number')[file_type_id]
#
#         if fileEntry:
#              fileEntry.update(upload_path=up,upload_type_id=ut,roll_numer=rn)
#         else:
#              instance=fileUploadForm.save(commit=False)
#              instance.upload_path=up
#              instance.upload_type_id=ut
#              instance.roll_number=rn
#              instance.save()
#
#     transaction.commit()
#     return (request)
#
#
#

def jobDetailsView(request, roll_number):

    title = "Program Applying For"
    jobDetailEntry=PostApplied.objects.filter(roll_number=roll_number)

    if jobDetailEntry:
        for jde in jobDetailEntry:
            po=jde.post

        jdForm=JobDetailForm(request.POST or None, initial={"post":po })

    else:
        jdForm=JobDetailForm(request.POST or None)



    context={
        "title" : title,
        "jobDetailForm" :jdForm,
        "roll_number": roll_number,
        "adminRef":admin_ref
    }


    if jdForm.is_valid():
        req=request.POST
        print req
        po=req.getlist('post')[0]

        if jobDetailEntry:

            jobDetailEntry.update(post=po,roll_number=roll_number)
        else:
            instance= jdForm.save(commit=False)
            instance.roll_number= roll_number
            instance.post=po

            instance.save()


        transaction.commit()

    return render(request, "candidate_job_details.html", context)



def personalDetailsView(request, roll_number):

    title = "Candidate Personal Details"

    pd_entry = PersonalDetail.objects.get(roll_number=roll_number)

    print "pd_entry:=="
    print pd_entry

    #for pd in pd_entry:
    roll_number     = pd_entry.roll_number
    full_name       = pd_entry.full_name,
    father_name     = pd_entry.father_name,
    mother_name     = pd_entry.mother_name,
    date_of_birth   = pd_entry.date_of_birth,
    gender          = pd_entry.gender,
    nationality     = pd_entry.nationality,
    category_id     = pd_entry.category_id,
    phone_number    = pd_entry.phone_number,
    pan_card        = pd_entry.pan_card,
    email_id        = pd_entry.email_id

    pdForm=PersonalDetailForm(request.POST or None,initial={
        #'roll_number'       : pd.roll_number,
        'full_name'         : full_name[0],
        'father_name'       : father_name[0],
        'mother_name'       : mother_name[0],
        'date_of_birth'     : date_of_birth[0],
        'gender'            : gender[0],
        'nationality'       : nationality[0],
        'category_id'       : category_id[0],
        'phone_number'      : phone_number[0],
        'pan_card'          : pan_card[0],
        'email_id'          : email_id
    })

    context = {
        "title" : title,
        "roll_number" : roll_number,
        "title" : title,
        "pdForm" : pdForm,
        "adminRef":admin_ref
    }

    if pdForm.is_valid():
        print "valid"
        fu= request.POST['full_name']
        fa= request.POST['father_name']
        mo= request.POST['mother_name']
        da= request.POST['date_of_birth']
        ge= request.POST['gender']
        na= request.POST['nationality']
        ca= request.POST['category_id']
        ph= request.POST['phone_number']
        pa= request.POST['pan_card']
        em= request.POST['email_id']

        pd_entry.update(full_name=fu,father_name=fa,mother_name=mo,date_of_birth=da,gender=ge,
                        nationality=na,category_id=ca,phone_number=ph,pan_card=pa,email_id=em)
        transaction.commit()

    return render(request, "candidate_personalDetails.html",context)






def addressDetailsView(request, roll_number):

    title="Candidate Address Details"

    permanentAddressEntry=AddressDetails.objects.filter(roll_number=roll_number, address_type=0)
    permanentAddressDetailsForm=initiateAddressForm(0,request,permanentAddressEntry)

    currentAddressEntry=AddressDetails.objects.filter(roll_number=roll_number, address_type=1)
    currentAddressDetailsForm=initiateAddressForm(1,request,currentAddressEntry)

    request=saveAddress(roll_number,request,0,permanentAddressDetailsForm,permanentAddressEntry)
    request=saveAddress(roll_number,request,1,currentAddressDetailsForm,currentAddressEntry)

    context={
        "title" : title,
        "permanentAddress":permanentAddressDetailsForm,
        "currentAddress":currentAddressDetailsForm,
        "roll_number":roll_number,
        "adminRef":admin_ref,

    }
    return render(request, "candidate_addressDetails.html", context)





def initiateAddressForm(address_type,request, addressEntry):

    if addressEntry:
        for cae in addressEntry:
            address_type =cae.address_type
            address1 = cae.address1
            address2 = cae.address2
            address3 = cae.address3
            state = cae.state
            print state
            pincode= cae.pincode
            city = cae.city

        address_db={
            "address_type" : address_type,
            "address1" : address1,
            "address2" : address2,
            "address3" : address3,
            "state"    : state,
            "city"     : city,
            "pincode"  : pincode
            }
        addressDetailForm= AddressDetailForm(request.POST or None, initial=address_db)

    else:
        addressDetailForm=AddressDetailForm(request.POST or None, initial={
            "address_type" : address_type
        })

    return (addressDetailForm)


def saveAddress(roll_number, request, i,addressDetailForm,addressEntry):

    if addressDetailForm.is_valid():

        ad1=request.POST.getlist('address1')[i]
        ad2=request.POST.getlist('address2')[i]
        ad3=request.POST.getlist('address3')[i]
        st=request.POST.getlist('state')[i]
        pi=request.POST.getlist('pincode')[i]
        ci=request.POST.getlist('city')[i]

        if addressEntry:
             addressEntry.update(address_type=i,address1=ad1,address2=ad2,address3=ad3,state=st,city=ci,pincode=pi)
        else:
             instance=addressDetailForm.save(commit=False)
             instance.address_type=i
             instance.roll_number=roll_number
             instance.address1=ad1
             instance.address2 = ad2
             instance.address3 = ad3
             instance.state=st
             instance.pincode=pi
             instance.city= ci
             instance.save()

    transaction.commit()
    return (request)

def programDetailsView(request, roll_number):
    title = "Program Applying For"
    programDetailEntry=ProgramApplied.objects.filter(roll_number=roll_number)

    if programDetailEntry:
        for prde in programDetailEntry:
            pr=prde.program_id
            co=prde.course_id
            en=prde.exam_name_id
            es=prde.exam_subject_id
            ms=prde.marks_scored

        programDetailForm=ProgramDetailForm(request.POST or None, initial={
            "program_id"      :pr,
            "course_id"       :co,
            "exam_name_id"    :en,
            "exam_subject_id" :es,
            "marks_scored"    :ms

        })

    else:
        programDetailForm=ProgramDetailForm(request.POST or None)



    context={
        "title" : title,
        "programDetailForm" :programDetailForm,
        "roll_number": roll_number,
        "adminRef":admin_ref
    }


    if programDetailForm.is_valid():
        req=request.POST
        print req
        pr=req.getlist('program_id')[0]
        co=req.getlist('course_id')[0]
        en=req.getlist('exam_name_id')[0]
        es=req.getlist('exam_subject_id')[0]
        ms=req.getlist('marks_scored')[0]


        if programDetailEntry:

            programDetailEntry.update(program_id=pr,roll_number=roll_number,course_id=co,exam_name_id=en,
                                       exam_subject_id=es,marks_scored=ms)
        else:
            instance= programDetailForm.save(commit=False)
            instance.roll_number= roll_number
            instance.program_id=pr
            instance.course_id=co
            instance.exam_name_id=en
            instance.exam_subject_id=es
            instance.marks_scored=ms

            instance.save()


        transaction.commit()

    return render(request, "candidate_program_details.html", context)





def workExperienceView(request, roll_number):

    title = "Candidate Work Experience"

    workExperienceEntry=WorkExperience.objects.filter(roll_number=roll_number)
    print workExperienceEntry
    #ai=0
    if workExperienceEntry:
        print "true"
        for wee in workExperienceEntry:
            #ai=wee.workEx_id
            #print ai
            lo=wee.last_organisation
            po=wee.position
            jd=wee.job_description
            sy=wee.start_year
            ey=wee.end_year
            du=wee.duration


        workExperienceForm=WorkExperienceForm(request.POST or None, initial={
            "last_organisation" : lo,
            "position":po,
            "job_description":jd,
            "start_year":sy,
            "end_year":ey,
            "duration":du,


        })

    else:
        workExperienceForm=WorkExperienceForm(request.POST or None)

    context={
        "title" : title,
        "workExperienceForm" : workExperienceForm,
        "roll_number": roll_number,
        "adminRef":admin_ref
    }


    if workExperienceForm.is_valid():

        lo=request.POST.getlist('last_organisation')[0]
        po=request.POST.getlist('position')[0]
        jd=request.POST.getlist('job_description')[0]
        print jd
        sy=request.POST.getlist('start_year')[0]
        ey=request.POST.getlist('end_year')[0]
        du=request.POST.getlist('duration')[0]

        if workExperienceEntry:

            workExperienceEntry.update(last_organisation=lo,roll_number=roll_number,position=po,job_description=jd,
                                       start_year=sy,end_year=ey,duration=du)
        else:
            instance= workExperienceForm.save(commit=False)
            instance.roll_number= roll_number
            instance.last_organisation=lo
            instance.position=po
            instance.job_description=jd
            instance.start_year=sy
            instance.end_year=ey
            instance.duration=du

            instance.save()


        transaction.commit()

    return render(request, "candidate_workExperience.html", context)





def educationDetailsView(request, roll_number):
    title = "Candidate Educational Details"

    xEntry = EducationDetails.objects.filter(roll_number=roll_number,education_type=1)
    xiiEntry = EducationDetails.objects.filter(roll_number=roll_number,education_type=2)
    grEntry = EducationDetails.objects.filter(roll_number=roll_number,education_type=3)

    print xEntry, xiiEntry, grEntry

    xForm   = initiateEducationDetailForm("Xth",request,xEntry)
    xiiForm = initiateEducationDetailForm("XIIth",request,xiiEntry)
    grForm  = initiateEducationDetailForm("Graduation",request,grEntry)

    request = saveEducationDetails(roll_number,1,xEntry,xForm,0,request)
    request = saveEducationDetails(roll_number,2,xiiEntry,xiiForm,1,request)
    request = saveEducationDetails(roll_number,3,grEntry,grForm,2,request)

    context = {
        "roll_number" : roll_number,
        "title" : title,
        "xForm" : xForm,
        "xiiForm" : xiiForm,
        "grForm"  : grForm,
        "adminRef":admin_ref,
    }

    return render(request, "candidate_educationDetails.html",context)


def initiateEducationDetailForm(std,request,entry):

    if entry :
        for ed in entry:
            ty      = ed.education_type
            pe      = ed.percentage
            bo      = ed.board_university
            ins      = ed.institute
            yp      = ed.year_of_passing


        edForm = EducationalDetailForm(request.POST or None,initial={
            #"education_type"   : x_ty,
            "percentage"      : pe,
            "board_university"           : bo,
            "institute"       : ins,
            "year_of_passing" : yp
        })
    else :
        edForm = EducationalDetailForm(request.POST or None, initial={
            "education_type"   : std,
        })
    return (edForm)

def saveEducationDetails(roll_number,ty,edEntry, edForm,i,request):
    if edForm.is_valid():
        req=request.POST
        pe= req.getlist('percentage')[i]
        bo= req.getlist('board_university')[i]
        ins= req.getlist('institute')[i]
        yp= req.getlist('year_of_passing')[i]

        if edEntry:
            edEntry.update(education_type=ty,percentage=pe,board_university=bo,institute=ins,year_of_passing=yp)
        else:
            instance=edForm.save(commit=False)
            instance.education_type=ty
            instance.roll_number=roll_number
            instance.percentage=pe
            instance.board=bo
            instance.institute=ins
            instance.year_of_passing=yp
            instance.save()

    transaction.commit()

    return (request)


