from django.shortcuts import render,redirect
from .models import Todolist
from .forms import TodoListForm
from django.views.decorators.http import require_POST
# Create your views here.
def index(request):
    todo_items=Todolist.objects.order_by('id')
    context={'todo_items':todo_items}
    return render(request, 'todolist/index.html', context)
@require_POST
def addTodoItem(request):
    form=TodoListForm(request.POST)
    if form.is_valid():
        new_todo=Todolist(text=request.POST['text'])
        new_todo.save()
    return redirect('index')

def completeTodo(request,todo_id):
    todo=Todolist.objects.get(pk=todo_id)
    todo.completed=True
    todo.save_base()
    return redirect("index")

def deleteCompleted(request):
    Todolist.objects.filter(completed=True).delete()  # Corrected the filtering condition
    return redirect('index')

def deleteall(request):
    Todolist.objects.all().delete()
    return redirect('index')
