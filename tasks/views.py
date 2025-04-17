from django.shortcuts import render, redirect
from .models import Task

# Create your views here.


def index(request):

    tasks = Task.objects.all().order_by("-created_at")

    return render(request, "index.html", {"tasks": tasks})


def add_task(request):
    title = request.POST["title"]
    Task.objects.create(title=title)

    return redirect("index")
