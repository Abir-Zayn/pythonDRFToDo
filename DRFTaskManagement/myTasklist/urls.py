from django.contrib import admin
from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

# Create a router and register the viewsets.

urlpatterns = [
    path('', homepage, name='homepage'),
    path('login/',loginPage, name='loginPage'),
    path('signup/',signupPage, name='signupPage'),
    # path('<int:pk>/', DetailTodo.as_view()),
    # path('api/', ListTodo.as_view()),
    # path('create', CreateTodo.as_view(), name="createTask"),
    # path('delete/<int:pk>', DeleteTodo.as_view())
   
    # path('api/tasks/<int:pk>/', createTodo.as_view(), name='createTodo'),
]
