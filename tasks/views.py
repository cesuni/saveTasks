from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User  
from django.contrib.auth import login, logout

# Create your views here.


def home(request):
    return render(request, 'home.html') 

def tasks(request):
    return render(request, 'tasks.html')


# register user
def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
        'form': UserCreationForm 
    })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # usuario
                login(request, user)
                return redirect('tasks')
            except:
                # return HttpResponse('el usuario ya existe')
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error' : 'usario ya existe' 
                })
        # return HttpResponse('passwords no coinciden')
        return render(request, 'signup.html', {
            'form': UserCreationForm, 
            'error': 'passwords no coinciden'
    })

# logout
def endsession(request):
    logout(request)
    return redirect('home')

   

   
