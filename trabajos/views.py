from django.shortcuts import render

def Mensura(request):
    return render(request, 'trabajos/mensura.html')

def Estadoparcelario(request):
    return render(request, 'trabajos/estado_parcelario.html')

def Relevamiento(request):
    return render(request, 'trabajos/relevamiento.html')

def Amojonamiento(request):
    return render(request, 'trabajos/amojonamiento.html')

def Replanteo(request):
    return render(request, 'trabajos/replanteo.html')

def PropiedadHorizontal(request):
    return render(request, 'trabajos/propiedad_horizontal.html')

def Unificacion(request):
    return render(request, 'trabajos/unificacion.html')

def Loteo(request):
    return render(request, 'trabajos/loteo.html')

def Usucapion(request):
    return render(request, 'trabajos/usucapion.html')

def BarrioCerradoClub(request):
    return render(request, 'trabajos/barrio_cerrado_club.html')