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


def track_code_generator():
    last_entry = Tracker.objects.last()
    if last_entry == None:
        return "DAQS00000001"
    tracking_code = last_entry.trackingcode
    serial_number = int(tracking_code[4:]) + 1
    return "DAQS" + str(("%08d"%serial_number))