from django.contrib import admin
from django.contrib.auth.models import User
from TMS.models import Tasks,StudentTasks
from django.core import serializers
from django.http import HttpResponse
import json

# def make_published(modeladmin, request, queryset):
#     users = User.objects.filter(is_active=1,is_staff=1,is_superuser=0, studenttasks__status='to-do',studenttasks__is_approved=False).all()
#     data = serializers.serialize("json", users)
#     context = json.dumps({'data': data})
#     return HttpResponse(context, content_type='application/json')
# make_published.short_description = "Assign Task"

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task_id', 'task_desc']
    ordering = ['task_id']
    # actions = [make_published]

admin.site.register(Tasks, TaskAdmin)
