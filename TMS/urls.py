
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^[index/]*$', views.index, name='index'),
    url(r'task/(?P<task_id>[0-9]+)/$',views.task_detail,name='task_detail'),
    url(r'task/(?P<task_id>[0-9]+)/assign/$',views.assign_task,name='assign_task'),
    url(r'task/(?P<task_id>[0-9]+)/approve/$',views.approve_disapprove,{'approval_status' : "approved"}, name='approve_disapprove'),
    url(r'task/(?P<task_id>[0-9]+)/disapprove/$',views.approve_disapprove, {'approval_status' : "disapproved"},  name='approve_disapprove'),
    url(r'^task/(?P<task_id>[0-9]+)/update_status$', views.update_status, name='update_status'),
]
