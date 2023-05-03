from django.shortcuts import render
from django.core.cache import cache
from .models import Info, Projects

def index(request):
    # Try to get the cached result for this view
    cached_result = cache.get('index_view')
    if cached_result is not None:
        # If a cached result exists, return it
        return cached_result
        
    
    # If no cached result exists, get the data and render the template
    data = Info.objects.all()
    all_projects = Projects.objects.all()
    context = {
        'data': data,
        'projects': all_projects
    }
    # Cache the result for 1 week
    cache.set('index_view', render(request, 'index.html', context), 604800)
    return render(request, 'index.html', context)