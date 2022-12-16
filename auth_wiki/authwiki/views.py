from .models import *
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response({
                "Message": "Your account has been successful created",
                "User": serializer.data}, status=status.HTTP_201_CREATED
            )

        return Response({"error": serializer._errors}, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return render(request, 'authwiki/home.html')

def community(request):
    return render(request, 'authwiki/community.html')

def contact_us(request):
    return render(request, 'authwiki/contact_us.html')

def post(request):
    return render(request, 'authwiki/post.html')

def landing(request):
    return render(request, 'authwiki/landing.html')

def authenticated(request):
    return render(request, 'authwiki/authenticated.html')

def unauthenticated(request):
    return render(request, 'authwiki/unauthenticated.html')

def error(request):
    return render(request, 'authwiki/error.html')

def error_land(request):
    return render(request, 'authwiki/errorland.html')

def individual(request):
    return render(request, 'authwiki/individual.html')

def registerPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'authwiki/register.html', {'form': form})

def loginPage(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Login failed!'
    return render(request, 'authwiki/login.html', context={'form': form, 'message': message})

def search_error(request):
    return render(request, 'authwiki/search_error.html')