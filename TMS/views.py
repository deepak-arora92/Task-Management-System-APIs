from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login as django_login, authenticate
from models import *
import json

TASK_STATUS = ['to-do', 'doing', 'done']
APPROVAL_STATUS = ['approved, disapproved']

def index(request):
     return HttpResponse("Hello World")

@login_required()
def task_detail(request,task_id):
     """ fetch a task description """
     t = Tasks.objects.filter(task_id=task_id).first()
     if t is not None:
          students = User.objects.filter(studenttasks__task_id=task_id)
          studds = [i.username for i in students]
          print "students: {0}".format(list(students))
          data = json.dumps({"task_desc": t.task_desc,"assigned_to":studds})
     else:
          data="task doesnt exist."
     return HttpResponse(data, content_type='application/json')

def assign_task_to_users(task_id,user_list):
     status={}
     assigned,alreday_assigned,dont_exist=[],[],[]
     for user_id in user_list:
          u = User.objects.filter(id = user_id).first()
          if u:
               obj, created = StudentTasks.objects.get_or_create(task_id = task_id,user_id=user_id)
               if not created:
                    alreday_assigned.append(str(int(u.id)) + "-" + u.username)
                    status.update({"Already Assigned to ": alreday_assigned})
               else:
                    assigned.append(str(int(u.id)) + "-" + u.username)
                    status.update({"Assigned to ": assigned})
          else:
               dont_exist.append(user_id)
               status.update({"student ids dont Exist":dont_exist})
     return status

@login_required()
def assign_task(request,task_id):
     """ assign taskt to students."""
     a=""
     if request.GET and request.user.is_superuser:
          t = Tasks.objects.filter(task_id=task_id).first()
          if t is not None:
               task_id = t.task_id
               user_ids = request.GET.get('student')
               user_list = map(int,user_ids.split(','))
               if len(user_list)>0:
                    status = assign_task_to_users(task_id,user_list)
                    print "status:{0}".format(status)
                    if len(status) > 0:
                         a = json.dumps({"msg":"Error: {0}".format(status)})
                    else:
                         a=json.dumps({"msg":"Assigned Successfully"})
               else:
                    a = json.dumps({"msg":"Please give valid user ids."})
          else:
               a = json.dumps({"msg":"Given Task Id doesnt exist."})
     else:
          a = json.dumps({"msg":"students doesnt have permission for this operation."})
     return HttpResponse(a, content_type='application/json')

@login_required()
def update_status(request,task_id):
     """ update task status by students"""
     user_id = request.user.id
     print "usr:{0}".format(user_id)
     st = request.GET.get('status')
     if st not in TASK_STATUS:
          a = json.dumps({"msg":"Invalid Status"})
          return HttpResponse(a, content_type='application/json')
     t = Tasks.objects.filter(task_id=task_id).first()
     if t is not None:
          s =  StudentTasks.objects.filter(task_id = task_id,user_id=user_id)
          if s.exists():
               StudentTasks.objects.filter(task_id = task_id,user_id=user_id).update(status=st)
               a = json.dumps({"msg":"The following task has been updated successfully as: {0}.Task: {1}".format(st,t.task_desc)})
          else:
               a = json.dumps({"msg":"Task is not assigned to the student."})
     else:
          a = json.dumps({"msg":"Given Task Id doesnt exists."})
     return HttpResponse(a, content_type='application/json')

@login_required()         
def approve_disapprove(request,task_id,approval_status = None):
     """ update task status by Admin"""
     
     if request.GET and request.user.is_superuser:
          task_approval_status = 1 if approval_status == 'approved' else 2
          t = Tasks.objects.filter(task_id=task_id).first()
          if t is not None:
               user_ids = request.GET.get('student')
               user_list = map(int,user_ids.split(','))
               if len(user_list)>0:
                    unassigned_users=[]
                    for user_id in user_list:
                         s =  StudentTasks.objects.filter(task_id = task_id,user_id=user_id)
                         if s.exists():
                              StudentTasks.objects.filter(task_id = task_id,user_id=user_id).update(is_approved=task_approval_status)
                              a = json.dumps({"msg":"The following task has been updated successfully as:{0}. Task: {1}".format(approval_status,t.task_desc)})
                         else:
                              unassigned_users.append(user_id)
                              print "get:{0}".format(unassigned_users)
                    if len(unassigned_users) > 0:
                         a = json.dumps({"msg":"Task is not assigned to the students: {0}".format(unassigned_users)})
               else:
                    a = json.dumps({"msg":"provide assigned user(s) for approval/Disapporval."})
          else:
               a = json.dumps({"msg":"Given Task Id doesnt exist."})
     else:
          a = json.dumps({"msg":"students doesnt have permission for this operation."})
     return HttpResponse(a, content_type='application/json')

