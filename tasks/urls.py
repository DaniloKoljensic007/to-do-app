from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add_task, name="add"),
    path("<int:task_id>/update", views.update_task, name="update"),
    path("<int:task_id>/delete", views.delete_task, name="delete"),
]
