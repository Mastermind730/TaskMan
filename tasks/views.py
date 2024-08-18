# tasks/views.py

from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserSignupForm, TaskForm
from .models import Task, Activity
from django.contrib.auth import logout

def signup(request):
    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserSignupForm()
    return render(request, 'signup.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def task_list(request):
    sort_by = request.GET.get('sort_by', 'name')  # Default sort by 'name'
    order = request.GET.get('order', 'asc')

    if order == 'desc':
        sort_by = f'-{sort_by}'

    tasks = Task.objects.all().order_by(sort_by)
    
    context = {
        'tasks': tasks,
        'current_sort': sort_by.lstrip('-'),
        'current_order': order,
    }
    return render(request, 'task_list.html', context)
@login_required
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            Activity.objects.create(user=request.user, action=f'You added task "{task.name}"')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

@login_required
def mark_task(request, task_id, completed):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = completed
    task.save()
    action = "completed" if completed else "marked incomplete"
    Activity.objects.create(user=request.user, action=f'You {action} task "{task.name}"')
    return redirect('task_list')

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task_name = task.name
    task.delete()
    Activity.objects.create(user=request.user, action=f'You deleted task "{task_name}"')
    return redirect('task_list')

@login_required
def activity_feed(request):
    activities = Activity.objects.filter(user=request.user).order_by('-timestamp')
    return render(request, 'activity_feed.html', {'activities': activities})
