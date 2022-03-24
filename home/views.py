from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def index(request):
    today = datetime.datetime.now().date()
    return render(request, "index.html", {"today": today})
def track(request):
    today = datetime.datetime.now().date()
    return render(request, "track.html", {"today": today})
def pricing(request):
    today = datetime.datetime.now().date()
    return render(request, "pricing.html", {"today": today})
def about(request):
    today = datetime.datetime.now().date()
    return render(request, "about.html", {"today": today})
def contactus(request):
    today = datetime.datetime.now().date()
    return render(request, "contactus.html", {"today": today})
def admin(request):
    today = datetime.datetime.now().date()
    return render(request, "admin.html", {"today": today})