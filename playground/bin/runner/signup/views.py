from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import auth
from django.contrib.auth import login, authenticate,logout
from django.core.context_processors import csrf
from django.db import models
from django.shortcuts import render, redirect, RequestContext,HttpResponseRedirect,HttpResponse,render_to_response


# Create your views here.
from .forms import UserForm, RegisterForm


def home(request):

    register_data = request.POST if request.POST else None
    register_form = RegisterForm(register_data)
    to_list=[request.POST.get('email', '')]
    if request.method == 'POST':
        if register_form.is_valid():
            register_form.save()
            subject='Thanks for registration'
            message='Welcome to our site. Hope you will get in shape with us!'
            from_email=settings.EMAIL_HOST_USER
            #to_list=[register_form.email]
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            messages.success(request, 'Thank you for joining !')
            register_form = RegisterForm()
            return HttpResponse("<a href=\"/login/\"><span class=\"glyphicon glyphicon-user\"></span> Login!</a>")

    return render(request, "signup.html", locals())



def login(request):
    login_data = request.POST if request.POST else None
    login_form = UserForm(login_data)

    if request.method == 'POST':
        username=request.POST.get('username', '')
        password=request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        login_form = UserForm( )
        if user is not None:
            auth.login(request, user)
            #return HttpResponseRedirect('/profile/')
            return render_to_response('profile.html',
                          RequestContext(request,
                                         {'username':username, }))
        else:
            return HttpResponse('<h1>401: Unauthorized</h1>Wrong username or password!', status=401)

    return render(request, "login.html", locals())


def profile(request):
    username = request.user.username
    if request.user.is_authenticated():
        pass
    else:
        messages.error(request, 'Please sign in!')
    return render_to_response('profile.html',
                          RequestContext(request,
                                         {'username':username, }))

def err_log(request):
    return HttpResponse('<h1>401: Something went terribly wrong!', status=401)


def logout(request):
    auth.logout(request)
    return render(request, "home.html", locals())





