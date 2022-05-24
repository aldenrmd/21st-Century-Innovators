from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def index(request):
    today = datetime.datetime.now().date()
    return render(request, "home/index.html", {"today": today})
def pricing(request):
    return render(request, "home/pricing.html")
def about(request):
    return render(request, "home/about.html")
def contactus(request):
    return render(request, "home/contactus.html")
