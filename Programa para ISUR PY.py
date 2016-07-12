#Programa de Organización de Instituto Del Sur.
#-------------------------Problema--------------------------------
"""
# saben en la pagina de Intituto de sur, hay mas opciones para nuestro PROGRAMA-----kevin--------
Nos pide:
-numeros de alumnos por carrera profesional
-precio de pensiones de cada carrera profesional
-precio de matriculas por alumno
-salario de docentes
-salario de administrativos
-salario de personal de servicio
-numero de alumnos aprobados
-numero de alumnos desaprobados
-cantidad de Cursos por semestre
-cantidad de Creditos por semestre
-
Este programa te Halla
1)Reporte : 
    1.-numero de alumnos(por cada carrera profesional), docentes, administrativos, personal de servicio
    2.-total de pensiones por carrera profesional
    3.-cantidad de Cursos por semestre
    4.-cantidad de Creditos por semestre
    5.-total de salario de docentes
    6.-total de salario de administrativos
    7.-total de salario de personal de servicio
    8.-monto total recaudado por matriculas
    9.-monto total recaudado por pagos de abandono
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
6) Reporte de cantid
"""
#tambien podemos añadir personas postulantes , egresados, capacitaciones, eventos 
#-------------------Aldo(Inicio)-------------------
def numalum(x):
    a=1
    while a!=0:
        na=input("Ingrese la cantidad de alumnos de {0} :".format(x))
        if na.isdigit():
            a=0
            print("Dato valido...")
        else:
            print("Error ingrese un numero")
            a=1
    return na

numalum("Negocios internacionales")
numalum("Diseño")
numalum("Marketin")
#------------------Aldo(Final)---------------------


#-----------------KEVIN-----------------
              INSTITUTO DEL SUR AREQUIPA
                MENU:
1.	¿Quiénes Somos?
	Identidad
Somos una comunidad educativa católica de alta especialización tecnológica, que a la luz de la espiritualidad sodálite, promueve integralmente la formación de la persona y el desarrollo de la sociedad
Visión
Seremos líderes con impacto nacional en la formación especializada de agentes comprometidos con el desarrollo integral de la sociedad.
Pilares
•	Comunidad educativa católica.
•	Alta especialización tecnológica.
•	Formación Integral de la persona humana.
•	Evangelización y desarrollo integral de la sociedad.
Valores
•	Compromiso, adheridos plenamente a nuestra identidad y visión, teniendo como centro a la persona humana.
•	Solidaridad, permanente actitud de servicio entre los miembros de nuestra comunidad educativa y hacia la sociedad.
•	Integridad, pensar y actuar con virtud y coherencia.
•	Excelencia, despliegue de nuestros talentos, según el máximo de nuestras capacidades y posibilidades.
•	Innovación, incorporar creativamente las nuevas tecnologías.

2.	Carreras Profesionales
	Escuela de negocios
	Administración de negocios bancarios y financieros 
	Administración de negocios Internacionales
	Marketing
	Escuela de turismo
	Administración de servicios de hostelería y restaurant
	Guía oficial de turismo
	Escuela de gastronomía
	gastronomía
	Escuela de tecnologías de la información 
	Administración y sistemas
	Desarrollo de sistema s de información 	
	Escuela de diseño
	Diseño gráfico multimedia
	Diseño y decoración de interiores
	Diseño de prendas de vestir

3.	Campus Virtual
Estimados alumnos:
Según las modificaciones a la normatividad legal vigente emitidas por el Ministerio de Educación, que involucran a nuestras actividades académicas desde el semestre 2016-I, les informamos lo siguiente:
1.	Matrícula 

Los estudiantes que desaprueben una o más asignaturas PODRÁN SER PROMOVIDOS DE SEMESTRE; debiéndose matricular en primer lugar en las asignaturas desaprobadas y luego completar sus créditos con las asignaturas del semestre superior.
2.	Titulación 

Para poder obtener el Título Profesional Técnico, se deberá cumplir con los siguientes requisitos:
o	Haber concluido y aprobado la totalidad de sus asignaturas.
o	Haber cumplido con sus prácticas pre-profesionales.
o	Haber aprobado el Proceso de Titulación en cualquiera de sus modalidades.
o	ACREDITAR EL CONOCIMIENTO DE UN IDIOMA EXTRANJERO O LENGUA NATIVA.
Con el objetivo de apoyar a nuestros alumnos en cumplir con este último requisito, el Instituto del Sur se encuentra trabajando en el lanzamiento de la LÍNEA DE INGLÉS SEMI PRESENCIAL, la cual se desarrollará en la plataforma virtual de PEARSON EDUCATION desde el próximo año. El costo, horarios y forma de matrícula serán comunicados oportunamente.
Atentamente,	
Martín Quintanilla Rodríguez
Director Académico

4.	Convenios Internacionales
	Practicas Pre- profesionales y clases de campo
	Capacitación empresarial
	Incubación y emprendimiento de negocios
	Capacitación en turismo 
	Capacitación en tecnologías de la información 
	Convalidación universitaria
	Capacitación en gestión 
5.	Contáctenos
Gracias por visitar nuestra página web. Para comunicarse con nosotros llame a nuestra central telefónica: 6044444, anexo 100 o escríbanos al correo informes@isur.edu.pe, para temas de consultas sobre nuestras carreras técnico profesionales y sus procesos de admisión, sobre temas de extensión profesional, sugerencias u otra información que necesite concerniente a nuestros servicios.
También lo atendemos personalmente de lunes a viernes de 08:30 a 13:00 h y de 16:00 a 19:30 h en el campus ubicado en Av. Salaverry 301, Vallecito, Arequipa.

1)	POSTULANTES
	Admisión 
	Carreras profesionales
	Carreras para gente que trabaja
	Convenios
	Ventajas Institucionales
2)	ESTUDIANTES
	Aulas virtuales
	Servicios estudiantiles
	Practicas pre-profesionales
	Información bibliográfica
	Información académica
	Extensión profesional
3)	EGRESADOS
	ISUR emplea
	Extensiones profesionales
4)	EMPRESAS
	ISUR emplea
	Extensión profesional
	Testimonios
	convenios
5)	EXTENSION PROFESIONAL
