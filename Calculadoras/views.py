from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import math

# Create your views here.

@csrf_exempt
def CalcuTMB(request):
    if request.method == "POST":
        # Get Datos = Recibe los datos del Usuario
        sexo = str(request.POST["sexo"]) if "sexo" in request.POST else "Mn"
        edad = int(request.POST["edad"]) if "edad" in request.POST else 18
        peso = int(request.POST["peso"]) if "peso" in request.POST else 70
        altura = int(request.POST["altura"]) if "altura" in request.POST else 170
        actividad = float(request.POST["actividad"]) if "actividad" in request.POST else 1.2
        macros = int(request.POST["DivirMacros"]) if "DivirMacros" in request.POST else 1


        # TMB = Tasa Metabolica Basal
        TMB_M = (10 * peso) + (6.25 * altura) - (5 * edad) + 161
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
        

        def MasMusculo(acti_M, acti_H, sexo):
            if sexo == "M":
                proteinasKcalM = (0.30 * acti_M)
                proteinasGramoM = proteinasKcalM / 4
                carbohidratosKcalM = (0.50 * acti_M)
                carbohidratosGramoM = carbohidratosKcalM / 4
                grasasKcalM = (0.20 * acti_M)
                grasasGramoM = grasasKcalM / 9
                contextMujer = {"data_k_proteM": proteinasKcalM,"data_g_proteM": proteinasGramoM,"data_k_carbM": carbohidratosKcalM, "data_g_carbM": carbohidratosGramoM, "data_k_grasasM":grasasKcalM, "data_g_grasasM": grasasGramoM}
                return contextMujer
            else:
                proteinasKcalH = (0.30 * acti_H)
                proteinasGramoM = proteinasKcalH / 4
                carbohidratosKcalH = (0.50 * acti_H)
                carbohidratosGramoH = carbohidratosKcalH / 4
                grasasKcalH = (0.20 * acti_H)
                grasasGramoH = grasasKcalH / 9
                contextHombre = {"data_k_proteH": proteinasKcalH, "data_g_proteH": proteinasGramoM, "data_k_carbH": carbohidratosKcalH, "data_g_carbH": carbohidratosGramoH, "data_k_grasasH": grasasKcalH, "data_g_grasasH": grasasGramoH}
                return contextHombre

        def Definicion(acti_M, acti_H, sexo):
            if sexo == "M":
                proteinasKcalM = (0.30 * acti_M)
                proteinasGramoM = proteinasKcalM / 4
                carbohidratosKcalM = (0.40 * acti_M)
                carbohidratosGramoM = carbohidratosKcalM / 4
                grasasKcalM = (0.30 * acti_M)
                grasasGramoM = grasasKcalM / 9
                contextMujer = {"data_k_proteM": proteinasKcalM,"data_g_proteM": proteinasGramoM,"data_k_carbM": carbohidratosKcalM, "data_g_carbM": carbohidratosGramoM, "data_k_grasasM":grasasKcalM, "data_g_grasasM": grasasGramoM}
                return contextMujer
            else:
                proteinasKcalH = (0.30 * acti_H)
                proteinasGramoM = proteinasKcalH / 4
                carbohidratosKcalH = (0.40 * acti_H)
                carbohidratosGramoH = carbohidratosKcalH / 4
                grasasKcalH = (0.30 * acti_H)
                grasasGramoH = grasasKcalH / 9
                contextHombre = {"data_k_proteH": proteinasKcalH, "data_g_proteH": proteinasGramoM, "data_k_carbH": carbohidratosKcalH, "data_g_carbH": carbohidratosGramoH, "data_k_grasasH": grasasKcalH, "data_g_grasasH": grasasGramoH}
                return contextHombre

        def PerderPeso(acti_M, acti_H, sexo):
            if sexo == "M":
                proteinasKcalM = (0.30 * acti_M)
                proteinasGramoM = proteinasKcalM / 4
                carbohidratosKcalM = (0.35 * acti_M)
                carbohidratosGramoM = carbohidratosKcalM / 4
                grasasKcalM = (0.35 * acti_M)
                grasasGramoM = grasasKcalM / 9
                contextMujer = {"data_k_proteM": proteinasKcalM,"data_g_proteM": proteinasGramoM,"data_k_carbM": carbohidratosKcalM, "data_g_carbM": carbohidratosGramoM, "data_k_grasasM":grasasKcalM, "data_g_grasasM": grasasGramoM}
                return contextMujer
            else:
                proteinasKcalH = (0.30 * acti_H)
                proteinasGramoM = proteinasKcalH / 4
                carbohidratosKcalH = (0.35 * acti_H)
                carbohidratosGramoH = carbohidratosKcalH / 4
                grasasKcalH = (0.35 * acti_H)
                grasasGramoH = grasasKcalH / 9
                contextHombre = {"data_k_proteH": proteinasKcalH, "data_g_proteH": proteinasGramoM, "data_k_carbH": carbohidratosKcalH, "data_g_carbH": carbohidratosGramoH, "data_k_grasasH": grasasKcalH, "data_g_grasasH": grasasGramoH}
                return contextHombre

        def MantenerPeso(acti_M, acti_H, sexo):
            if sexo == "M":
                proteinasKcalM = (0.20 * acti_M)
                proteinasGramoM = proteinasKcalM / 4
                carbohidratosKcalM = (0.50 * acti_M)
                carbohidratosGramoM = carbohidratosKcalM / 4
                grasasKcalM = (0.30 * acti_M)
                grasasGramoM = grasasKcalM / 9
                contextMujer = {"data_k_proteM": proteinasKcalM,"data_g_proteM": proteinasGramoM,"data_k_carbM": carbohidratosKcalM, "data_g_carbM": carbohidratosGramoM, "data_k_grasasM":grasasKcalM, "data_g_grasasM": grasasGramoM}
                return contextMujer
            else:
                proteinasKcalH = (0.20 * acti_H)
                proteinasGramoM = proteinasKcalH / 4
                carbohidratosKcalH = (0.50 * acti_H)
                carbohidratosGramoH = carbohidratosKcalH / 4
                grasasKcalH = (0.30 * acti_H)
                grasasGramoH = grasasKcalH / 9
                contextHombre = {"data_k_proteH": proteinasKcalH, "data_g_proteH": proteinasGramoM, "data_k_carbH": carbohidratosKcalH, "data_g_carbH": carbohidratosGramoH, "data_k_grasasH": grasasKcalH, "data_g_grasasH": grasasGramoH}
                return contextHombre

        
        GanarMusculo = MasMusculo(acti_M, acti_H, sexo)
        Definir = Definicion(acti_M, acti_H, sexo)
        PerdidaDePeso = PerderPeso(acti_M, acti_H, sexo)
        Mantenimiento = MantenerPeso(acti_M, acti_H, sexo)
        context = {"TMBH": TMB_H, "TMBM": TMB_M, "sexo": sexo, "actiM": acti_M, "actiH": acti_H, "adelH": adelgazar_H, "adelM": adelgazar_M, "aumenM": aumentar_M, "aumenH": aumentar_H}
        def Fucionar(macros, GanarMusculo, Definir, PerdidaDePeso, Mantenimiento, context):
            if macros == 1:
                context.update(GanarMusculo)
                return context
            elif macros == 2:
                context.update(Definir)
                return context
            elif macros == 3:
                context.update(PerdidaDePeso)
                return context
            else:
                context.update(Mantenimiento)
                return context

        Fucionar(macros, GanarMusculo, Definir, PerdidaDePeso, Mantenimiento, context)
        return render(request, "Calculadoras/CalcuTMB.html", context)
    else:
        return render(request, "Calculadoras/CalcuTMB.html")

@csrf_exempt
def CalcuIMC(request):
    if request.method == "POST":
        # Get Datos = Recibe los datos del Usuario
        peso = int(request.POST["peso"]) if "peso" in request.POST else 70
        altura = int(request.POST["altura"]) if "altura" in request.POST else 170

        # IMC = Indice de Masa Corporal
        def calIMC(altura, peso):
            m = (altura / 100)
            float(m)
            IMC = (peso/(m * m))
            return IMC
        IMC = calIMC(altura, peso)

        context = {"IMC": IMC}
        return render(request, "Calculadoras/CalcuIMC.html", context)
    else:
        return render(request, "Calculadoras/CalcuIMC.html")

@csrf_exempt
def CalcuPGCM(request):
    if request.method == "POST":
        # Get Datos = Recibe los datos del Usuario
        edad = int(request.POST["edad"]) if "edad" in request.POST else 18
        peso = int(request.POST["peso"]) if "peso" in request.POST else 70
        altura = int(request.POST["altura"]
                     ) if "altura" in request.POST else 160
        cuello = int(request.POST["cuello"]
                     ) if 'cuello' in request.POST else 45
        cintura = int(request.POST["cintura"]
                      ) if "cintura" in request.POST else 120
        cadera = int(request.POST["cadera"]
                     ) if "cadera" in request.POST else 105

        # PesoIdeal Mujer
        def PesoIdeal(altura, edad):
            PesoIdeal = 50 + ((altura - 150) / 4) * 3 + (edad - 20) / 4
            PesoIdealMujer = int(PesoIdeal * 0.9)
            return PesoIdealMujer

        # Peso Ideal
        PesoIdealMujer = PesoIdeal(altura, edad)
        KgFaltantes = int(peso - PesoIdealMujer)

        # PGC = Porcentaje de Grasa Corporal
        PGC_Mujer = 163.205 * math.log10(cintura + cadera - cuello) - 97.684 * math.log10(altura) - 78.387


        context = {"PGC_M": PGC_Mujer, "edad": edad, "PIdealM": PesoIdealMujer, "peso": peso, "KgF": KgFaltantes}
        return render(request, "Calculadoras/CalcuPGCM.html", context)

    else:
        return render(request, "Calculadoras/CalcuPGCM.html")

@csrf_exempt
def CalCuPGCH(request):
    if request.method == "POST":
        # Get Datos = Recibe los datos del Usuario
        edad = int(request.POST["edad"]) if "edad" in request.POST else 18
        peso = int(request.POST["peso"]) if "peso" in request.POST else 70
        altura = int(request.POST["altura"]) if "altura" in request.POST else 160
        cuello = int(request.POST["cuello"]) if 'cuello' in request.POST else 45
        cintura = int(request.POST["cintura"]) if "cintura" in request.POST else 120

        # PesoIdeal Hombre
        def PesoIdeal(altura, edad):
            PesoIdealHombre = 50 + ((altura - 150) / 4) * 3 + (edad - 20) / 4
            return PesoIdealHombre

         # Peso Ideal
        PesoIdealHombre = PesoIdeal(altura, edad)
        KgFaltantesH = int(peso - PesoIdealHombre)

        # PGC = Porcentaje de Grasa Corporal
        PGC_Hombre = 495 / (1.0324 - 0.19077 * math.log10(cintura - cuello) + 0.15456 * math.log10(altura)) - 450

        context = {"PGC_H": PGC_Hombre, "edad": edad, "PIdealH": PesoIdealHombre, "peso": peso, "KgF": KgFaltantesH}
        return render(request, "Calculadoras/CalcuPGCH.html", context)

    else:
        return render(request, "Calculadoras/CalcuPGCH.html")

@csrf_exempt
def CalcuMCM(request):
    if request.method == "POST":
        # Get Datos = Recibe los datos del Usuario
        sexo = str(request.POST["sexo"]) if "sexo" in request.POST else "M"
        peso = int(request.POST["peso"]) if "peso" in request.POST else 70
        altura = int(request.POST["altura"]) if "altura" in request.POST else 170

        # MCM = Masa Corporal Magra
        MCM_Hombre = (1.10 * peso) - (128 * (peso * peso) / (altura * altura))
        MCM_Mujer = (1.07 * peso) - (148 * (peso * peso) / (altura * altura))

        # MGC = Masa Grasa corporal
        MGC_Hombres = peso - MCM_Hombre
        MGC_Mujeres = peso - MCM_Mujer


        context = {"MCM_H": MCM_Hombre, "MCM_M": MCM_Mujer, "sexo": sexo, "MGC_M": MGC_Mujeres, "MGC_H": MGC_Hombres}
        return render(request, "Calculadoras/CalcuMCM.html", context)

    else:
        return render(request, "Calculadoras/CalcuMCM.html")


def CalcuSalud(request):
    return render(request, "Calculadoras/CalcuSalud.html")
