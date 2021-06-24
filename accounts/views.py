from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.
def index(request):
    return render(request,'accounts/index.html')

def signupPage(request):
    return render(request,'accounts/signup.html')

def signinPage(request):
    return render(request,'accounts/signin.html')

def userHome(request):
    return render(request,'accounts/userhome.html')

def signUp(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        unm = request.POST['uname'] #rs123
        pwd = request.POST['pwd']
        try :
            user = User.objects.get(username=unm)
            return render(request,'accounts/signup.html',{'error' : "User name already exists."})
        except:
             user = User.objects.create_user(first_name=fname,last_name=lname,email=email,username=unm,password=pwd)
             user.save()
             return render(request,'accounts/signup.html',{'msg':"User Registered Successfully..!!!"})
    else:
        return render(request,'accounts/signup.html',{'error' : "Invalid User Request."})


def signIn(request):
    if request.method == "POST":
        unm = request.POST['uname']#abc123
        pwd = request.POST['pwd']#123456
        user = auth.authenticate(username=unm,password=pwd)
        if user is not None:
            auth.login(request,user)
            return render(request,'accounts/userhome.html')
        else:
            return render(request,'accounts/signin.html',{'error' : "Invalid Credentials."})
    else:
        return render(request,'accounts/signin.html',{'error' : "Invalid User Request."})

def signOut(request):
    auth.logout(request)
    return render(request,'accounts/signin.html',{'msg':"Logged out successfully...!!!"})