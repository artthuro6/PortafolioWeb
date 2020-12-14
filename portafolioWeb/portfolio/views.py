from django.shortcuts import render
#Importando de la BD
from .models import Project

# Create your views here.

def portfolio(request):
    projects = Project.objects.all()
    #Pasando datos al template
    return render(request, 'portfolio/portafolio.html',{'projects': projects})

