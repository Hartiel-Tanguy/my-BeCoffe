from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from compte.models import users

## import todo form and models

from .forms import TodoForm
from .models import Todo

@login_required(login_url='acces')
def index(request):

	item_list = Todo.objects.order_by("-date")
	if request.method == "POST":
		form = TodoForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data['user']
			if user == request.user:
				form.save()
				messages.success(request, "bonne chance a toi ")
			else: 
				messages.error(request,"dommage bien esseyé")
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
	is_user = request.user == item.user
	if is_user or request.user.chef:
		if request.method == "POST":
			item.delete()
			return redirect('todo')
	else:
		messages.error(request,"on ne touche pas a se qui n'est pas a soi")
		return redirect('todo')
	return render(request,'todo/index.html')