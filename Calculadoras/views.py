from django.shortcuts import render
from django.http import HttpResponse
from math import log10

# Create your views here.


def CalcuTMB(request):
    # Get Datos = Recibe los datos del Usuario
    sexo = str(request.POST["sexo"]) if "sexo" in request.POST else "M"
    edad = int(request.POST["edad"]) if "edad" in request.POST else 18
    peso = int(request.POST["peso"]) if "peso" in request.POST else 70
    altura = int(request.POST["altura"]) if "altura" in request.POST else 170
    actividad = float(request.POST["actividad"]) if "actividad" in request.POST else 1.2
    estado = bool(request.POST["estado"]) if "estado" in request.POST else "False"

    # TMB = Tasa Metabolica Basal
    TMB_M = (10 * peso) + (6.25 * altura) - (5 * edad) - 161
    TMB_H = (10 * peso) + (6.25 * altura) - (5 * edad) + 5

    # Factor Actividad + Calorias de mantenimiento
    acti_M = TMB_M * actividad
    acti_H = TMB_H * actividad

    # Calorias para adelgazar
    adelgazar_H = acti_H - 300
    adelgazar_M = acti_M - 300

    # Calorias para aumentar de peso
    aumentar_H = acti_H + 500
    aumentar_M = acti_M + 500

    return render(request, "Calculadoras/CalcuTMB.html", {"TMB_H": TMB_H, "TMB_M": TMB_M, "sexo": sexo, "acti_M": acti_M, "acti_H": acti_H, "adelgazar_H": adelgazar_H, "adelgazar_M": adelgazar_M, "aumentar_M": aumentar_M, "aumentar_H": aumentar_H, "estado": estado})


def CalcuIMC(request):
    # Get Datos = Recibe los datos del Usuario
    sexo = str(request.POST["sexo"]) if "sexo" in request.POST else "M"
    peso = int(request.POST["peso"]) if "peso" in request.POST else 70
    altura = int(request.POST["altura"]) if "altura" in request.POST else 170
    estado = bool(request.POST["estado"]) if "estado" in request.POST else "False"

    # IMC = Indice de Masa Corporal
    def calIMC(altura, peso):
        m = (altura / 100)
        float(m)
        IMC = (peso/(m * m))
        return IMC
    IMC = calIMC(altura, peso)
    
    return render(request, "Calculadoras/CalcuIMC.html", {"IMC": IMC, "sexo": sexo, "estado": estado})


def CalcuPGCM(request):
    # Get Datos = Recibe los datos del Usuario
    sexo = str(request.POST["sexo"]) if "sexo" in request.POST else "M"
    edad = int(request.POST["edad"]) if "edad" in request.POST else 18
    altura = int(request.POST["altura"]) if "altura" in request.POST else 170
    cuello = int(request.POST["cuello"]) if 'cuello' in request.POST else 45
    estado = bool(request.POST["estado"]) if "estado" in request.POST else False
    cintura = int(request.POST["cintura"]) if "cintura" in request.POST else 120
    cadera = int(request.POST["cadera"]) if "cadera" in request.POST else 105
    
    # PGC = Porcentaje de Grasa Corporal | Convertidor de Centimetros a Metros y los transforma a Float
    def convertidor(altura, cadera, cintura, cuello):
        altura = (altura / 100)
        float(altura)
        cadera = (cadera / 100)
        float(cadera)                   # Metros = cm / 100
        cintura = (cintura / 100)
        float(cintura)
        cuello = (cuello / 100)
        float(cuello)
        return altura, cadera, cintura, cuello

    PGC_Mujer = 495 / (1.29579 - 0.35004 * log10(cintura + cadera - cuello) + 0.22100 * log10(altura)) - 450
    

    return render(request, "Calculadoras/CalcuPGCM.html", {"sexo": sexo, "PGC_M": PGC_Mujer, "estado": estado, "edad": edad})

def CalCuPGCH(request):
    # Get Datos = Recibe los datos del Usuario
    sexo = str(request.POST["sexo"]) if "sexo" in request.POST else "M"
    edad = int(request.POST["edad"]) if "edad" in request.POST else 18
    altura = int(request.POST["altura"]) if "altura" in request.POST else 170
    cuello = int(request.POST["cuello"]) if 'cuello' in request.POST else 45
    estado = bool(request.POST["estado"]) if "estado" in request.POST else False
    cintura = int(request.POST["cintura"]) if "cintura" in request.POST else 120
    
    # Convertidor de Centimetros a Metros y los transforma a Float
    def convertidor(altura,cintura, cuello):
        altura = (altura / 100)
        float(altura)                  
        cintura = (cintura / 100)   
        float(cintura)              # Metros = cm / 100
        cuello = (cuello / 100)
        float(cuello)
        return altura, cintura, cuello

    # PGC = Porcentaje de Grasa Corporal
    PGC_Hombre = 495 / (1.0324 - 0.19077 * log10(cintura - cuello) + 0.15456 * log10(altura)) - 450

    return render(request, "Calculadoras/CalcuPGCH.html", {"sexo": sexo, "PGC_H": PGC_Hombre, "estado": estado, "edad": edad})

def CalcuMCM(request):
    # Get Datos = Recibe los datos del Usuario
    sexo = str(request.POST["sexo"]) if "sexo" in request.POST else "M"
    peso = int(request.POST["peso"]) if "peso" in request.POST else 70
    altura = int(request.POST["altura"]) if "altura" in request.POST else 170
    estado = bool(request.POST["estado"]) if "estado" in request.POST else "False"

    # MCM = Masa Corporal Magra
    MCM_Hombre = (1.10 * peso) - (128 * (peso * peso) / (altura * altura))
    MCM_Mujer = (1.07 * peso) - (148 * (peso * peso) / (altura * altura))

    #Proteinas necesarias Rango Minimo: 1.2 x Peso | Rango Mayor: 2 x Peso.
    RangoMinimo = 1.2 * peso
    RangoMayor = 2 * peso


    return render(request, "Calculadoras/CalcuMCM.html", {"MCM_H": MCM_Hombre, "MCM_M": MCM_Mujer, "sexo": sexo, "estado": estado, "RMinimo": RangoMinimo, "RMayor": RangoMayor})

def CalcuSalud(request):
    return render(request, "Calculadoras/CalcuSalud.html")