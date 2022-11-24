from django.shortcuts import render

def Trabajos(request):
    return render(request, 'trabajos/trabajos.html')