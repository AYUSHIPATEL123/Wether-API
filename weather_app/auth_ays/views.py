from django.shortcuts import render,redirect
from .forms import UserForm,LoginForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView,FormView
from django.contrib.auth import authenticate,login,logout

# Create your views here.

class Register(CreateView):
    form_class = UserForm
    template_name = 'register.html'
    success_url = reverse_lazy('weather')


class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('weather')

    def post(self,request,*args,**kwargs):
        
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(email=email,password=password)

        if user:
            login(request,user)
            messages.success(request,"you have loged in successfuly...")
            return redirect(self.success_url)
        else:
            messages.error(request,"login creadential are wrong...")
            return self.get(request,*args,**kwargs)

def logout_view(request):
    logout(request)
    messages.success(request,"logout successfuly...")
    return redirect('login')
