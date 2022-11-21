from django.shortcuts import render

def Index(request):
    return render(request, 'principal/index.html')

def Nosotros(request):
    return render(request, 'principal/nosotros.html')