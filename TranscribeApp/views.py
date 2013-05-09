from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext

def hello(request):
	return HttpResponse("Hello world")

def root(request):
	t = get_template('root.html')
	c = RequestContext(request, {
    'next':'/'
		})
	html = t.render(c)
	return HttpResponse(html)

def test(request):
	t = get_template('test_root.html')
	c = RequestContext(request, {
		'username':'Hareesh'
		})
	html = t.render(c)
	return HttpResponse(html)



def accounts(request):
	t = get_template('accounts.html')
	html = t.render(c)
	return HttpResponse(html)
