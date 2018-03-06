from django.shortcuts import render

def main(request):
	context = {'item' : ' MainApp Index'}
	return render(request, 'mainapp/index.html', context)

def tutorial(request):
	context = {'item' : ' MainApp Tutorial'}
	return render(request, 'mainapp/tutorial.html', context)

def contacts(request):
	context = {'item' : ' MainApp Contacts'}
	return render(request, 'mainapp/contacts.html', context)