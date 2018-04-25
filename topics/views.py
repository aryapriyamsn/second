from django.shortcuts import render
from genres.models import Genres
from .models import Topics
# Create your views here.

def show_topics(request,name):
	#import ipdb; ipdb.set_trace()
	context={}
	genre=name
	all_topics=Topics.objects.all()
	genre_headlines=[]
	all_genres=Genres.objects.all()
	name=Genres.objects.get(name=genre)
	if Topics.objects.filter(genre=name).exists():
		for item in all_topics:
			if item.genre == name:
				genre_headlines.append(item)
		context={
			'genre':genre,
			'name':name,
			'all_genres':all_genres,
			'topics':genre_headlines,
			'headlines':all_topics,
			'user':request.user.username,
		}
	else:
		context={
			'genre':name,
			'all_genres':all_genres,
			'user':request.user.username,
		}
	return render(request,'digest-genre.html',context)

def show_all(request):
	context={}
	all_topics=Topics.objects.all()
	all_genres=Genres.objects.all()
	context={
		'all_genres':all_genres,
		'headlines':all_topics,
		'user':request.user.username,
	}
	
	return render(request,'home_digest.html',context)
