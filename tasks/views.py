from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

# Create your views here.


def index(request):

    tasks = Task.objects.all().order_by("-created_at")

    return render(request, "index.html", {"tasks": tasks})


def add_task(request):
    title = request.POST["title"]
    Task.objects.create(title=title)

    return redirect("index")


def update_task(request, task_id):

    task = get_object_or_404(Task, pk=task_id)
    task.is_completed = not task.is_completed
    task.save()

    return redirect("index")


def delete_task(request, task_id):

    task = get_object_or_404(Task, pk=task_id)
    task.delete()

    return redirect("index")
