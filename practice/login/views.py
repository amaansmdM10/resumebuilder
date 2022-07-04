from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Log
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage
from django.views import View
import csv
import os
from django.views.generic import View
from django.forms.models import model_to_dict


# Create your views here.

def index(request):
    return render(request, 'index.html')


def signupPage(request):

    if request.method == "POST":
        uname=request.POST.get("Username")
        email=request.POST.get("Emailid")
        pass1=request.POST.get("Password")
        pass2=request.POST.get("confirmPassword")

        if pass1 != pass2:
            messages.error(request, "Password doesn't match!")
            return redirect('/signup')

        try:
            if User.objects.get(username = uname):
                messages.warning(request, "Username is already taken!")
                return redirect('/signup')

        except Exception as identifier:
            pass

        try:
            if User.objects.get(email = email):
                messages.warning(request, "Email ID is already registered!")
                return redirect('/signup')

        except Exception as identifier:
            pass

        myuser = User.objects.create_user(uname, email, pass1)
        myuser.save()

        messages.success(request, "SignUp Successful!")
        return redirect('/login')

    return render(request, 'signup.html')

def loginPage(request):

    if request.method == "POST":
        uname=request.POST.get("Username")
        password=request.POST.get("Password")

        myuser = authenticate(username=uname, password=password)

        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login Successful!")
            return redirect('/')

        else:
            messages.error(request, "Invalid Credentials!")
            return redirect('/login')

    return render(request, 'login.html')
    

def addResume(request):
    if request.method == "POST":
        userid=request.POST['userid']
        start=request.POST['fname']
        end=request.POST['lname']
        pnoneno=request.POST['number']
        mails=request.POST['mails']
        github=request.POST['github']
        linkedln=request.POST['linkedln']
        school=request.POST['secondary']
        sdate=request.POST['sdate']
        intermediate=request.POST['intermediate']
        interdate1=request.POST['interstart']
        interdate2=request.POST['interend']
        degree=request.POST['degree']
        ds=request.POST['specialization']
        dstart=request.POST['dstart']
        dend=request.POST['dend']
        s11=request.POST['s11']
        s2=request.POST['s2']
        s3=request.POST['s3']
        s4=request.POST['s4']
        h1=request.POST['h1']
        h2=request.POST['h2']
        h3=request.POST['h3']
        h4=request.POST['h4']
        p1=request.POST['p1']
        p2=request.POST['p2']
        p3=request.POST['p3']
        p1_desc=request.POST['p1_desc']
        p1sdate=request.POST['p1sdate']
        p1edate=request.POST['p1edate']
        p2_desc=request.POST['p2_desc']
        p2sdate=request.POST['p2sdate']
        p2edate=request.POST['p2edate']
        p3_desc=request.POST['p3_desc']
        p3sdate=request.POST['p3sdate']
        p3edate=request.POST['p3edate']
        i1=request.POST['i1']
        i2=request.POST['i2']
        i3=request.POST['i3']
        i1_desc=request.POST['i1_desc']
        i1sdate=request.POST['i1sdate']
        i1edate=request.POST['i1edate']
        i2_desc=request.POST['i2_desc']
        i2sdate=request.POST['i2sdate']
        i2edate=request.POST['i2edate']
        i3_desc=request.POST['i3_desc']
        i3sdate=request.POST['i3sdate']
        i3edate=request.POST['i3edate']
        c1=request.POST['c1']
        c2=request.POST['c2']
        c3=request.POST['c3']
        c1_desc=request.POST['c1_desc']
        c2_desc=request.POST['c2_desc']
        c3_desc=request.POST['c3_desc']
        img=request.POST['img']
        data=Log(userid=userid,firstname=start,lastname=end,mail=mails,phoneno=pnoneno,s1=school,c1=c1,c2=c2,c3=c3,c1_desc=c1_desc,c2_desc=c2_desc,c3_desc=c3_desc,s1_date=sdate,inter1=intermediate,inter1_start=interdate1,inter1_end=interdate2,degree=degree,degree_Specialization=ds,degree_start=dstart,degree_end=dend,skills1=s11,skills2=s2,skills3=s3,skills4=s4,hobbies1=h1,hobbies2=h2,hobbies3=h3,hobbies4=h4,github=github,linkedln=linkedln,p1=p1,p2=p2,p3=p3,p1_desc=p1_desc,p2_desc=p2_desc,p3_desc=p3_desc,p1_startdate=p1sdate,p1_enddate=p1edate,p2_startdate=p2sdate,p2_enddate=p2edate,p3_startdate=p3sdate,p3_enddate=p3edate,i1=i1,i2=i2,i3=i3,i1_desc=i1_desc,i2_desc=i2_desc,i3_desc=i3_desc,i1_startdate=i1sdate,i1_enddate=i1edate,i2_startdate=i2sdate,i2_enddate=i2edate,i3_startdate=i3sdate,i3_enddate=i3edate,img=img)
        data.save()

        messages.success(request, "Your resume has been successfully added!")
        return redirect('/addResume')

    return render(request, 'addResume.html')   


def viewResume(request, id):
    data1 = Log.objects.get(pk=id)
    return render(request, "viewResume.html", {'data1':data1})


def listResume(request):
    current_user = request.user.username
    userid = Log.userid

    if Log.objects.filter(userid = current_user).exists():
        profile=Log.objects.filter(userid = current_user)
        return render(request, "listResume.html", {'profile':profile})
        
    return render(request, "listResume.html")


def logoutPage(request):
    logout(request)
    messages.success(request, 'Logout Successful!')
    return redirect('/login')