import os
import sys,time
import sqlite3

def verificar(a):
    for c in a:
        if((ord(c)<65 or ord(c)>90 ) and (ord(c)<97 or ord(c)>122) and (ord(c)!=32)):
            return False
    return True

def nuevo():
    os.system("cls")
    nombre=input(("Ingrese su nombre: "))
    while(not verificar(nombre)):
        print("Nombre Incorrecto...!!!vuelva Intentar")
        nombre=input(("Ingrese su nombre: "))
    apellidos=input(("Ingrese sus Apellidos: "))
    while(not verificar(apellidos)):
        print("Apellido Incorrecto...!!!Vuelva Intentar")
        apellidos=input(("Ingrese sus Apellidos: "))
    while(1):
        try:
            print("Ingrese su Edad")
            edad=input()
            edad=int(edad)
            while(edad<0 or edad>170):
                print("Edad Incorrecta...!!!vuelva intentar: ")
                edad=input()
                edad=int(edad)
            break
        except ValueError:
            print("Ingrese correctamente ...: ")
    while(1):
        try:
            print("Ingrese su DNI")
            dni=input()
            dni=int(dni)
            while(len(str(dni))!=8):
                dni=int(input("Error...!!!Ingrese DNI de 8 digitos"))
            break
        except ValueError:
            print("Error...!!!Ingrese correctamente su DNI")
    data_sexo=""
    while(1):
        try:
            print("Ingrese su Sexo F/M: ")
            sexo=input()
            sexo=str(sexo)
            while(len(str(sexo))!=1):
                print("Ingrese solo un caracter F o M : ")
            sexo=input()
            sexo=str(sexo)
            data_sexo=str(sexo)
            break
        except ValueError:
            print("Ingrese Correctamente su Sexo F/M: ")
    if (data_sexo[0:1] == "F"):
        sexo=F
    elif(data_dni[0:2]=="M"):
        sexo==M
    correo=input()
    print("Ingrese su Especialidad")
    especialidad=input()
    while(not verificar(especialidad)):
        especialidad=input("Ingrese su Especialidad corretamente: ")
    print("Ingrese sus Observaciones")
    observaciones=input()
    while(not verificar(observaciones)):
        observaciones=input("Ingrese sus Observaciones correctamente: ")

    con=sqlite3.connect("trabajo final.s3db")
    cursor=con.cursor()
    cursor.execute("insert into instituto (nombre,edad,dni) values ('"+nombre+"','"+edad+"','"+str(dni)+"')")
    con.commit()
    con.close()
    time.sleep(3)
    menu()

def menu():
    os.system("cls")
    print("Base de datos del Instituto del Sur")
    print("")
    print("\t1.- Agregar datos del Alumno")
    print("\t2.- Ver Alumno")
    print("\t3.- Modificar datos del Alumno")
    print("\t4.- Eliminar datos del Alumno")
    print("\t5.- Salir")
    while(1):
        try:
            print("Ingrese una Opcion")
            entrada=input()
            entrada=int(entrada)
            while(entrada<0 or entrada>5):
                print("Error...!!!Ingrese correctamente la opcion")
                entrada=input()
                entrada=int(entrada)
            break
        except ValueError:
            print("Ingrese correctamente una opcion valida")
    if (entrada==1):
        nuevo()
    elif(entrada==2):
        reporte()
    elif(entrada==3):
        modificar()
    elif(entrada==4):
        iliminar()
    elif(entrada==5):
        sys.exit()

def reporte():
    con=sqlite3.connect("trabajo final.s3db")
    cursor=con.cursor()
    cursor.execute("select*from instituto ")
    for instituto in cursor:
        print("")
        print("\t Alumnos Agregados")
        print("\t------------------------")
        print("\t Nombre:"'\t'+str(instituto[1]))
        print("\t Edad:"'\t'+str(instituto[2]))
        print("\t DNI:"'\t'+str(instituto[3]))
        print("\t Codigo:"'\t'+str(instituto[0]))
    con.commit()
    con.close()
    input()
    menu()
def modificar():
    con=sqlite3.connect("trabajo final.s3db")
    cursor=con.cursor()
    cursor.execute("select*from instituto ")
    for instituto in cursor:
        print("")
        print("\t Alumnos agregados")
        print("\t------------------------")
        print("\t Nombre:"'\t'+str(instituto[1]))
        print("\t Edad:"'\t'+str(instituto[2]))
        print("\t DNI:"'\t'+str(instituto[3]))
        print("\t Codigo:"'\t'+str(instituto[0]))
    cod=input("digite el codigo del articulo que desea modificar")
    for intituto in cursor:
        if int(instituto[0])==int(cod):
            nombre=instituto[1]
            edad=instituto[2]
            dni=instituto[3]
            break
    nombre= input("Digite nuevo nombre o corrija" )
    edad=input("Digite nueva edad o corrija")
    dni= input("Digite nuevo dni o corrija" )
    sql = "UPDATE instituto set nombre ='"+nombre+"', edad='"+edad+"',dni='"+dni+"' where codigo = "+cod
    cursor.execute(sql)

    con.commit()
    con.close()
    print("")
    print("el archivo fue modificado exitoxamente-.......")
    input()
    menu()
def iliminar():
    con=sqlite3.connect("trabajo final.s3db")
    cursor=con.cursor()
    cursor.execute("select*from instituto ")
    for instituto in cursor:
        print("")
        print("\t Alumnos Agregados")
        print("\t------------------------")
        print("\t Nombre:"'\t'+str(instituto[1]))
        print("\t Edad:"'\t'+str(instituto[2]))
        print("\t DNI:"'\t'+str(instituto[3]))
        print("\t Codigo:"'\t'+str(instituto[0]))
    cod=input("digite el codigo  que desea iliminar")
    sql="delete from instituto where codigo="+cod
    cursor.execute(sql)
    con.commit()
    con.close()
    print("")
    print("el archivo fue iliminado exitoxamente-.......")
    input()
    menu()

menu()
