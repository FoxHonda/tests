from django.shortcuts import render
from . import models

def index(request):
	posts = models.Post.objects.all()
	context = {'collection' : posts}
	return render(request, 'posts/index.html', context)

def details(request, pk):
	posts = models.Post.objects.get(id=pk)
	related_posts = models.Post.objects.filter(theme=posts.theme).exclude(id=posts.id)[:3]
	context = {'item' : posts, 'related':related_posts}
	return render(request, 'posts/details.html', context)
