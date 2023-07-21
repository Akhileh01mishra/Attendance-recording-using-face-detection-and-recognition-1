from django.shortcuts import render,HttpResponse
from . import registerStudent
from . import recognition
from . import spreadsheet
# Create your views here.
def index(request):
    return render(request,'login.html')

def admin(request):
    return render(request,'admin_dashboard.html')
def validate(request):
    name=request.GET.get("username","default")
    password=request.GET.get("password","default")
    if name=="Admin" and password=="1234":
        # return HttpResponse(name+" "+password)
        return render(request,'admin_dashboard.html')
    else:
        params={'flag':'1'}
        return render(request,'login.html',params)

def register(request):
    name=request.GET.get("name","default")
    email=request.GET.get("email","default")
    roll=request.GET.get("rollno","default")
    if name!="default" and email!="default" and roll !="default":
        flag=registerStudent.enroll_via_camera(name,email,roll)
        params={"flag":flag}
        
        return render(request,"register.html",params)
    return render(request,"register.html")

def attendance(request):
    recognition.run_recognition()
    params={'flag':'1'}
    return render(request,"admin_dashboard.html",params)

def allAbsent(request):
    spreadsheet.mark_all_absent()
    params={'flag1':'1'}
    return render(request,"admin_dashboard.html",params)