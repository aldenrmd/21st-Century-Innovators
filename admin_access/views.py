from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def login(request):
    return render(request, "admin_access/admin.html")

def dashboard(request):
    return render(request, "admin_access/dashboard.html")