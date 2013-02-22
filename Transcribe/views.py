from django.http import HttpResponse

def hello(request):
	return HttpResponse("Hello world")

def root(request):
	return HttpResponse("home")