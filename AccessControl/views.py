from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django.http  import HttpResponse
from django.contrib.auth import login, logout,authenticate
from django.db import IntegrityError
#from AccessControl.forms import SignUpForm
# Create your views here.

def signupPage(request):
    
    if request.method == 'GET':
        print('enviando formulario')
        
        title = 'hello World'
        return render(request, 'signup.html', 
            {
            'mytitle': title , 
            'form_class':UserCreationForm
            }
        )
    else:
        print(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            # register user
            print('obteniendo datos', request.POST)

            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'],is_active=request.POST['is_active']) 
                user.save(),
                login(request, user)
                return redirect('home')
                #return HttpResponse('user create successfully')   

            except IntegrityError:
                return render(request, 'signup.html', 
                    {
                    'error': 'Username already exists' , 
                    'form':UserCreationForm
                    })   

            
        else:
            return render(request, 'signup.html', 
            {
            'error': 'password does not match' , 
            'form':UserCreationForm
            })  

        
    

    
    
def home(request):
    
    Author = 'Milano'
    grupo = 'Grupo Scout Baden Powell'
    return render(request, 'home.html', 
        {
        'grupo': grupo , 
        }
    )
    
    
    
def signout(request):
    logout(request)
    return redirect('home')



def signin(request):
    
    if request.method == 'GET':
            return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    #print(user)
    if user is None:
        return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Username or password is incorrect."})

    login(request, user)
    return redirect('home')
    
    
