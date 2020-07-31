from django.shortcuts import render
from django.conf import settings
# Create your views here.
def index(request):

    context={
        'name':settings.DATA['name'],
        'about_me':settings.DATA['about_me']
    }
    return render(request,'main/index.html',context)
def projects(request):
    context={}
    return render(request,'main/projects.html',context)
def language(request):
    context={
        'languages':settings.DATA['languages']
    }
    return render(request,'main/language.html',context)