from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext

def hello(request):
	return HttpResponse("Hello world")

def root(request):
	t = get_template('root.html')
	c = RequestContext(request, {
    'next':'/transcribe/'
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
  c = RequestContext(request, {
                               'username':'Hareesh'
                               })
  html = t.render(c)
  return HttpResponse(html)


def save(request):
  text = request.POST["notetext"]
  video_url = request.POST["video_url"]
  c = RequestContext(request, {'content': text, 'video_url': video_url})
  t = get_template('notes.html')
  
  html = t.render(c)
  return HttpResponse(html)
