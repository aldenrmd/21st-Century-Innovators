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
    return render(request, "track.html")
def pricing(request):
    return render(request, "pricing.html")
def about(request):
    return render(request, "about.html")
def contactus(request):
    return render(request, "contactus.html")
def admin(request):
    return render(request, "admin.html")
