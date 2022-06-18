from django.shortcuts import get_object_or_404, redirect, render
from .models import Status, Task, TaskComment
from .forms import TaskForm, TaskCommentForm, TaskStatusForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    todo_list = Task.objects.filter(taskStatus = 1)    
    inprogress_list = Task.objects.filter(taskStatus = 2)
    done_list = Task.objects.filter(taskStatus = 3)

    context = {
        'todo_list': todo_list,
        'inprogress_list': inprogress_list,
        'done_list': done_list,
        'range': max(len(todo_list), len(inprogress_list), len(done_list)),
    }
    return render(request, 'worklogapp/index.html', context)

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
    task = Task.objects.get(id=id)
    taskcomments = TaskComment.objects.filter(taskid=task.id)
    form = TaskStatusForm(instance=task)

    if request.method == 'POST':
        form = TaskStatusForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task', id=id)

    context = {
        'task': task,
        'taskcomments': taskcomments,
        'form':form,
        'id':id
    }

    return render(request, 'worklogapp/task.html', context)


def loginmessage(request):
    return render(request, 'worklogapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'worklogapp/logoutmessage.html')

@login_required
def newtask(request):
    if not request.user.is_authenticated:
        return redirect("/registation/login")

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

@login_required
def newcomment(request, id):
    if not request.user.is_authenticated:
        return redirect("/registation/login")


    taskinstance = get_object_or_404(Task, pk=id)

    if request.method=='POST':
        form=TaskCommentForm(request.POST)
        if form.is_valid():
            form.instance.taskUserCreated = request.user
            form.instance.taskid=taskinstance
            form.save()
            return redirect('task', id=id)
    else:
        form=TaskCommentForm()
    return render(request, 'worklogapp/newcomment.html', {'form': form})    

# def updateStatus(request, id):

#     ttask = Task.objects.get(id=id)
#     form = TaskForm(instance=ttask)

#     if request.method == 'POST':
#         form = TaskForm(request.Post,instance=ttask)
#         if form.isvalid():
#             form.save()
#             return redirect('task', id=id)

#     context = {'form':form}
#     return render(request, 'worklogapp/task.html', context)

# def testtask (request, id):
#     ttask = Task.objects.get(id=id)
#     taskcomments = TaskComment.objects.filter(taskid=ttask.id)
#     form = TaskStatusForm(instance=ttask)

#     if request.method == 'POST':
#         form = TaskStatusForm(request.POST, instance=ttask)
#         if form.is_valid():
#             form.save()
#             return redirect('testtask', id=id)

#     context = {
#         'task': ttask,
#         'taskcomments': taskcomments,
#         'form':form,
#         'id':id
#     }

#     return render(request, 'worklogapp/testtask.html', context)
