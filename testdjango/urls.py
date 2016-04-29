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
	url(r'^logsout/$','adminmodule.views.logsout',name='logout'),


	url(r'^staff/$','staffmodule.views.fetchPendingRequest',name='staffDashboard'),
	url(r'^studentDetailForm/(?P<admission_id>[0-9]+)/$','staffmodule.views.studentValidation',name='studentValidation'),
	url(r'^submitComments/$','staffmodule.views.submitComments',name='submitComments'),
	url(r'^staff_search/$','staffmodule.views.staffSearch',name='staffSearch'),

	url(r'^admin_module/', 'adminmodule.views.main', name="main"),
	url(r'^userAdmin1/$','adminmodule.views.formTemplate1',name='formTemplate1'),
	url(r'^userAdmin2/$','adminmodule.views.formTemplate2',name='formTemplate2'),
	url(r'^admin_req/', 'adminmodule.views.userReq', name="userReq"),
	url(r'^admin_users/', 'adminmodule.views.users', name="users"),
	url(r'^templates/', 'adminmodule.views.template', name="template"),
	url(r'^userDetailForm/(?P<email>[A-Za-z0-9@.]+)/$','adminmodule.views.userValidation',name='userValidation'),


	url(r'^candidate_home/(?P<roll_number>[A-Za-z0-9]+)/$', 'candidateModule.views.homeView', name='home'),
	url(r'^candidate_personal_details/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.personalDetailsView',name='personalDetails'),
    url(r'^candidate_address/(?P<id>per)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.addressView',name='permanentAddress'),
	url(r'^candidate_address/(?P<id>cur)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.addressView',name='currentAddress'),
    url(r'^candidate_academic_details/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.educationDetailsView',name='educationDetails'),
	url(r'^candidate_academic_details/(?P<id>1)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.stdEducationDetailsView',name='xthDetails'),
	url(r'^candidate_academic_details/(?P<id>2)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.stdEducationDetailsView',name='xiithDetails'),
	url(r'^candidate_academic_details/(?P<id>3)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.stdEducationDetailsView',name='gradDetails'),
    url(r'^candidate_work_experience/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.workExperienceView',name='workExperience'),
    url(r'^candidate_address_details/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.addressDetailsView',name='addressDetails'),
    url(r'^candidate_program_details/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.programDetailsView',name='programDetails'),
    url(r'^candidate_job_details/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.jobDetailsView',name='jobDetails'),
    url(r'^candidate_file_upload/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.fileUploadView',name='fileUpload'),
    url(r'^candidate_photo_upload/(?P<upload_doc>photo)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.fileDetailsView',name='photoUpload'),
    url(r'^candidate_sign_upload/(?P<upload_doc>sign)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.fileDetailsView',name='signUpload'),
    url(r'^candidate_xm_upload/(?P<upload_doc>xm)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.fileDetailsView',name='xMarkUpload'),
	url(r'^candidate_xc_upload/(?P<upload_doc>xc)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.fileDetailsView',name='xCertUpload'),
    url(r'^candidate_xiim_upload/(?P<upload_doc>xiim)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.fileDetailsView',name='xiiMarkUpload'),
    url(r'^candidate_xiic_upload/(?P<upload_doc>xiic)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.fileDetailsView',name='xiiCerUpload'),
	url(r'^candidate_gm_upload/(?P<upload_doc>gm)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.fileDetailsView',name='gradMarkUpload'),
    url(r'^candidate_gc_upload/(?P<upload_doc>gc)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.fileDetailsView',name='gradCertUpload'),
    url(r'^candidate_sc_upload/(?P<upload_doc>sc)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.fileDetailsView',name='scoreCardUpload'),
	url(r'^candidate_ss_upload/(?P<upload_doc>ss)/(?P<roll_number>[A-Za-z0-9]+)/$','candidateModule.views.fileDetailsView',name='salarySlipUpload'),
	url(r'^candidate_submit/(?P<roll_number>[A-Za-z0-9]+)/$', 'candidateModule.views.submitView', name='submit'),
	
	
	url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:

	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns+= static(settings.DOWNLOAD_URL, document_root=settings.DOWNLOAD_ROOT)
