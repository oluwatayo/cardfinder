from django.conf.urls import url
from . import views

app_name = 'lostcard'

urlpatterns = [
    #/lostcard/
    url(r'^$', views.home, name='home'),

    url(r'^send/mail/', views.mail, name='mail'),

    url(r'^search/result', views.search, name='search'),
    
    url(r'^about', views.about, name='about'),

    url(r'^lost/form/submit', views.lost_form_submit, name='lost_form_submit'),

    url(r'^found/form/submit', views.found_form_submit, name='found_form_submit'),

    url(r'^lost/form', views.lost_form, name='lost_form'),

    url(r'^found/form', views.found_form, name='found_form'),

    url(r'^lost', views.LostIndexView.as_view(), name='lost_index'),

    url(r'^found', views.FoundIndexView.as_view(), name='found_index'),

    #/lostcard/Card_id/
    url(r'^(?P<pk>[0-9]+)/lost/$',views.LostDetailView.as_view(), name='lost_details'),

    url(r'^(?P<pk>[0-9]+)/found/$',views.FoundDetailView.as_view(), name='found_details'),



]
