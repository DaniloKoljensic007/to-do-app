from django.shortcuts import render
from .models import Task

# Create your views here.


def index(request):

    tasks = Task.objects.all().order_by("-created_at")

    return render(request, "index.html", {"tasks": tasks})
