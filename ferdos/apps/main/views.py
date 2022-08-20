from django.shortcuts import render
from django.conf import settings
from .models import user
from django.views.generic.edit import CreateView
from django.urls import reverse
# Create your views here.
def media_admin(request):
    return {'media_url':settings.MEDIA_URL}

def index(request):
    return render(request,'main/index.html')

class usercreate(CreateView):
    model=user
    fields='__all__'
    template_name= 'main/user.html'
    def get_success_url(self) :
        return reverse('index')
    
