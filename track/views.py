from django.shortcuts import render
from django.http import HttpResponse
from .models import Tracker


TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)


def results(request):
    query=None
    post=[]
    if request.method == 'GET':
        query = request.GET.get('search')
        post = Tracker.objects.filter(trackingcode=query)
        return render(request,  'track/results.html', {'query':query,'post':post})
    else:
        return render(request, 'track/results.html',{})

        
def track(request):
    return render(request, "track/track.html")