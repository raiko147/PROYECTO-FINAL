#PROGRAMACION 2
#programa base de datos menu principal

from modulow import *
from especialidades import *
from logoISUR import logo
import time
import sys
import os
import sqlite3

def ingresoAlfabetico(denominacion,limite): #funcion de ingreso alfabetico denominacion es que lo que va ingresar
    nombre , j, k= '', 0, 0
    denominacion = denominacion.title()
    while not ( len(nombre) == j and k <= limite and j > 0 ):
        k, nombre = 0 , str(input('Ingrese {} Completos: \n'.format(denominacion)))
        nombre = nombre.title()
        for i in nombre:
            k+=1
        nombre = nombre.split()
        nombreConcatenado = ''
        j = 0
        for i in nombre:
            if i.isalpha():
                j+=1
                nombreConcatenado += i+' '
        if not (len(nombre) == j and k <= limite and j > 0):
            print('\tIngrese {} alfabeticos o denominacion aceptable'.format(denominacion))
        nombreConcatenado = nombreConcatenado[:-1]
    return nombreConcatenado

def ingresoAlfanumerico(denominacion, limitemayor, limiteinferior): #funcion de ingreso alfabetico denominacion es que lo que va ingresar
    nombre , j, k = '', 0, -1
    denominacion = denominacion.title()
    while not (len(nombre) == j and j>= limiteinferior and k >= limiteinferior and k <= limitemayor ):
        k, nombre = 0, str(input('Ingrese {} : \n'.format(denominacion)))
        nombre = nombre.title()
        for i in nombre:
            k += 1
        nombre = nombre.split()
        Concatenado = ''
        j = 0
        for i in nombre:
            if i.isalnum():
                j+=1
                Concatenado += i+' '
        if not (len(nombre) == j and j>=limiteinferior and k >= limiteinferior and k <= limitemayor ):
            print('\tIngrese {} alfanumericos o denominacion aceptable'.format(denominacion))
        Concatenado = Concatenado[:-1]
    if k == 0:
        return None
    else:
        return Concatenado

def ingresoNumerico(denominacion,limite):
    #funcion de ingreso numerico denominacion (str)es el nombre de que lo que ingresa , limite (int)= cantidad numeros permitidos
    numero,j = 0,0
    denominacion = denominacion.title()
    while not (len(str(numero)) == limite and j == limite):
        j = 0
        numero = input('Ingrese {}: \t'.format(denominacion))
        if len(numero) > 0:
            if numero[0] == '0':
                print('\tNo puede con cero {}'.format(denominacion))
                j-=1
        for i in numero:
            if i.isdigit():
                j += 1
                #print('j+1')
        if not (len(str(numero)) == limite and j == limite):
            print('\tIngrese correctamente aceptable {} dijitos'.format(limite))
    return numero
def ingresoNumericoVariable(denominacion):
    numero,j = 0,0
    denominacion = denominacion.title()
    while not (len(str(numero)) == j):
        j = 0
        numero = input('Ingrese {}: \t'.format(denominacion))
        if len(numero) > 0:
            if numero[0] == '0':
                print('\tNo puede con cero {}'.format(denominacion))
                j-=1
        for i in numero:
            if i.isdigit():
                j += 1
                #print('j+1')
        if not (len(str(numero)) == j):
            print('\tIngrese correctamente aceptable {} dijitos'.format(limite))
    return numero

def ingresoCorreo(denominacion, limitemayor, limiteinferior):
    correo, j,k,m ="",0,0,0
    while not ("@" in correo and j == 0 and k<=limitemayor and k>=limiteinferior and m>0):
        correo = input("Ingrese {}: ".format(denominacion))
        for i in correo:
            if i == " ":
                j+=1
            elif i==".":
                m +=1
            k+=1
        if not ("@" in correo and j == 0 and k<=limitemayor and k>=limiteinferior and m>0):
            print("Ingrese un correo valido")
    return correo

def inscripcionNueva():
    global codigo, b

    #ingreso datos del nuevo alumno
    s = ' '
    while not (s.lower() == 'si' or s == 'c'):

        print('\tINGRESO DATOS')


    #nombre var (20), apellidos var(20), edad integer(2), dni integer(8), direccion var(30),
    # #sexo,#correo, especialidad, observaciones var(60),

        #ingreso de apellidos y nombres completos
        nombre = ingresoAlfabetico("nombres",20)                    #ingreso nombre
        apellido = ingresoAlfabetico("apellidos",20)                #ingreso apellido
        edad = ingresoNumerico("edad",2)                            #ingreso edad
        dni = ingresoNumerico("dni", 8)                             #ingreso dni
        direccion = ingresoAlfanumerico("direccion", 30, 1)         #ingreso direccion
        #ingreso sexo
        sexo =""
        while not (sexo.lower()=="m" or sexo.lower()=="f"):
            sexo = ingresoAlfabetico("sexo (M/F)",1)
            sexo = sexo.upper()
            if not (sexo.lower()=="m" or sexo.lower()=="f"):
                print("Error solo masculino (M) femenino (F)")
        #ingreso correo
        correo = ingresoCorreo("correo",32,5)

        #Ingreso la especilidad que estudiara
        especialidad = especialidadesisur.carreras()
        print('\tEspecialidad que estudia : ')
        j, opcion = 1, ''
        respuesta = ''
        while not ((respuesta in opcion) and len(respuesta)>0 and len(especialidad)<= j):
            j = 1
            for i in especialidad:
                print('{0}.-{1}'.format(j, i))
                opcion += str(j)
                j +=1
                #print(opcion)
            respuesta = input('\tIngrese una opcion de la Especialidad: ')
            if not ((respuesta in opcion) and len(respuesta) > 0 and len(especialidad)<= j):
                print('Ingrese una opcion correcta\n')
                time.sleep(3)
                os.system('clear')
        respuesta = int(respuesta)
        respuestaEligida = especialidad[respuesta-1]
        observaciones = ingresoAlfanumerico("observaciones (opcional)", 60, 0)
        #bucle para ingreso de confirmacion
        while not (s.lower() == 'si' or s == 'c'):
            s = input('Para guardar SI, cancelar C : ')
            if not (s.lower() == 'si' or s.lower() == 'c') :
                print('\tError ingrese opcion correcta')

    #termina la confirmacion de inscripcion
    if s.lower() == 'si':
        if observaciones == None:
            observaciones = ''
        return [nombre,apellido,edad,dni,direccion, sexo, correo, respuestaEligida, observaciones]

    else:
        print('Los datos ingresados no se registraron')
        return None
def tablaCodigo(nombretabla,nombre_columna,categoria):
    cursor.execute("select {0} from {1}".format(nombre_columna, nombretabla))
    id = []
    for i in cursor:
        id.append(i[0])
    s = ""
    print("\tCodigos registrados {0} ".format(id))
    print("\tCantidad Registrados: {0} {1}".format(len(id),categoria))
    while not ( s in id or len(id) == 0):
        while True:
            try:
                s = int(input("\nIngrese codigo: "))
                break
            except: print("\tError ingrese codigo valido")
        if not (s in id ):
            print("\tIngrese un codigo registrado\n")
    if len(id) == 0:
        print("Registro vacio")
        return
    cota = [nombretabla,s]
    return cota

def reporte(nombretabla,nombreColumna_de_codigo,lista_reporte):
    cursor.execute("select {0} from {1}".format(nombreColumna_de_codigo,nombretabla))
    id = []
    for i in cursor:
        id.append(i[0])
    s =''
    while not (s == "no" or s=="n") or (s=="si" or s=="s"):
        t = ''
        while not (t =="3") :
            print("\n\tMENU REPORTE")
            t = input("1.-Reporte completo\n2.-Reporte por codigo\n3.-Salir\n\nIngrese una opcion >")

            if t =="1":
                print()
                cursor.execute("select * from {} ".format(nombretabla))
            elif t =="2":
                print()
                #ingreso de codigo
                codigo = tablaCodigo(nombretabla, nombreColumna_de_codigo," ")
                if codigo :
                    cursor.execute("select * from {0} where {2} in ({1})".format(codigo[0],codigo[1],nombreColumna_de_codigo))
                codigo = "" #deshace el codigo para el nuevo reporte
            x,datos =0, lista_reporte
            #imprime el reporte depende de la opcion
            print()
            for i in cursor:
                x= 0
                for j in i:
                    print("{0}: {1}".format(datos[x],j))
                    x+=1
                print()
                time.sleep(1)
            time.sleep(2)
            os.system("clear")
            #opcion salida
            if (t =="3"):
                break
            else: #cuando la opcion es incorrecta
                print("Ingrese opcion de reporte")
        s = input("Quiere continuar en el menu reporte si/no:").lower()
        if not (s == "no" or s=="n") or (s=="si" or s=="s"):
            print("\tEsta en menu reporte ingrese una opcion correcta")

def modificar(nombretabla, columna_codigo):
    print()
    s=''
    while not (s=='3' ):
        print("Menu Modificacion datos")
        s = input("1.-Modificar segun al codigo\n2.-Consultar datos\n3.-Cancelar\nIngrese una opcion >>")
        if s == "1":
            codigo = tablaCodigo(nombretabla, columna_codigo," ")
            codigo = codigo[1]
            dat = inscripcionNueva()
            print(end="\tActualizando...")
            cursor.execute("update {10} set nombre=\"{0}\",apellidos=\"{1}\",edad=\"{2}\",dni=\"{3}\","
                           "direccion=\"{4}\",sexo=\"{5}\",correo=\"{6}\",especialidad=\"{7}\",observaciones=\"{8}\" where id = \"{9}\""
                           "".format(dat[0],dat[1],dat[2],dat[3],dat[4],dat[5],dat[6],dat[7],dat[8],codigo,nombretabla))
            con.commit()
            print("ok\n")
        elif s == "2":
            lista = ["Codigo","Nombres","Apellidos","Edad","DNI","Direccion", "Sexo", "Correo","Especialidad","Observaciones"]
            reporte(nombretabla,columna_codigo,lista)
        if not (s in '123' and len(s)==1 ):
            print("\tIngrese opcion correcta")
def menuAlumno():
            print("\tMenu Alumno")
            opcion, j, opcionElegido, menuAlumno = " ", 1,"", especialidadesisur.opcionesAlumnos()
            for i in menuAlumno:
                opcion += str(j)
                j +=1
            opcion += str(j)
            while not (opcionElegido == opcion[-1]):#error string index out of range -- por que [-1] es la ultimacifra
                j = 1
                for i in menuAlumno:
                    print("{0}.-{1}".format((j), i))
                    j += 1
                print("{}.-Salir de menu alumno".format(j))

                opcionElegido = input("\tIngrese una opcion >> ".format(j))
                if opcionElegido == "1":
                    datos = inscripcionNueva()
                    if datos :
                        print(end="\tguardando... ")
                        cursor.execute("insert into registro(nombre,apellidos,edad,dni,direccion,sexo,correo,especialidad,observaciones) "
                                       "values(\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\",\"{5}\",\"{6}\",\"{7}\",\"{8}\")"
                                       "".format(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8]))
                        con.commit()
                        print("ok")
                #reporte estudiantes
                elif opcionElegido == "2":
                    lista = ["Codigo","Nombres","Apellidos","Edad","DNI","Direccion", "Sexo", "Correo","Especialidad","Observaciones"]
                    reporte("registro","id",lista)
                #modificar datos

                elif opcionElegido == "3":
                    print("\tModificacion de datos")
                    modificar("registro","id")
                #eliminar datos
                elif opcionElegido == "4":
                    print("\tEliminar registro")
                    codigo = tablaCodigo("registro","id"," Estudiante(s)")
                    codigo = codigo[-1]
                    s = ""
                    while not (s=="si" or s=="no" or s=="s" or s=="n" or codigo ==None ):
                        s = input("Esta seguro que desea eliminar el codigo {} si/no: ".format(codigo)).lower()
                        if s == "si" or s=="s" :
                            print(end="\teliminando... ")
                            cursor.execute("delete from registro where id =\'{}\'".format(codigo))
                            con.commit()
                            print("ok")
                        elif s =="no" or s=="n" :
                            print("\tcancelado")
                        if not (s=="si" or s=="no"or s=="s" or s=="n"):
                            print("\tconfirme correctamente")
                if not (opcionElegido == opcion[-1]):
                    print("Ingrese una opcion")

            print()
            os.system("clear")
def menuDocentes():
            print("\tMenu Docente")
            opcion, j, opcionElegido, menuAlumno = "", 1," ", especialidadesisur.opcionesDocentes()
            for i in menuAlumno:
                opcion += str(j)
                j += 1

            opcion += str(j)
            while not (opcionElegido == opcion[-1]):
                j = 1
                for i in menuAlumno:
                    print("{0}.-{1}".format((j), i))
                    j += 1
                print("{}.-Salir de menu Docente".format(j))
                opcionElegido = input("\tIngrese una opcion >> ".format(j))
                if opcionElegido == "1":
                    datos = inscripcionNueva()
                    if datos :
                        print(end="\tguardando... ")
                        cursor.execute("insert into docentes(nombre,apellidos,edad,dni,direccion,sexo,correo,especialidad,observaciones) "
                                       "values(\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\",\"{5}\",\"{6}\",\"{7}\",\"{8}\")"
                                       "".format(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8]))
                        con.commit()
                        print("ok")
                #reporte estudiantes
                elif opcionElegido == "2":
                    lista = ["Codigo","Nombres","Apellidos","Edad","DNI","Direccion", "Sexo", "Correo","Especialidad","Observaciones"]
                    reporte("docentes","codigo",lista)
                #modificar datos

                elif opcionElegido == "3":
                    print("\tModificacion de datos")
                    modificar("docentes","codigo")
                #eliminar datos
                elif opcionElegido == "4":
                    print("\tEliminar registro")
                    codigo = tablaCodigo("docentes","codigo"," Docente(s)")
                    codigo = codigo[1]
                    s = ""
                    while not (s=="si" or s=="no" or s=="s" or s=="n" or codigo ==None ):
                        s = input("Esta seguro que desea eliminar el codigo {} si/no: ".format(codigo)).lower()
                        if s == "si" or s=="s" :
                            print(end="\teliminando... ")
                            cursor.execute("delete from docentes where codigo =\'{}\'".format(codigo))
                            con.commit()
                            print("ok")
                        elif s =="no" or s=="n" :
                            print("\tcancelado")
                        if not (s=="si" or s=="no"or s=="s" or s=="n"):
                            print("\tconfirme correctamente")
                if not (opcionElegido == opcion[-1]):
                    print("Ingrese una opcion")

            print()
            os.system("clear")

def menuAdministrativos():
            print("\tMenu Administrativos")
            opcion, j, opcionElegido, menuAlumno = " ", 1,"", especialidadesisur.opcionesAdministrativos()
            for i in menuAlumno:
                opcion += str(j)
                j +=1
            opcion += str(j)
            while not (opcionElegido == opcion[-1]):#error string index out of range -- por que [-1] es la ultimacifra
                j = 1
                for i in menuAlumno:
                    print("{0}.-{1}".format((j), i))
                    j += 1
                print("{}.-Salir de menu Administrativo".format(j))

                opcionElegido = input("\tIngrese una opcion >> ".format(j))
                if opcionElegido == "1":
                    datos = inscripcionNueva()
                    if datos :
                        print(end="\tguardando... ")
                        cursor.execute("insert into administrativos(nombre,apellidos,edad,dni,direccion,sexo,correo,especialidad,observaciones) "
                                       "values(\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\",\"{5}\",\"{6}\",\"{7}\",\"{8}\")"
                                       "".format(datos[0],datos[1],datos[2],datos[3],datos[4],datos[5],datos[6],datos[7],datos[8]))
                        con.commit()
                        print("ok")
                #reporte estudiantes
                elif opcionElegido == "2":
                    lista = ["Codigo","Nombres","Apellidos","Edad","DNI","Direccion", "Sexo", "Correo","Especialidad","Observaciones"]
                    reporte("administrativos","codigo", lista)
                #modificar datos

                elif opcionElegido == "3":
                    print("\tModificacion de datos")
                    modificar("administrativos","codigo")
                #eliminar datos
                elif opcionElegido == "4":
                    print("\tEliminar registro")
                    codigo = tablaCodigo("administrativo","codigo"," Administrativo(s)")
                    codigo = codigo[-1]
                    s = ""
                    while not (s=="si" or s=="no" or s=="s" or s=="n" or codigo ==None ):
                        s = input("Esta seguro que desea eliminar el codigo {} si/no: ".format(codigo)).lower()
                        if s == "si" or s=="s" :
                            print(end="\teliminando... ")
                            cursor.execute("delete from administrativos where id =\'{}\'".format(codigo))
                            con.commit()
                            print("ok")
                        elif s =="no" or s=="n" :
                            print("\tcancelado")
                        if not (s=="si" or s=="no"or s=="s" or s=="n"):
                            print("\tconfirme correctamente")
                if not (opcionElegido == opcion[-1]):
                    print("Ingrese una opcion")

            print()
            os.system("clear")
def menuMatriculas():
            print("\tMenu Matriculas")
            opcion, j, opcionElegido, menuMatriculas = " ", 1, "", especialidadesisur.opcionesMatriculas()

            for i in menuMatriculas:
                opcion += str(j)
                j +=1
            opcion += str(j)
            while not (opcionElegido == opcion[-1]):#error string index out of range -- por que [-1] es la ultimacifra
                j = 1
                for i in menuMatriculas:
                    print("{0}.-{1}".format((j), i))
                    j += 1
                print("{}.-Salir de menu Matriculas".format(j))

                opcionElegido = input("\tIngrese una opcion >> ".format(j))
                if opcionElegido == "1":
                    ciclo = ingresoAlfanumerico("ciclo de matricula (año ciclo=A,B)",8,2)
                    semestre = ingresoAlfanumerico("semestre (I,II)",2,1)
                    codigo_alumno = tablaCodigo("registro","id"," Estudiante(s)")
                    print()
                    if codigo_alumno :
                        print(end="\tguardando... ")
                        cursor.execute("insert into matriculas( ciclo ,semestre_academico , codigo_alumno) "
                                       "values(\"{0}\",\"{1}\",\"{2}\")"
                                       "".format(ciclo,semestre, codigo_alumno[1]))
                        con.commit()
                        print("ok")
                #reporte estudiantes
                elif opcionElegido == "2":
                    lista = ["Codigo Matricula","Ciclo", "Semestre Academico", "Codigo Alumno"]
                    reporte("matriculas","codigo", lista)
                #modificar datos

                elif opcionElegido == "3":
                    print("\tModificacion de datos")
                    modificar("codigo_matricula","codigo")
                #eliminar datos
                elif opcionElegido == "4":
                    print("\tEliminar registro")
                    codigo = tablaCodigo("codigo_matricula","codigo"," Matriculas")
                    codigo = codigo[-1]
                    s = ""
                    while not (s=="si" or s=="no" or s=="s" or s=="n" or codigo ==None ):
                        s = input("Esta seguro que desea eliminar el codigo {} si/no: ".format(codigo)).lower()
                        if s == "si" or s=="s" :
                            print(end="\teliminando... ")
                            cursor.execute("delete from matriculas where id =\'{}\'".format(codigo))
                            con.commit()
                            print("ok")
                        elif s =="no" or s=="n" :
                            print("\tcancelado")
                        if not (s=="si" or s=="no"or s=="s" or s=="n"):
                            print("\tconfirme correctamente")
                if not (opcionElegido == opcion[-1]):
                    print("Ingrese una opcion")

            print()
            os.system("clear")
def menuPagos():
            print("\tMenu Pagos")
            opcion, j, opcionElegido, menuPago = " ", 1, "", especialidadesisur.opcionesPagos()

            for i in menuPago:
                opcion += str(j)
                j +=1
            opcion += str(j)
            while not (opcionElegido == opcion[-1]):#error string index out of range -- por que [-1] es la ultimacifra
                j = 1
                for i in menuPago:
                    print("{0}.-{1}".format((j), i))
                    j += 1
                print("{}.-Salir de menu Pagos".format(j))

                opcionElegido = input("\tIngrese una opcion >> ".format(j))
                if opcionElegido == "1":
                    concepto = ingresoAlfanumerico("Concepto de pago",60,2)
                    cantidad = ingresoNumericoVariable("Cantidad de")
                    s = ""
                    while not (s=="1" or s == "2" or s.lower() == "c"):
                        s = input("Generar recibo para:\n1.-Docente\n2.-Administrativo\ningrese una opcion >>")
                        if s == "1":
                            codigo_benificiado = tablaCodigo("docentes","codigo"," Docente(s)")
                        elif s == "2":
                            codigo_benificiado = tablaCodigo("administrativos","codigo", " Administrativos")
                        elif not (s=="1" or s == "2" or s.lower() == "c"):
                            print("Ingrese una opcion")
                    print()
                    if codigo_benificiado :
                        print(end="\tguardando... ")
                        cursor.execute("insert into pagos(concepto, cantidad, codigo_nombre"
                                       "values(\"{0}\",\"{1}\",\"{2}\",\"{3}\")"
                                       "".format(concepto,cantidad, codigo_benificiado))
                        con.commit()
                        print("ok")
                #reporte
                elif opcionElegido == "2":
                    lista = ["Codigo de Recibo", "Concepto", "Cantidad", "Emitido (codigo)"]
                    reporte("pagos","codigo_recibo",lista)
                #modificar datos

                elif opcionElegido == "3":
                    print("\tModificacion de datos")
                    modificar("codigo_recibo","codigo_recibo")
                #eliminar datos
                elif opcionElegido == "4":
                    print("\tEliminar registro")
                    codigo = tablaCodigo("pagos","codigo_recibo"," Recibo(s)")
                    codigo = codigo[-1]
                    s = ""
                    while not (s=="si" or s=="no" or s=="s" or s=="n" or codigo ==None ):
                        s = input("Esta seguro que desea eliminar el codigo {} si/no: ".format(codigo)).lower()
                        if s == "si" or s=="s" :
                            print(end="\teliminando... ")
                            cursor.execute("delete from pagos where codigo_recibo =\'{}\'".format(codigo))
                            con.commit()
                            print("ok")
                        elif s =="no" or s=="n" :
                            print("\tcancelado")
                        if not (s=="si" or s=="no"or s=="s" or s=="n"):
                            print("\tconfirme correctamente")
                if not (opcionElegido == opcion[-1]):
                    print("Ingrese una opcion")

            print()
            os.system("clear")

def menuPrincipal():
    opciones = especialidadesisur.opcionesmenuprincipal()
    j,k, s = 1,'', ''
    for i in opciones:
        k+=str(j)
        j+=1
    k+=str(j)
    k = str(k)
    while not ((s == k[-1] and len(s)==1) or (s == "no" or s=="n")):
        t = ""
        while not (t in k and len(t)==1):
            print("\tINSTITUTO DEL SUR AREQUIPA\n\tMENU PRINCIPAL")
            j = 1
            for i in opciones:
                print("{0}.-{1}".format(j, i))
                j+=1
            print("{0}.-SALIR DEL PROGRAMA".format(j))
            t = input("\n\tIngrese una opcion: ")
            if not (t in k and len(t)==1 ):
                print('Ingrese una opcion correcta')
        #nueva inscripcion
        if t == "1":
            menuAlumno()
        #reporte estudiantes
        elif t == "2":
            print("docentes")
            menuDocentes()
        #modificar datos

        elif t == "3":
            print("\tPersonal administrativo")
            menuAdministrativo()

        #eliminar datos
        elif t == "4":
            print("\tmatriculas")
            menuMatriculas()

        #pagos
        elif t == "5" :
            menuPagos()
        print()
        s = input("Desea continuar en el programa principal? si/no:").lower()
        if not ((s == k[-1] and len(s)==1) or s == "si" or s=="no" or s=="s" or s=="n"):
            print("Ingrese correctamente las opciones")
        os.system("clear")


#iniciar coneccion datos
os.system('clear')
print (end="\tINSTITUTO DEL SUR AREQUIPA\nConectando base datos...")
con=sqlite3.connect("trabajo-final.db")
print("OK")
time.sleep(1)
os.system("clear")
logo()
time.sleep(2)
os.system("clear")
cursor=con.cursor()
menuPrincipal()
#cerrar coneccion
con.commit()
print(end="\tCerrando coneccion base datos... ")
con.close()
print("ok")
print("\tAdios \4\4")

