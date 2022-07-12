from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

## import todo form and models

from .forms import TodoForm
from .models import Todo

@login_required(login_url='acces')
def index(request):

	item_list = Todo.objects.order_by("-date")
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('todo')
	form = TodoForm()

	page = {
			"forms" : form,
			"list" : item_list,
			"title" : "TODO LIST",
		}
	return render(request, 'todo/index.html', page)


#def remove(request, item_id):
#	item = Todo.objects.get(id=item_id)
#	item.delete()
#	messages.info(request, "item removed !!!")
#	return redirect('todo')

def remove(request, item_id):
	item = Todo.objects.get(id=item_id)
	if request.method == "POST":
		item.delete()
		return redirect('todo')
	return render(request,'todo/index.html')