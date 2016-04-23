"""testdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	url(r'^$', 'module1.views.sign', name="sign"),
	url(r'^login/', 'module1.views.login1', name="login1"),


	url(r'^staff/$','staffmodule.views.fetchPendingRequest',name='staffDashboard'),
	url(r'^studentDetailForm/(?P<admission_id>[0-9]+)/$','staffmodule.views.studentValidation',name='studentValidation'),
	url(r'^submitComments/$','staffmodule.views.submitComments',name='submitComments'),
	url(r'^staff_search/$','staffmodule.views.staffSearch',name='staffSearch'),

	url(r'^admin_module/', 'adminmodule.views.main', name="main"),
	url(r'^userAdmin1/$','adminmodule.views.formTemplate1',name='formTemplate1'),
	url(r'^userAdmin2/$','adminmodule.views.formTemplate2',name='formTemplate2'),
	url(r'^admin_req/', 'adminmodule.views.users', name="users"),
	url(r'^templates/', 'adminmodule.views.template', name="template"),


	url(r'^home/(?P<roll_number>[A-Za-z0-9]+)/$', 'candidateModule.views.homeView', name='home'),
    url(r'^candidate_personal_details/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.personalDetailsView',name='personalDetails'),
    url(r'^candidate_academic_details/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.educationDetailsView',name='educationDetails'),
    url(r'^candidate_work_experience/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.workExperienceView',name='workExperience'),
    url(r'^candidate_address_details/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.addressDetailsView',name='addressDetails'),
    url(r'^candidate_program_details/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.programDetailsView',name='programDetails'),
    url(r'^candidate_job_details/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.jobDetailsView',name='jobDetails'),
    url(r'^candidate_file_upload/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.fileUploadView',name='fileUpload'),
    url(r'^candidate_photo_upload/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.photoUploadView',name='photoUpload'),
    url(r'^candidate_sign_upload/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.signUploadView',name='signUpload'),
    url(r'^candidate_xm_upload/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.xmUploadView',name='xmUpload'),

	
	
	
	url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:

	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   
