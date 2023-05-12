from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='HomePage'),
    path('about/', views.About, name='AboutPage'),
    path('solutions/', views.Solutions, name='SolutionsPage'),
    path('products/', views.Products, name='ProductsPage'),
    path('groups/', views.Groups, name='GroupsPage'),
    path('Reminders/', views.Reminders, name='RemindersPage'),
    path('login/', views.Login, name='LoginPage'),
    path('register/', views.Register, name='RegisterPage'),
    

]