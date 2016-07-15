from modulow import *
from especialidades import *
import time
import sys
import os

codigo = 1
b = []
def inscripcionNueva():
    global codigo, b

    #ingreso datos del nuevo alumno
    s = ' '
    while not (s.lower() == 'si' or s == 'c'):

        print('\tINGRESO DATOS DEL NUEVO ESTUDIANTE')

        #ingreso de nombres ojo ingreso de varios nombres
        nombre , j= ' ', 0
        while not len(nombre) == j:
            nombre = str(input('Ingrese Nombres Completos: \n'))
            nombre = nombre.title()
            nombre = nombre.split()
            nombreConcatenado = ''
            j = 0
            for i in nombre:
                if i.isalpha():
                    j+=1
                    nombreConcatenado += i+' '
            if not len(nombre) == j:
                print('\tIngrese nombre alfabetico')
            nombreConcatenado = nombreConcatenado[:-1]

        #ingreso de apellidos completos
        apellidos, j = ' ', 0
        while not len(apellidos)== j:
            apellidos = input('Ingrese Apellidos Completos:\n')
            apellidos= apellidos.title()
            apellidos = apellidos.split()

            #prueba si es alfabetico
            apellidoConcatenado,j = '', 0
            for i in apellidos:
                if i.isalpha():
                    j+=1
                    apellidoConcatenado += i+' '
            if not len(apellidos) == j:
                print('\tdIngrese apellidos alfabeticos')
            apellidoConcatenado = apellidoConcatenado[:-1]

        #bucle pra iniciar ingreso DNI acepta 8 dijitos
        dni,j = 0,0
        while not (len(str(dni)) == 8 and j == 8):
            j = 0
            dni = input('Ingrese el numero DNI: \t')
            if dni[0] == '0':
                print('\tNo puede empezar con cero el DNI')
                j-=1
            for i in dni:
                if i.isdigit():
                    j += 1
                    #print('j+1')
            if not (len(str(dni)) == 8 and j == 8):
                print('\tIngrese correctamente')
        dni = int(dni)

        #ingreso direccion
        direccion, j = ' ', 0
        while not len(direccion)== j:
            direccion = input('Ingrese Direccion: \t')
            direccion = direccion.title()
            direccion = direccion.split()
            #formatea la direccion
            direccionConcatenado,j = '', 0
            for i in direccion:
                j+=1
                direccionConcatenado += i+' '
            if not len(direccion) == j:
                print('\tdIngrese datos alfanumericos')
            direccionConcatenado = direccionConcatenado[:-1]

        #Ingreso la especilidad que estudiara
        especialidad = especialidadesisur.carreras()
        print('\tEspecialidad que estudiara el estudiante')
        j, opcion = 1, ''
        respuesta = ' '
        while not (respuesta in opcion):
            j = 1
            for i in especialidad:
                print('{0}.-{1}'.format(j, i))
                opcion += str(j)
                j +=1
            #print(opcion)
            respuesta = input('\tIngrese una opcion de la Especialidad: ')
            if not (respuesta in opcion):
                print('Ingrese una opcion correcta\n')
                time.sleep(3)
                os.system('clear')
        respuesta = int(respuesta)
        respuestaEligida = especialidad[respuesta-1]

        s = input('Para confirmar ingrese SI, cancelar C : ')
        if not s.lower() == 'si' or s.lower() == ' ' :
            print('Cancelado')

    #termina la confirmacion de inscripcion
    if s.lower() == 'si':
        b.append([codigo])
        #[ nombre, apellidos, dni, direccion, Especialidad ]
        a = matriculas(nombreConcatenado, apellidoConcatenado, dni, direccionConcatenado, respuestaEligida)
        b[abs(codigo-1)].append(a.Alumnos())
        print(b)
    else:
        print('Los datos ingresados no se registraron')

inscripcionNueva()