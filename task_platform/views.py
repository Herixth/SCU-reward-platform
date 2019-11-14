from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def index(request):
    latest_task_list = Task.objects.order_by('-pub_time')[:5]
    #latest_task_list = [1, 2, 3]
    context = {'latest_task_list': latest_task_list}
    return render(request, 'task_platform/index.html', context)

def detail(request, task_id):
    return HttpResponse("你在浏览任务#%d的详细描述" % task_id)
 