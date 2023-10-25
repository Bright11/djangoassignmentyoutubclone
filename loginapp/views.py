from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from.forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.views import View

class register(View):
    def get(self,request):
        registerform=RegisterForm()
        loginform=LoginForm()
        constext={'registerform':registerform,"loginform":loginform}
        
        return render(request,"login.html",constext)

    def post(self,request):
         registerform=request.POST.get("registernow")
         loginuser=request.POST.get("loginnow")
         
         if registerform=="register":
             #print("register")
             register=RegisterForm(request.POST,request.FILES)
             if register.is_valid():
                 profile=register.save(commit=False)
                 profile.save()
                 if profile:
                     messages.success(request,"Success")
                     return redirect('loginapp:register')
                 else:
                     messages.success(request,"Error occured")
                     return redirect('loginapp:register')
             
            #  end of register
         elif loginuser=="login":
            #print("login")
            username=request.POST.get("username")
            password=request.POST.get("password")
            user=authenticate(request,username=username,password=password)
            if user is not None:
                 login(request,user)
                 messages.success(request,"login was succesful")
                 return redirect("youtubeapp:index")
            else:
                messages.success(request,"contact site admistrator")
                return redirect('loginapp:register')
               # pass
            #  login
            #  the end of login
         else:
            messages.success(request,"contact site admistrator")
            return redirect('loginapp:register')
             
             

# logout
def logoutuser(request):
    logout(request)
    return redirect("youtubeapp:index")
    
    
        
           

