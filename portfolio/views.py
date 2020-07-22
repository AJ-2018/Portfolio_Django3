from django.shortcuts import render

#importing model Project for accessing its db
from .models import Project

# Create your views here.
def home(request):
    projects = Project.objects.all() #this grabs all the objects from the db in Project
    return render(request, 'portfolio/home.html', {'projects': projects})

