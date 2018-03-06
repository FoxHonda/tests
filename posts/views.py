from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from . import models

def index(request):
	posts = models.Post.objects.all()
	paginator = Paginator(posts, 12)
	page = request.GET.get('page')
	try:
		collection = paginator.get_page(page)	
	except PageNotAnInteger:
		collection = paginator.get_page(1)
	except EmptyPage:
		collection = paginator.get_page(paginator.num_pages)

	collection = paginator.get_page(page)
	context = {'collection':collection}

	return render(request, 'posts/index.html', context)

def details(request, pk):
	posts = models.Post.objects.get(id=pk)
	related_posts = models.Post.objects.filter(theme=posts.theme).exclude(id=posts.id)[:3]
	context = {'item' : posts, 'related':related_posts}
	return render(request, 'posts/details.html', context)
