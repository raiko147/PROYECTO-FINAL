#Programa de Organización de Instituto Del Sur.
#-------------------------Problema--------------------------------
"""

nos pide:
-numeros de alumnos por carrera profesional
-precio de pensiones de cada carrera profesional
-precio de matriculas por alumno
-salario de docentes
-salario de administrativos
-salario de personal de servicio
-numero de alumnos aprobados
-numero de alumnos desaprobados
Este programa te alla
1)Reporte : 
    1.-numero de alumnos(por cada carrera profesional), docentes, administrativos, personal de servicio
    2.-total de pensiones por carrera profesional
    3.-total de salario de docentes
    4.-total de salario de administrativos
    5.-total de salario de personal de servicio
    6.-monto total recaudado por matriculas
    7.-monto total recaudado por pagos de abandono
2) El dato estadistico en porcentaje de alumnos aprobados (su ponderado mayor o igual 11) y desaprobados
(su ponderado menor a 11) en todo el instituto, Abandonos, Matriculados
3) Reporte de dinero recaudado por pensiones  de alumnos si:
    -La pension es de 300 nuevos soles(segun cada carrera profesional)
4) Reporte del pago de los Docentes que estan enseñando si se sabe:
    -Son 11 Carreras y por cada carrera hay cuatro Docente
    -El pago por docente es de 1200 soles(suposicion)
5) Reporte financiero cada mes teniendo como datos:
    -Monto de dinero con que cuenta el ISUR en (soles)[inicial]
    -Monto de Gastos(salarios docentes, salarios administrativos, salarios personal de servicio)
    -Monto de ingresos(pensiones, matriculas, monto de abandono)
    total_dinero= monto_dinero_inicial + ingresos - gastos
"""
#tambien podemos añadir personas postulantes , egresados, capacitaciones, eventos 
#-------------------Aldo(Inicio)-------------------
def numalum (x):
    a=1
    while a!=0:
        na=input("Ingrese la cantidad de alumnos de ",x," :" )
        try:
            na=abs(int(na))
            a=0
            print("Dato valido...")
        except:
            print("Error ingrese un dato correcto...")
            n=1
return na


#------------------Aldo(Final)---------------------
