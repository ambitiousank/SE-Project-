from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SignUp(models.Model):
	ROLE_CHOICES = (
        ('Admin', 'Administrator'),
        ('Staff', 'Staff'),
        ('User', 'Candidate')
    )
   
    
	name = models.CharField(max_length=30)         #for alphanumeric
	email = models.EmailField()
	password = models.CharField(max_length=20,default='12345678')
	confirmPassword = models.CharField(max_length=20,default='12345678')
	role = models.CharField(max_length=5, choices=ROLE_CHOICES, default=1) 
	approve = models.CharField(max_length=1, default='3')
	match = models.CharField(max_length=10)
	comment = models.CharField(max_length=40,blank=True)

	def __unicode__(self):
		return self.name,self.email,self.role,self.approve  #what unicode is displayed in admin after data is entered(should be string)


class MatchRef(models.Model):
    
    match_id=models.AutoField(primary_key=True)
    roll_no = models.CharField(max_length=10)  
    email = models.EmailField()
