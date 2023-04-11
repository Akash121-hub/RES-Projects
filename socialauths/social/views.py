from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
# Create your views here.



def user_login(request):
    request.session.set_test_cookie()
    print("cookie worked")
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user =  authenticate(request, username=cd['username'], password=cd['password'] )

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse(" Successfully Logged In ")
                return HttpResponse("Your Account is Disabled")
            return HttpResponse("Invalid Login")
    else:
        form = LoginForm()
    return render(request, 'social/login.html', {'form':form})