from django.urls import path
from Calculadoras import views


urlpatterns = [
    path('CalcuTMB/',views.CalcuTMB , name="CalcuTMB"),
    path('CalcuIMC/',views.CalcuIMC, name="CalcuIMC"),
    path('CalcuPGC/Mujeres/',views.CalcuPGCM, name="CalcuPGCM"),
    path('CalcuPGC/Hombres/',views.CalCuPGCH, name="CalcuPGCH"),
    path('CalcuMCM/',views.CalcuMCM, name="CalcuMCM"),
    path('',views.CalcuSalud, name="CalcuSalud")
]
