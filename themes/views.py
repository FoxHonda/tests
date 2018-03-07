from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import models


def details(request,pk):
	theme = models.Themes.objects.get(id=pk)
	paginator = Paginator(theme.post_set.all(), 12)
	page = request.GET.get('page')

	try:
		collection = paginator.get_page(page)
	except PageNotAnInteger:
		collection = paginator.get_page(1)
	except EmptyPage:
		collection = paginator.get_page(paginator.num_pages)

	collection = paginator.get_page(page)
	context = {'collection' : collection}

	return render(request, 'posts/index.html', context)