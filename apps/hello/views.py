from django.shortcuts import render
from apps.hello.models import Info
from django.shortcuts import render_to_response
from apps.context_processors.context_processor import *
from django.template import RequestContext
from django.template import loader, Context



from django.contrib import messages


# Create your views here.
def show_info_all(request, id=1):
    allinfo = Info.objects.all()
    db = Info._meta.fields
    print db
    return render_to_response('info.html',{'allinfo': allinfo})

def show_info(request, id = "1"):
    return render_to_response('info.html',{'allinfo': Info.objects.filter(pk = id)}, context_instance=RequestContext(request))

def get_messages(request):
    infos = Info.objects.all()
    render_to_response('messages.html',{'message': infos} )

def settings(request):
    page_name = 'SETTINGS'
    return render_to_response('settings.html',{'page':page_name}, context_instance=RequestContext(request))