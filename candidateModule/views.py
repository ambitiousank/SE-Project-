from django.shortcuts import render
from django.db import transaction
from django import forms
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist


from .forms import PersonalDetailForm, \
    EducationalDetailForm, WorkExperienceForm,AddressDetailForm,ProgramDetailForm,JobDetailForm, \
    FileUploadForm,FormSubmissionForm#,PhotoUploadForm

from staffmodule.models import AdmissionDetail,PersonalDetail,EducationDetails, \
    AddressDetails,WorkExperience,ProgramApplied,ExamRef,CourseRef, \
    ExamSubjectRef,CategoryRef,StateRef,ProgramRef,UploadDetails, \
    AdminReference,PostApplied,User,SubmitStatus,AddressRef,UploadTypeRef





# here we have to validate roll_number of a user in the url as well only then we'll allow access

resAddType = AddressRef.objects.get(add_desc='residential')
PERMANENT_ADDRESS_TYPE = resAddType.add_type_id

curAddType = AddressRef.objects.get(add_desc='current')
CURRENT_ADDRESS_TYPE = curAddType.add_type_id;


ADMISSION_TYPE=1
JOB_TYPE=2
NOT_SUBMITTED=0
SUBMITTED=1



try:
    admin_ref =AdminReference.objects.get(reference_id=1)
    form_template=admin_ref.form_template
except ObjectDoesNotExist:
    form_template =ADMISSION_TYPE





"""

To Show all the information provided by the candidate, we collect information from different tables and present it as an
html page. A candidate can verify how his/her information will look once the form is submitted

"""
def homeView(request, roll_number):

    title="Candidate Details "
    context={"title":title,"roll_number": roll_number}

    resAddType=AddressRef.objects.get(add_desc='residential')
    PERMANENT_ADDRESS_TYPE=resAddType.add_type_id;
    print "PERMANENT_ADDRESS_TYPE===";print PERMANENT_ADDRESS_TYPE

    curAddType=AddressRef.objects.get(add_desc='current')
    CURRENT_ADDRESS_TYPE=curAddType.add_type_id;
    print "CURRENT_ADDRESS_TYPE==";print CURRENT_ADDRESS_TYPE

    try:
        try:
            personal_details = PersonalDetail.objects.get(roll_number=roll_number.upper())
        except ObjectDoesNotExist:
            personal_details=PersonalDetail.objects.get(roll_number=roll_number.lower())
        context.update({"personal":personal_details})

    except ObjectDoesNotExist:
        pass

    else:
        try:
            category_details= CategoryRef.objects.get(category_id =personal_details.category_id)
            category=category_details.category_desc
            context.update({"category":category})
        except ObjectDoesNotExist:
            pass
        try:
            educational_details=EducationDetails.objects.filter(roll_number=roll_number)
            context.update({"education_details":educational_details})
        except ObjectDoesNotExist:
            pass
        try:
            permanentAddress=AddressDetails.objects.get(roll_number=roll_number,address_type=PERMANENT_ADDRESS_TYPE)
            context.update({"permanent_address":permanentAddress})
        except ObjectDoesNotExist:
            pass
        try:
            currentAddress=AddressDetails.objects.get(roll_number=roll_number,address_type=CURRENT_ADDRESS_TYPE)
            context.update({"current_address":currentAddress})
        except ObjectDoesNotExist:
            pass
        work_experience=WorkExperience.objects.filter(roll_number=roll_number)

        context.update({"work_ex":work_experience})

    #if institute is offering admission
    if form_template==ADMISSION_TYPE:
        try:
            program_applied=ProgramApplied.objects.get(roll_number=roll_number)
        except ObjectDoesNotExist:
            pass
        else:
            program=ProgramRef.objects.get(program_id=program_applied.program_id)
            exam_details=ExamRef.objects.get(exam_id=program_applied.exam_name_id)
            exam_subject_details=ExamSubjectRef.objects.get(exam_subject_id=program_applied.exam_subject_id)
            course_details=CourseRef.objects.get(course_id=program_applied.course_id)
            exam=exam_details.exam_desc
            course=course_details.course_desc
            subject=exam_subject_details.exam_subject_desc
            program_name=program.program_desc


            context.update({
                "program":program_applied,
                "exam":exam,
                "course":course,
                "subject":subject,
                "program_name":program_name,
            })

    #if institute is offering a job
    elif form_template==JOB_TYPE:
        try:
            post=PostApplied.objects.get(roll_number=roll_number)
        except ObjectDoesNotExist:
            pass
        else:
            context.update({"post":post})


    upload=UploadDetails.objects.filter(roll_number=roll_number)
    for k in upload:
        path,filename=k.upload_path.name.split('/media/')
        k.upload_path=filename
        print "<<<<Upload Type>>>"
        print k.upload_type
	    #print k.upload_type.upload_type_desc

    context.update({
        #"form":form,
        "form_template":form_template,
        "filename":"/xth_"+roll_number+".pdf",
        "filename2":"/photo_"+roll_number+".jpg",
        "upload":upload
    })
    try:
        subStatus =SubmitStatus.objects.get(roll_number=roll_number)
        submission_status=subStatus.submission_status
    except ObjectDoesNotExist:
        submission_status =NOT_SUBMITTED

    if submission_status ==SUBMITTED:
         return render (request,"candidate_form_disabled.html",context)

    return render (request, "candidate_home.html",context)


def fileUploadView(request,roll_number):

    try:
        subStatus =SubmitStatus.objects.get(roll_number=roll_number)
        submission_status=subStatus.submission_status
    except ObjectDoesNotExist:
        submission_status =NOT_SUBMITTED

    if submission_status ==SUBMITTED:
        return HttpResponseRedirect("/candidate_home/"+roll_number+"/")

    title= "File Upload List"
    context={
        "title" : title,
        "roll_number" : roll_number,
        "form_template":form_template
    }

    return render(request, "candidate_upload_file_list.html",  context)


def fileDetailsView(request,upload_doc,roll_number):

    try:
        subStatus =SubmitStatus.objects.get(roll_number=roll_number)
        submission_status=subStatus.submission_status
    except ObjectDoesNotExist:
        submission_status =NOT_SUBMITTED

    if submission_status ==SUBMITTED:
        return HttpResponseRedirect("/candidate_home/"+roll_number+"/",{"submitted":"submitted"})


    print "<<<<<<fileDetails--request.POST>>>"
    print request.POST

    if upload_doc=="photo":
        uploaded_doc='Photograph'
        upload_type=UploadTypeRef.objects.get(upload_type_desc=uploaded_doc)
        upload_type_id=upload_type.upload_type_id

    elif upload_doc=="sign":
        uploaded_doc='Signature'
        upload_type=UploadTypeRef.objects.get(upload_type_desc=uploaded_doc)
        upload_type_id=upload_type.upload_type_id

    elif upload_doc=="xm":
        uploaded_doc='Xth Marksheet'
        upload_type=UploadTypeRef.objects.get(upload_type_desc=uploaded_doc)
        upload_type_id=upload_type.upload_type_id

    elif upload_doc=="xc":
        uploaded_doc='Xth Certificate'
        upload_type=UploadTypeRef.objects.get(upload_type_desc=uploaded_doc)
        upload_type_id=upload_type.upload_type_id

    elif upload_doc=="xiim":
        uploaded_doc='XIIth Marksheet'
        upload_type=UploadTypeRef.objects.get(upload_type_desc=uploaded_doc)
        upload_type_id=upload_type.upload_type_id

    elif upload_doc=="xiic":
        uploaded_doc='XIIth Certificate'
        upload_type=UploadTypeRef.objects.get(upload_type_desc=uploaded_doc)
        upload_type_id=upload_type.upload_type_id

    elif upload_doc=="gm":
        uploaded_doc='Graduation Marksheet'
        upload_type=UploadTypeRef.objects.get(upload_type_desc=uploaded_doc)
        upload_type_id=upload_type.upload_type_id

    elif upload_doc=="gc":
        uploaded_doc='Graduation Certificate'
        upload_type=UploadTypeRef.objects.get(upload_type_desc=uploaded_doc)
        upload_type_id=upload_type.upload_type_id

    elif upload_doc=="sc":
        uploaded_doc='Gate Score Card'
        upload_type=UploadTypeRef.objects.get(upload_type_desc=uploaded_doc)
        upload_type_id=upload_type.upload_type_id

    elif upload_doc=="ss":
        uploaded_doc='Salary Slip'
        upload_type=UploadTypeRef.objects.get(upload_type_desc=uploaded_doc)
        upload_type_id=upload_type.upload_type_id

    else:
        uploaded_doc=''
        upload_type_id=0

    title= uploaded_doc+" Upload Details"

    if request.POST:
        ufForm=FileUploadForm(request.POST,request.FILES)
    else:
        ufForm=FileUploadForm(request.POST or None)

    if ufForm.is_valid():

        try:
            fileEntry=UploadDetails.objects.get(roll_number=roll_number, upload_type=upload_type_id)
            upload_path = request.FILES["upload_path"]
            fileEntry.upload_path=upload_path

            print "<<<<fileEntry:::PK>>>>"
            print fileEntry._get_pk_val()

            fileEntry.save(force_update=True,update_fields=["upload_path"])

        except ObjectDoesNotExist:
            uf=UploadDetails(roll_number=roll_number,upload_path = request.FILES["upload_path"],upload_type=upload_type_id)
            uf.save()



    context={
        "title" : title,
        "ufForm" :ufForm,
        "roll_number": roll_number,
        "upload_type":upload_type_id,
        "form_template":form_template
    }
    print ">>>before valid "
    print request.POST

    transaction.commit()
    return render(request, "candidate_file_details.html",  context)

def submitView(request, roll_number):
    try:
        subStatus = SubmitStatus.objects.get(roll_number=roll_number)
        submission_status = subStatus.submission_status
    except ObjectDoesNotExist:
        submission_status =NOT_SUBMITTED

    if submission_status ==SUBMITTED:
        return HttpResponseRedirect("/candidate_home/"+roll_number+"/")

    title = "Submission Form"
    subForm=FormSubmissionForm(request.POST or None)

    context={
        "title" : title,
        "subForm" :subForm,
        "roll_number": roll_number,
        "form_template":form_template
    }

    print "<<<<<submit request>>>>>"
    print request.POST
    if subForm.is_valid():
        print "<<<<<Valid submit request>>>>>"
        print request.POST

        ss=SubmitStatus.objects.filter(roll_number=roll_number)
        print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        print SubmitStatus._meta.get_fields(include_parents=True,include_hidden=True,)
        if ss:
            ss.roll_number=roll_number
            ss.submission_status=SUBMITTED
            ss.save(force_update=True)
        else:
            ss=SubmitStatus(roll_number=roll_number, submission_status=SUBMITTED)
            ss.save(force_insert=True)
        transaction.commit()
        print "<<<<<Valid submit request:::SAVED_USER>>>>>"
        print ss.pk

        ad=AdmissionDetail.objects.filter(roll_number=roll_number)
        if ad:
            ad.status_of_request=SUBMITTED
            ad.save(force_update=True,updated_fields=["status_of_request"])
        else:
            ad=AdmissionDetail(roll_number=roll_number,status_of_request=SUBMITTED,validated_by="NA")
            ad.save(force_insert=True)
        transaction.commit()
        return HttpResponseRedirect("/candidate_home/"+roll_number+"/")
    return render(request, "candidate_submit.html", context)



def jobDetailsView(request, roll_number):
    try:
        subStatus =SubmitStatus.objects.get(roll_number=roll_number)
        submission_status=subStatus.submission_status
    except ObjectDoesNotExist:
        submission_status =NOT_SUBMITTED

    if submission_status ==SUBMITTED:
        return HttpResponseRedirect("/candidate_home/"+roll_number+"/")

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
        "form_template":form_template
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
    try:
        subStatus =SubmitStatus.objects.get(roll_number=roll_number)
        submission_status=subStatus.submission_status
    except ObjectDoesNotExist:
        submission_status =NOT_SUBMITTED

    if submission_status ==SUBMITTED:
        return HttpResponseRedirect("/candidate_home/"+roll_number+"/")

    title = "Candidate Personal Details"
    context={"form_template":form_template,
             "title" : title,
             "roll_number" : roll_number,
             }

    pd_entries = PersonalDetail.objects.filter(roll_number=roll_number.upper())
    if not pd_entries:
        pd_entries=PersonalDetail.objects.filter(roll_number=roll_number.lower())

    if pd_entries:
        full_name='';father_name='';mother_name='';date_of_birth='';gender='';nationality='';category_id='';
        phone_number='';pan_card='';email_id='';

        for pd_entry in pd_entries:
            roll_number     = pd_entry.roll_number
            full_name       = pd_entry.full_name
            father_name     = pd_entry.father_name
            mother_name     = pd_entry.mother_name
            date_of_birth   = pd_entry.date_of_birth
            gender          = pd_entry.gender
            nationality     = pd_entry.nationality
            category_id     = pd_entry.category_id
            phone_number    = pd_entry.phone_number
            pan_card        = pd_entry.pan_card
            email_id        = pd_entry.email_id

        pdForm=PersonalDetailForm(request.POST or None,initial={
            'roll_number'       : roll_number,
            'full_name'         : full_name,
            'father_name'       : father_name,
            'mother_name'       : mother_name,
            'date_of_birth'     : date_of_birth,
            'gender'            : gender,
            'nationality'       : nationality,
            'category_id'       : category_id,
            'phone_number'      : phone_number,
            'pan_card'          : pan_card,
            'email_id'          : email_id
        })
    else:
        pdForm=PersonalDetailForm(request.POST or None)
    context.update({
        "pdForm" : pdForm,

    })

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

        if pd_entries:
            pd_entries.update(roll_number=roll_number,full_name=fu,father_name=fa,mother_name=mo,date_of_birth=da,gender=ge,
                              nationality=na,category_id=ca,phone_number=ph,pan_card=pa,email_id=em)
        else:
            instance=pdForm.save(commit=False)
            instance.roll_number=roll_number
            instance.full_name=fu
            instance.father_name=fa
            instance.mother_name=mo
            instance.date_of_birth=da
            instance.gender=ge
            instance.nationality=na
            instance.category_id=ca
            instance.phone_number=ph
            instance.pan_card=pa
            instance.email_id=em
            instance.save()

        transaction.commit()

    return render(request, "candidate_personalDetails.html",context)



def addressDetailsView(request,roll_number):

    try:
        subStatus =SubmitStatus.objects.get(roll_number=roll_number)
        submission_status=subStatus.submission_status
    except ObjectDoesNotExist:
        submission_status =NOT_SUBMITTED

    if submission_status ==SUBMITTED:
        return HttpResponseRedirect("/candidate_home/"+roll_number+"/")

    title= "Address List"
    context={
        "title" : title,
        "roll_number" : roll_number,
        "form_template":form_template
    }

    return render(request, "candidate_address_list.html",  context)




def addressView(request,id,roll_number):

    title="Address Details"
    if id == 'per':
        address_type_name = "Permanent"
        address_type = PERMANENT_ADDRESS_TYPE
    elif id == 'cur':
        address_type_name = "Current"
        address_type = CURRENT_ADDRESS_TYPE

    print "<<<<address_type from DB>>>>"
    print address_type

    addressEntry = AddressDetails.objects.filter(roll_number=roll_number, address_type=address_type)
    addressDetailsForm = initiateAddressForm(address_type,request,addressEntry)

    request=saveAddress(roll_number,request,address_type,addressDetailsForm,addressEntry)
    updateAddressInPersonalDetails(roll_number,address_type)

    context={
        "title" : title,
        "address":addressDetailsForm,
        "roll_number":roll_number,
        "form_template":form_template,
        "address_type_name":address_type_name,
    }
    return render(request, "candidate_address_details.html", context)



##

def updateAddressInPersonalDetails(roll_number,address_type):


    print "<<<addressType>>>"
    print address_type


    if address_type == PERMANENT_ADDRESS_TYPE:

        perDetail=PersonalDetail.objects.get(roll_number=roll_number)
        latestPerAddressEntry = AddressDetails.objects.get(roll_number=roll_number, address_type=PERMANENT_ADDRESS_TYPE)
        print "perDetail.residential_address_id"
        print perDetail.residential_address_id
        print "latestPerAddressEntry.address_id"
        print latestPerAddressEntry.address_id
        if (perDetail.residential_address_id != latestPerAddressEntry.address_id):
             perDetail.residential_address_id=latestPerAddressEntry.address_id
             print "residential_address_id"
             print perDetail.residential_address_id
             perDetail.save(force_update=True,update_fields=["residential_address_id"])
             transaction.commit()
    elif address_type == CURRENT_ADDRESS_TYPE:
        perDetail=PersonalDetail.objects.get(roll_number=roll_number)
        latestCurAddressEntry = AddressDetails.objects.get(roll_number=roll_number, address_type=CURRENT_ADDRESS_TYPE)
        if (perDetail.current_address_id != latestCurAddressEntry.address_id):
             perDetail.current_address_id = latestCurAddressEntry.address_id
             perDetail.save(force_update=True,update_fields=["current_address_id"])
             transaction.commit()
    else:
        pass
    return()

def initiateAddressForm(address_type,request, addressEntry):

    if addressEntry:
        for ae in addressEntry:
            address_type =ae.address_type
            address1 = ae.address1
            address2 = ae.address2
            address3 = ae.address3
            state = ae.state
            pincode= ae.pincode
            city = ae.city

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

        ad1=request.POST.getlist('address1')[0]
        ad2=request.POST.getlist('address2')[0]
        ad3=request.POST.getlist('address3')[0]
        st=request.POST.getlist('state')[0]
        pi=request.POST.getlist('pincode')[0]
        ci=request.POST.getlist('city')[0]

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
    try:
        subStatus =SubmitStatus.objects.get(roll_number=roll_number)
        submission_status=subStatus.submission_status
    except ObjectDoesNotExist:
        submission_status =NOT_SUBMITTED

    if submission_status ==SUBMITTED:
        return HttpResponseRedirect("/candidate_home/"+roll_number+"/")

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
        "form_template":form_template
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
    try:
        subStatus =SubmitStatus.objects.get(roll_number=roll_number)
        submission_status=subStatus.submission_status
    except ObjectDoesNotExist:
        submission_status =NOT_SUBMITTED

    if submission_status ==SUBMITTED:
        return HttpResponseRedirect("/candidate_home/"+roll_number+"/")

    title = "Candidate Work Experience"
    workExperienceEntry=None

    context={
        "title" : title,
        "roll_number": roll_number,
        "form_template":form_template
    }


    workExperienceEntry=WorkExperience.objects.filter(roll_number=roll_number)


    if workExperienceEntry:
        lo='';po='';jd='';sy='';ey='';du='';
        for wee in workExperienceEntry:
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

    context.update({"workExperienceForm" : workExperienceForm})


    if workExperienceForm.is_valid():

        lo=request.POST.getlist('last_organisation')[0]
        po=request.POST.getlist('position')[0]
        jd=request.POST.getlist('job_description')[0]
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


def educationDetailsView(request,roll_number):
    try:
        subStatus =SubmitStatus.objects.get(roll_number=roll_number)
        submission_status=subStatus.submission_status
    except ObjectDoesNotExist:
        submission_status =NOT_SUBMITTED

    if submission_status ==SUBMITTED:
        return HttpResponseRedirect("/candidate_home/"+roll_number+"/")

    title= "Education Details"
    context={
        "title" : title,
        "roll_number" : roll_number,
         "form_template":form_template,
    }

    return render(request, "candidate_educational_details.html",  context)


def stdEducationDetailsView(request, id, roll_number):

    if id== "1":
        type=1
        std="Xth"
    elif id=="2":
        type=2
        std="XIIth"
    else:
        type=3
        std="Graduation"

    title = std+" Details"

    edEntry = EducationDetails.objects.filter(roll_number=roll_number,education_type=type)
    edForm   = initiateEducationDetailForm(id,request,edEntry)

    request = saveEducationDetails(roll_number,type,edEntry,edForm,0,request)

    context = {
        "std" : std,
        "roll_number" : roll_number,
        "title" : title,
        "edForm" : edForm,
        "form_template":form_template,
    }

    return render(request, "candidate_std_details.html",context)


def initiateEducationDetailForm(std,request,entry):

    if entry :
        for ed in entry:
            ty      = ed.education_type
            pe      = ed.percentage
            bo      = ed.board_university
            ins      = ed.institute
            yp      = ed.year_of_passing


        edForm = EducationalDetailForm(request.POST or None,initial={
            "education_type"   : ty,
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
            instance.board_university=bo
            instance.institute=ins
            instance.year_of_passing=yp
            instance.save()

    transaction.commit()

    return (request)


