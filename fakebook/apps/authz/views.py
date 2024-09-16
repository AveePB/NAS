from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect

# Create your views here.
class RegisterPage(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        if (not request.user.is_anonymous):
            return redirect('home-page')
        
        return render(request, 'auth/register.html')
    
class LoginPage(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        if (not request.user.is_anonymous):
            return redirect('home-page')
        
        return render(request, 'auth/login.html')