from django.shortcuts import render,redirect
from django.contrib import messages
from models import *
import bcrypt

# Create your views here.
def index(request):
    if 'current_user' not in request.session:
        request.session['current_user'] = 0
    return render(request, "temp/index.html")

def register(request):
    errors = user.objects.registration_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            print errors.iteritems()
        return redirect('/')
    else:
        print request.POST['first_name']
        password = request.POST['password']
        pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt(8))
        user.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'],password=pwd)
        user_email = request.POST['email']
        request.session['current_user'] = request.POST['email']
        query = user.objects.get(email=user_email)
        print query
        return redirect('/success')


def signIn(request):
    errors = user.objects.login_validator(request.POST)
    if len(errors):
        print errors
        for tag, error in errors.iteritems():
            print errors.iteritems()
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        user_email = request.POST['email']
        password = request.POST['password']
        query = user.objects.get(email=user_email)
        print query.id
        pwd = bcrypt.hashpw(password.encode(), query.password.encode())
        #checks password
        if pwd == query.password:
            request.session['current_user'] = request.POST['email']
            return redirect("/success")
        else:
            messages.error(request, 'Invalid email or password')
    return redirect("/")

def success(request):
    context = {
        "user": user.objects.get(email=request.session['current_user'])
    }
    print user
    return render(request, 'temp/success.html', context)

def signOut(request):
    request.session.clear()
    return redirect('/')
