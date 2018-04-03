from django.shortcuts import render
from django.template.context_processors import csrf
from .models import Newspapers
from .forms import NewspaperForms

# Create your views here.

def paper_entry(request):
	context= {'nbar' : 'account',}
	if request.method == "GET":
		form = Newspaperforms(request.POST or None)
	else:
		form = Newspaperforms(request.POST or None)
		instance = form.save(commit=False)
		instance.save()
	context.update(csrf(request))
	return render(request,"paper entry.html",context)

def all_newspapers(request):
	context={}
	queryset=Newspapers.objects.all()
	context={
		"set":queryset,
	}
	context.update(csrf(request))
	return render(request,"all_newspapers.html",context)
