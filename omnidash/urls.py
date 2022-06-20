from django.conf import settings
from django.conf.urls import url
from mysite.settings import MEDIA_ROOT
from .import views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.handellogin,name='handellogin'),
    url(r'^home/$',views.index,name='index'),
    url(r'^leave/$',views.leaves,name='leave'),
    url(r'^req/$',views.req,name='req'),
    url(r'^reimbursemnt/$',views.remb,name='rem'),
    url(r'^attendance/$',views.atten,name='att'),
    url(r'^logout/$',views.logout,name='logout'),

]+static(settings.MEDIA_URL,document_root=MEDIA_ROOT )