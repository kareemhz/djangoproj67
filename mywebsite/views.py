from django.shortcuts import render
from django.http import HttpResponse
from .models import Reg
def logininput(request):
    return render(request,"login.html")
def reginput(request):
    return render(request,"reg.html")
def login(request):
    un1=request.POST['un']
    pw1=request.POST['pw']
    dbuser = Reg.objects.filter(userid=un1, password=pw1)
    if not dbuser:
        return HttpResponse('login faild')
    else:
        return HttpResponse('login success')
def reg(request):
    t1=request.POST['userid']
    t2=request.POST['passid']
    t3=request.POST['username']
    t4=request.POST['address']
    t5=request.POST['country']
    t6=request.POST['zip']
    t7=request.POST['email']
    t8=request.POST['sex']
    t9=request.POST['en']
    t10=request.POST['nonen']
    t11=request.POST['desc']
    r1=Reg(userid=t1,password=t2,username=t3,address=t4,country=t5,pincode=t6,email=t7,sex=t8,en=t9,nonen=t10,about=t11)
    r1.save()
    return HttpResponse("reg success")