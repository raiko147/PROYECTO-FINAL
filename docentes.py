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
    nombre=input(("Ingrese su Nombre: "))
    while(not verificar(nombre)):
        print("Ingrese su nombre correctamente: ")
        nombre=input(("Ingrese su Nombre: "))
    
    apellidos=input("Ingrese sus Apellidos: ")
    while(not verificar(apellidos)):
        print("Ingrese sus Apellidos  correctamente: ")
        apellidos=input("Ingrese sus Apellidos: ")
    while(1):
        try:
            print("Ingrese su Edad")
            edad=input()
            edad=int(edad)
            while(edad<0 or edad>170):
                print("edad incorrecta vuelva intentar...: ")
                edad=input()
                edad=int(edad)
            break
        except ValueError:
            print("ingrese correctamente ...: ")
    
    while(1):
        try:
            print("Ingrese su Dni")
            dni=input()
            dni=int(dni)
            while(len(str(dni))!=8):
                dni=int(input("Ingrese dni de 8 digitos"))
            break
        except ValueError:
            print("Error...!!!Ingrese correctamente su DNI")
    print("Ingrese su Direccion")
    direccion=input()
    
    data_sexo=""
    while(1):
        try:
            print("Ingrese su Sexo F/M: ")
            sexo=input()
            sexo=upper(str(sexo))
            while(len(str(sexo))!=1):
                print("Ingrese solo un caracter F O M : ")
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
    print("ingrese su correo")
    correo=input()
    print("ingrese su especialidad")
    especialidad=input()
    while(not verificar(especialidad)):
        especialidad=input("ingrese su especialidad corretamente: ")
    print("ingrese sus observaciones")
    observaciones=input()
    while(not verificar(observaciones)):
        observaciones=input("ingrese sus observaciones correctamente: ")
    con=sqlite3.connect("trabajo-final.s3db")
    cursor=con.cursor()
    cursor.execute("insert into instituto (nombre,apellidos,edad,dni,direccion,sexo,correo,especialidad) values ('"+nombre+"','"+apellidos+"','"+edad+"','"+str(dni)+"','"+direccion+"','"+str(sexo)+"','"+correo+"','"+especialidad+"','"+observaciones+"')")
    con.commit()
    con.close()
    time.sleep(3)
    menu()

def menu():
    os.system("clear")
    print("-----------------------------------------------------------------------------")
    print("\tBase de datos de docentes  del Instituto del Sur\n")
    print("\t1.- Agregar datos del docente")
    print("\t2.- Reporte del docente")
    print("\t3.- Modificar datos del Docente")
    print("\t4.- Eliminar datos del Docente")
    print("\t5.- Salir")
    print("-----------------------------------------------------------------------------")
    while(1):
        try:
            print("Ingrese una opcion")
            entrada=input()
            entrada=int(entrada)
            while(entrada<0 or entrada>5):
                print("ingrese correctamente la opcion")
                entrada=input()
                entrada=int(entrada)
            break
        except ValueError:
            print("ingrese correctamente una opcion valida")
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
    con=sqlite3.connect("trabajo-final.s3db")
    cursor=con.cursor()
    cursor.execute("select*from docentes ")
    for docentes in cursor:
        print("")
        print("\t docentes agregados")
        print("\t------------------------")
        print("\t Nombre:"'\t'+str(docentes[1]))
        print("\t Apellidos:"'\t'+str(docentes[2]))
        print("\t Edad:"'\t'+str(docentes[3]))
        print("\t Dni:"'\t'+str(docentes[4]))
        print("\t Direccion:"'\t'+str(docentes[5]))
        print("\t Sexo:"'\t'+str(docentes[6]))
        print("\t Correo:"'\t'+str(docentes[7]))
        print("\t Especialidad:"'\t'+str(docentes[8]))
        print("\t Observaciones:"'\t'+str(docentes[9]))
        print("\t Codigo:"'\t'+str(docentes[0]))
    con.commit()
    con.close()
    time.sleep(3)
    menu()
def modificar():
    con=sqlite3.connect("trabajo-final.s3db")
    cursor=con.cursor()
    cursor.execute("select*from docentes ")
    for docentes in cursor:
        print("")
        print("\t docentes agregados")
        print("\t------------------------")
        print("\t Nombre:"'\t'+str(docentes[1]))
        print("\t Apellidos:"'\t'+str(docentes[2]))
        print("\t Edad:"'\t'+str(docentes[3]))
        print("\t Dni:"'\t'+str(docentes[4]))
        print("\t Direccion:"'\t'+str(docentes[5]))
        print("\t Sexo:"'\t'+str(docentes[6]))
        print("\t Correo:"'\t'+str(docentes[7]))
        print("\t Especialidad:"'\t'+str(docentes[8]))
        print("\t Observaciones:"'\t'+str(docentes[9]))
        print("\t Codigo:"'\t'+str(docentes[0]))
    cod=input("digite el codigo del Docente que desea modificar")
    for docentes in cursor:
        if int(docentes[0])==int(cod):
            nombre=docentes[1]
            apellidos=docentes[2]
            edad=docentes[3]
            dni=docentes[4]
            direccion=docentes[5]
            sexo=docentes[6]
            correo=docentes[7]
            especialidad=docentes[8]
            observaciones=docentes[9]
            break
    nombre= input("Digite nuevo nombre o corrija" )
    apelldios=input("Digite nuevo apellido o corrija")
    edad=input("Digite nueva edad o corrija")
    dni= input("Digite nuevo dni o corrija" )
    direccion=input("Digite nueva direccion o corrija")
    sexo=input("Digite nuevo sexo o modifique")
    correo=input("Digite nuevo correo o modifique")
    especialidad=input("Digite nueva especialidad o modifique")
    observaciones=input("Digire nuevas observaciones o modifique")
    sql = "UPDATE docentes set nombre ='"+nombre+"',apellidos ='"+apellidos+"', edad='"+edad+"',dni='"+srt(dni)+"',direccion ='"+direccion+"',sexo ='"+str(sexo)+"',correo ='"+correo+"',especialidad ='"+especialidad+"',observaciones ='"+observaciones+"' where codigo = "+cod
    cursor.execute(sql)

    con.commit()
    con.close()
    print("")
    print("el archivo fue modificado exitoxamente-.......")
    input()
    menu()
def iliminar():
    con=sqlite3.connect("trabajo-final.s3db")
    cursor=con.cursor()
    cursor.execute("select*from docentes ")
    for docentes in cursor:
        print("")
        print("\t docentes agregados")
        print("\t------------------------")
        print("\t Nombre:"'\t'+str(docentes[1]))
        print("\t Apellidos:"'\t'+str(docentes[2]))
        print("\t Edad:"'\t'+str(docentes[3]))
        print("\t Dni:"'\t'+str(docentes[4]))
        print("\t Direccion:"'\t'+str(docentes[5]))
        print("\t Sexo:"'\t'+str(docentes[6]))
        print("\t correo:"'\t'+str(docentes[7]))
        print("\t Especialidad:"'\t'+str(docentes[8]))
        print("\t Observaciones:"'\t'+str(docentes[9]))
        print("\t Codigo:"'\t'+str(docentes[0]))
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

