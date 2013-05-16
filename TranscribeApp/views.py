from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
from TranscribeApp.models import Note, Video
import datetime

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
  notetext = request.POST["text"]
  video_url = Video(url = request.POST["video_url"])
  c = RequestContext(request, {'content': notetext, 'video_url': video_url})
  t = get_template('notes.html')
  
  note = Note(video=video_url, date_created=datetime.datetime.now(), text=notetext)
  note.save()
  note.user.add(User.objects.get(username__exact=request.user))
  
  html = t.render(c)
  return HttpResponse(html)
