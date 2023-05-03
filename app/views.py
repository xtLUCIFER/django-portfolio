from django.shortcuts import render
from django.core.cache import cache
from .models import Info, Projects

def index(request):
   
    
    # If no cached result exists, get the data and render the template
    data = Info.objects.all()
    all_projects = Projects.objects.all()
    context = {
        'data': data,
        'projects': all_projects
    }
    return render(request, 'index.html', context)