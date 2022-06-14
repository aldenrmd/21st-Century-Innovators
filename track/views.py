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
    min_code = 'DAQS00000001'
    max_code = 'DAQS99999999'
    last_entry = Tracker.objects.last().trackingcode
    print(type(last_entry))
    if last_entry is None or last_entry in max_code:
        return min_code
    serial_number = int(last_entry[4:]) + 1
    return f"DAQS{serial_number:08d}"