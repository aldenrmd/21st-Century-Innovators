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
        m=sql.connect(host="localhost",user="root",passwd="thegoldenchild",database="daqsDB")
        cursor = m.cursor()
        d = request.POST 
        for key,value in d.items():
            if key=="username":
                em=value
            if key=="password":
                pwd=value
        c = "select * from admin where Email='{}' and Password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,"admin_access/admin.html")
        else: 
            return render(request, "admin_access/dashboard.html")
    return render(request, "admin_access/admin.html")

def dashboard(request):
    return render(request, "admin_access/dashboard.html")