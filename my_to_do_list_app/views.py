from django.shortcuts import render, redirect
from my_to_do_list_app.models import ToDoList
from my_to_do_list_app.forms import ToDoListForm


def to_do_list_view(request):
    to_do_form = ToDoListForm()
    return render(request, 'user_interface/to-do-list.html', {'form':to_do_form})