from __future__ import unicode_literals

from django.db import models
from django.conf import settings


# Create your models here.


class CategoryRef(models.Model):
    category_id=models.AutoField(primary_key=True)
    category_desc=models.CharField(max_length=32)
    created_on=models.DateField(auto_now_add=True)

class StateRef(models.Model):
    state_id=models.AutoField(primary_key=True)
    state_desc=models.CharField(max_length=32)
    created_on=models.DateField(auto_now_add=True)

class CourseRef(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_desc=models.CharField(max_length=32)
    created_on=models.DateField(auto_now_add=True)

class ExamRef(models.Model):
    exam_id=models.AutoField(primary_key=True)
    exam_desc=models.CharField(max_length=32)
    created_on=models.DateField(auto_now_add=True)

class ProgramRef(models.Model):
    program_id=models.AutoField(primary_key=True)
    program_desc=models.CharField(max_length=32)
    created_on=models.DateField(auto_now_add=True)

class PostRef(models.Model):
    post_id=models.AutoField(primary_key=True)
    post_desc=models.CharField(max_length=32)
    created_on=models.DateField(auto_now_add=True)

class ExamSubjectRef(models.Model):
    exam_subject_id=models.AutoField(primary_key=True)
    exam_subject_desc=models.CharField(max_length=32)
    created_on=models.DateField(auto_now_add=True)

class EducationRef(models.Model):
    education_id=models.AutoField(primary_key=True)
    education_desc=models.CharField(max_length=32)
    created_on=models.DateField(auto_now_add=True)

class UploadTypeRef(models.Model):

    upload_type_id=models.AutoField(primary_key=True)
    upload_type_desc=models.CharField(max_length=32)
    created_on=models.DateField(auto_now_add=True)



class AdmissionDetail(models.Model):
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'Valid'),
        (3, 'Incomplete'),
        (4, 'Invalid')
    )
    admission_id=models.AutoField(primary_key=True)
    roll_number=models.CharField(max_length=32,unique=True)
    status_of_request=models.IntegerField(choices=STATUS_CHOICES, default=1)
    validated_by=models.CharField(max_length=32,default='ok',null=True)
    validation_comments=models.CharField(max_length=400,blank=True,default='NA',null=True)
    created_on=models.DateField(auto_now_add=True)


class AddressDetails(models.Model):
    STATE_CHOICES = (
		(0, 'Select'),        
	    (1,'ANDAMAN & NICOBAR ISLANDS'),
        (2,'ANDHRA PRADESH'),
        (3,'ARUNACHAL PRADESH'),
        (4,'ASSAM'),
        (5,'BIHAR'),
        (6,'CHANDIGARH'),
        (7,'CHHATTISGARH'),
        (8,'DADRA & NAGAR HAVELI'),
        (9,'DAMAN & DIU '),
        (10,'GOA'),
        (11,'GUJARAT'),
        (12,'HARYANA'),
        (13,'HIMACHAL PRADESH'),
        (14,'JAMMU & KASHMIR'),
        (15,'JHARKHAND'),
        (16,'KARNATAKA'),
        (17,'KERALA'),
        (18,'LAKSHADWEEP'),
        (19,'MADHYA PRADESH'),
        (20,'MAHARASHTRA'),
        (21,'MANIPUR'),
        (22,'MEGHALAYA'),
        (23,'MIZORAM'),
        (24,'NAGALAND'),
        (25,'DELHI'),
        (26,'ORISSA'),
        (27,'PUDUCHERRY '),
        (28,'PUNJAB'),
        (29,'RAJASTHAN'),
        (30,'SIKKIM'),
        (31,'TAMIL NADU'),
        (32,'TELANGANA'),
        (33,'TRIPURA'),
        (34,'UTTAR PRADESH'),
        (35,'UTTARAKHAND'),
        (36,'WEST BENGAL'),

    )

    address_id=models.AutoField(primary_key=True)
    address_type=models.IntegerField(blank=True,default=1)
    roll_number=models.CharField(max_length=32)
    address1=models.CharField(max_length=100,blank=False)
    address2=models.CharField(max_length=100,blank=True)
    address3=models.CharField(max_length=100,blank=True)
    state=models.IntegerField(choices=STATE_CHOICES,default=0)
    pincode=models.CharField(max_length=6)
    city=models.CharField(max_length=50)

class PersonalDetail(models.Model):
    GENDER_CHOICES = (
    	(0, 'Select'),
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Others')
    )

    CATEGORY_CHOICES = (
    	(0, 'Select'),
        (1, 'Gen'),
        (2, 'SC'),
        (3, 'ST'),
        (4, 'OBC')
    )

    roll_number=models.CharField(max_length=32,unique=True,primary_key=True)
    full_name=models.CharField(max_length=32)
    father_name=models.CharField(max_length=32)
    mother_name=models.CharField(max_length=32)
    date_of_birth=models.DateField()
    gender=models.IntegerField(choices=GENDER_CHOICES,default=0)
    nationality=models.CharField(max_length=32)
    category_id=models.IntegerField(choices=CATEGORY_CHOICES,default=0)
    phone_number=models.CharField(max_length=10)
    pan_card=models.CharField(max_length=32,blank=True)
    email_id=models.EmailField()
    residential_address_id=models.IntegerField(default=0)
    current_address_id=models.IntegerField(default=0)



class EducationDetails(models.Model):
    EDUCATION_CHOICES = (
        (1, 'Xth'),
        (2, 'XIIth'),
        (3, 'Graduation')
    )
    education_id=models.AutoField(primary_key=True)
    roll_number=models.CharField(max_length=32)
    education_type=models.IntegerField(choices=EDUCATION_CHOICES, default=1)
    percentage=models.DecimalField(max_digits=4,decimal_places=2)
    board_university=models.CharField(max_length=32)
    institute=models.CharField(max_length=32)
    year_of_passing=models.IntegerField(default=2000)


class WorkExperience(models.Model):
    workEx_id=models.AutoField(primary_key=True)
    roll_number=models.CharField(max_length=32)
    last_organisation=models.CharField(max_length=100,blank=False)
    position=models.CharField(max_length=100,blank=False)
    job_description=models.CharField(max_length=100,blank=False)
    start_year=models.IntegerField(default=2000)
    end_year=models.IntegerField(default=2016)
    duration=models.IntegerField()

class ProgramApplied(models.Model):
    PROGRAM_CHOICES = (
    	(0, 'Select'),
        (1, 'M.Tech'),
        (2, 'Integrated M.Tech'),
        (3, 'M.Sc Digital Society'),
        (4, 'MS'),
        (5, 'PHD')
    )

    EXAM_CHOICES =(
    	(0, 'Select'),
        (1, 'GATE'),
        (2, 'GRE'),
        (3, 'JEE')
    )
    COURSE_CHOICES =(
    	(0, 'Select'),
        (1, 'IT'),
        (2, 'ESD')
    )
    SUBJECT_CHOICES = (
    	(0, 'Select'),
        (1, 'CS/IT'),
        (2, 'ECE')
    )
    program_applied_id=models.AutoField(primary_key=True)
    roll_number=models.CharField(max_length=32)
    program_id=models.IntegerField(choices=PROGRAM_CHOICES,default=0)
    course_id=models.IntegerField(choices=COURSE_CHOICES,default=0)
    exam_name_id=models.IntegerField(choices=EXAM_CHOICES,default=0)
    exam_subject_id=models.IntegerField(choices=SUBJECT_CHOICES,default=0)
    marks_scored=models.DecimalField(max_digits=4,decimal_places=2)

class PostApplied(models.Model):
    POST_CHOICES = (
    	(0, 'Select'),
        (1, 'Software Engineer'),
        (2, 'Data Analyst'),
        (3, 'Software Developer'),
        (4, 'IT')
    )

    post_applied_id=models.AutoField(primary_key=True)
    roll_number=models.CharField(max_length=32)
    post=models.IntegerField(choices=POST_CHOICES,default=0)



class UploadDetails(models.Model):

    

    upload_id=models.AutoField(primary_key=True)
    roll_number=models.CharField(max_length=32)
    upload_type=models.IntegerField(UploadTypeRef)
    upload_path=models.FileField(upload_to=settings.DOWNLOAD_ROOT)

###New class
class AdminReference(models.Model):
    template_choice=(
        (1, "Admission"),
        (2, "Job")
    )
    reference_id=models.AutoField(primary_key=True)
    form_template=models.PositiveSmallIntegerField(choices=template_choice,default=1)
    created_by=models.CharField(max_length=32)
    created_on=models.DateField(auto_now_add=True)
    form_submission_date=models.DateField()

###New class
class GenderRef(models.Model):
    gender_id=models.AutoField(primary_key=True)
    gender_desc=models.CharField(max_length=32)
    created_on=models.DateField(auto_now_add=True)

###New class

class SubmitStatus(models.Model):
    roll_number=models.CharField(max_length=32,primary_key=True)
    submission_status=models.PositiveSmallIntegerField(default=0)   # 0- Not_submitted; 1-Submitted

class User(models.Model):
    user_id     = models.AutoField(primary_key=True)
    roll_number = models.CharField(max_length=32,unique=True)
    name        = models.CharField(max_length=32)
    email_id    = models.EmailField(unique=True)
    password    = models.CharField(max_length=32)
    created_on  = models.DateField(auto_now_add=True)

#####New class

class AddressRef(models.Model):
    addRef_id = models.AutoField(primary_key=True)
    add_type_id= models.PositiveSmallIntegerField()
    add_desc=models.CharField(max_length=32)
    created_on=models.DateField(auto_now_add=True)



