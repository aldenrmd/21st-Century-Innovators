from django.shortcuts import render
from django.http import HttpResponse
import datetime
import mysql.connector as sql
em = '' 
pwd = ''
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def login(request):
    global em, pwd
    if request.method == 'POST':  
        m=sql.connect(host="localhost",user="root",passwd="bundat castano2001",database="daqsDB")
        cursor = m.cursor()
        d = request.POST 
        for key,value in d.items():
            if key == "username":
                user = value
            if key == "password":
                pwd = value
        c = "select * from admin_access_credential where username='{}' and password='{}'".format(user,pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        print(t)
        if t == ():
            return render(request,"admin_access/admin.html")
        else: 
            return render(request, "admin_access/dashboard.html")
    return render(request, "admin_access/admin.html")

def dashboard(request):
    return render(request, "admin_access/dashboard.html")