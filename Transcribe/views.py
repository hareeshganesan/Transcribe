from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect

def redirect_to_home(request):
    return HttpResponseRedirect("/transcribe/")
  
def hello(request):
	return HttpResponse("Hello world")

def root(request):
	return HttpResponse("home")

def register(request):
  create_form = UserCreationForm()
  if request.method == 'GET' :
    t = get_template('registration/registration_form.html')
    c = RequestContext(request, {
        'next':'/transcribe/',
        'form':create_form,
        })
    html = t.render(c)
    return HttpResponse(html)
  if request.method == 'POST' :
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save() 
      return redirect_to_home(request)  
  request.method = 'GET'
  return register(request);
      