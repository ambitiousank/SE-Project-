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
    validated_by=models.CharField(max_length=32)
    validation_comments=models.CharField(max_length=400,blank=True)
    created_on=models.DateField(auto_now_add=True)


class AddressDetails(models.Model):
    STATE_CHOICES = (
		(0, 'Select'),        
		(1, 'Andhra Pradesh'),
        (2, 'Arunachal Pradesh'),
        (3, 'Assam'),
        (4, 'Bihar'),
        (5, 'Chattisgarh'),
        (6, 'Karnataka')
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
        (2, 'SC/ST'),
        (3, 'OBC')
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



class PhotoFiles(models.Model):
    photoFile_id            = models.AutoField(primary_key=True)
    roll_number             = models.CharField(max_length=32, unique=True)
    photograph_file 	    = models.FileField(upload_to = settings.MEDIA_ROOT, null=True)

class SignatureFiles(models.Model):
    sigFile_id              = models.AutoField(primary_key=True)
    roll_number             = models.CharField(max_length=32, unique=True)
    signature_file 	        = models.FileField(upload_to = settings.MEDIA_ROOT, null=True)

class XthMarksheets (models.Model):
    xmFile_id              = models.AutoField(primary_key=True)
    roll_number             = models.CharField(max_length=32, unique=True)
    xth_marksheet           = models.FileField(upload_to = settings.MEDIA_ROOT, null = True)

# class XthCertificates (models.Model):
#     xcFile_id              = models.AutoField(primary_key=True)
#     roll_number             = models.CharField(max_length=32, unique=True)
#     xth_certificate         = models.FileField(upload_to = settings.MEDIA_ROOT, null = True)
#
#
# class XIIthMarksheets (models.Model):
#     xiimFile_id              = models.AutoField(primary_key=True)
#     roll_number             = models.CharField(max_length=32, unique=True)
#     xIIth_marksheet         = models.FileField(upload_to = settings.MEDIA_ROOT, null = True)
#
# class XIIthCertificates (models.Model):
#     xiicFile_id              = models.AutoField(primary_key=True)
#     roll_number             = models.CharField(max_length=32, unique=True)
#     xIIth_certificate       = models.FileField(upload_to = settings.MEDIA_ROOT, null = True)
#
# class GraduationMarksheets (models.Model):
#     gmFile_id              = models.AutoField(primary_key=True)
#     roll_number             = models.CharField(max_length=32, unique=True)
#     graduation_marksheet    = models.FileField(upload_to = settings.MEDIA_ROOT, null = True)
#
# class GraduationCertificates (models.Model):
#     gcFile_id              = models.AutoField(primary_key=True)
#     roll_number             = models.CharField(max_length=32, unique=True)
#     graduation_certificate  = models.FileField(upload_to = settings.MEDIA_ROOT, null = True)



class UploadDetails(models.Model):

    FILE_CHOICES=((1, 'Photograph'),
                  (2, 'Signature'),
                  (3, 'Xth Marksheet'),
                  (4, 'Xth Certificate'),
                  (5, 'XIIth Marksheet'),
                  (6, 'XIIth Certificate'),
                  (7, 'Graduation Marksheet'),
                  (8, 'Graduation Certificate'),
                  (9, 'Gate Score Card'),
                  (10, 'Salary Slip'))


    upload_id=models.AutoField(primary_key=True)
    roll_number=models.CharField(max_length=32)
    upload_type_id=models.ForeignKey(UploadTypeRef, choices=FILE_CHOICES)
    upload_path=models.CharField(max_length=100)

###New class
class AdminReference(models.Model):
    offer_choice=(
        (1, "admission"),
        (2, "job")
    )
    reference_id=models.PositiveSmallIntegerField(primary_key=True,default=1)
    offer_id=models.PositiveSmallIntegerField(choices=offer_choice,default="admission")
    created_by=models.CharField(max_length=32)
    created_on=models.DateField(auto_now_add=True)
    form_submission_date=models.DateField()

###New class
class GenderRef(models.Model):
    gender_id=models.AutoField(primary_key=True)
    gender_desc=models.CharField(max_length=32)
    created_on=models.DateField(auto_now_add=True)

###New class

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



