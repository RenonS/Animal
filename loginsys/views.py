from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.template.context_processors import csrf
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден!"
            return render(request,'index.html', args)
    else:
        return render(request,'index.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    data = {}
    if request.method == "POST":
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser_form.save()
            newuser = auth.authenticate(username = newuser_form.cleaned_data['username'], password = newuser_form.cleaned_data['password2'])
            auth.login(request, newuser)
        else:
            data['form'] = newuser_form
    return render(request, 'index.html', context=data)


def profile(request, user_id):
    data = {"user": User.objects.get(pk=user_id)}
    try:
        return render(request, 'profile.html', context=data)
    except User.DoesNotExist:
        return None
