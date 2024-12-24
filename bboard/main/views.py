from django.contrib.auth import authenticate, login as auth_login
from django.db import IntegrityError
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.models import User


from .models import Userprofile
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        avatar = request.FILES.get('avatar')

        if User.objects.filter(username = username).exists():
            return render(request, 'register.html', {'error' : 'Takoi login est' })

        if User.objects.filter(email = email).exists():
            return render(request, 'register.html', {'error' : 'Takoi email est' })

        if password != password2:
            return render(request, 'register.html', {'error' : 'password ne podoshel' })

        try:

            user = User.objects.create_user(username = username, email = email, password = password, first_name = first_name)

            Userprofile.objects.create(user = user, avatar = avatar)
            return redirect('login')
        except IntegrityError:
            return render(request, 'register.html', {'error' : 'oshibka sozdania' })
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'user ne suhestvuet'})

    return render(request, 'login.html')

def home (request):
    if request.user.is_authenticated:
        try:
            user_profile = get_object_or_404(Userprofile, user=request.user)

        except Userprofile.DoesNotExist:
            user_profile = None

        return render(request, 'home.html', {'user_profile' : user_profile })


    return render(request, 'home.html')