from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import generics
from .models import task
from .serializers import taskserializer
from django.http import JsonResponse
from rest_framework.views import APIView

def homepage(request):
    return render(request, 'home.html')

def loginPage(request):
    # sourcery skip: remove-unnecessary-else, swap-if-else-branches
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user= authenticate(request, username=username, password = password)
        
        if user is not None:
            login(request, user)
            return render(request, 'loggedhome.html')
        else:
            return redirect('loginPage')        
    return render(request, 'login.html')

def signupPage(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        u_mail = request.POST.get('usermail')
        u_password = request.POST.get('password1')
        u_confirm_password = request.POST.get('password2')

        if u_password != u_confirm_password:
            return redirect('signupPage')
        else:
            my_user = User.objects.create_user(u_name, u_mail, u_password)
            my_user.save()
            return redirect('homepage')
    return render(request, 'signup.html')

# class ListTodo(generics.ListAPIView):
#     queryset = task.objects.all()
#     serializer_class = taskserializer
    
# class DetailTodo(generics.RetrieveUpdateAPIView):
#     queryset = task.objects.all()
#     serializer_class = taskserializer

# class CreateTodo(generics.CreateAPIView):
#     queryset = task.objects.all()
#     serializer_class = taskserializer
# class DeleteTodo(generics.DestroyAPIView):
#     queryset = task.objects.all()
#     serializer_class = taskserializer