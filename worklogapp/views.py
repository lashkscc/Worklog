from django.shortcuts import get_object_or_404, render
from .models import Status, Task, TaskComment
from .forms import TaskForm, TaskCommentForm

# Create your views here.
def index (request):
    return render(request, 'worklogapp/index.html')

def todo (request):
    # status = get_object_or_404(Status, pk=1)
    task_list = Task.objects.filter(taskStatus = 1)
    return render(request, 'worklogapp/todo.html', {'task_list': task_list})

def inprogress (request):
    task_list = Task.objects.filter(taskStatus = 2)
    return render(request, 'worklogapp/inprogress.html', {'task_list': task_list})

def done (request):
    task_list = Task.objects.filter(taskStatus = 3)
    return render(request, 'worklogapp/done.html', {'task_list': task_list})

def task (request, id):
    tasktarget = get_object_or_404(Task, pk=id)
    taskcomments = TaskComment.objects.filter(taskid=tasktarget.id)
    return render(request, 'worklogapp/task.html', {'task': tasktarget, 'taskcomments': taskcomments})

def loginmessage(request):
    return render(request, 'worklogapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'worklogapp/logoutmessage.html')

def newtask(request):
    form = TaskForm

    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=TaskForm()

    else:
        form=TaskForm
    return render(request, 'worklogapp/newtask.html', {'form': form})

def newcomment(request):
    form = TaskCommentForm

    if request.method=='POST':
        form=TaskCommentForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=TaskCommentForm()

    else:
        form=TaskCommentForm()
    return render(request, 'worklogapp/newtask.html', {'form': form})    