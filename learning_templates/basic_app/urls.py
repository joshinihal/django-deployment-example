from django.conf.urls import url
from basic_app import views

#template tagging
#django will look for a variable called app_namw, set it equal to our current app
app_name='basic_app'

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other')
]