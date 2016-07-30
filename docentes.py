import os
import sys,time
import sqlite3

def verificar(a):
    for c in a:
        if(ord(c)<65 or ord(c)>90 ) and (ord(c)<97 or ord(c)>122) and (ord(c)!=32):
            return False
    return True

def nuevo():
    os.system("cls")
    print("ingrese su nombre")
    nombre=input()
    while(not verificar(nombre)):
        nombre=input("ingrese su nombre correctamente: ")
    while(1):
        try:
            print("ingrese su edad")
            edad=input()
            edad=int(edad)
            while(edad<0 or edad>170):
                print("edad incorrecta vuelv intentar...: ")
                edad=input()
                edad=int(edad)
            break
        except ValueError:
            print("ingrese correctamente ...: ")
    print("ingrese sus Apellidos Completos")
    apellidos=input()
    while(not verificar(apellidos)):
        apellidos=input("ingrese sus Apellidos  correctamente: ")
    while(1):
        try:
            print("ingrese su Edad")
            edad=input()
            edad=int(edad)
            while(edad<0 or edad>170):
                print("edad incorrecta vuelv intentar...: ")
                edad=input()
                edad=int(edad)
            break
        except ValueError:
            print("ingrese correctamente ...: ")
    
    while(1):
        try:
            print("ingrese su dni")
            dni=input()
            dni=int(dni)
            while(len(str(dni))!=8):
                dni=int(input("ingrese dni de 8 digitos"))
            break
        except ValueError:
            print("error ingrese correctamente su dni")
    print("ingrese su Direccion")
    direccion=input()
    
    data_sexo=""
    while(1):
        try:
            print("Ingrese su Sexo F/M: ")
            sexo=input()
            sexo=str(sexo)
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
    while(not verificar(especialidad):
        especialidad=input("ingrese su especialidad corretamente: ")
    print("ingrese sus observaciones")
    observaciones=input()
    while(not verificar(observaciones):
        observaciones=input("ingrese sus observaciones correctamente: ")
    con=sqlite3.connect("trabajo-final.s3db")
    cursor=con.cursor()
    cursor.execute("insert into instituto (nombre,apellidos,edad,dni,direccion,sexo,correo,especialidad) values ('"+nombre+"','"+apellidos+"','"+edad+"','"+str(dni)+"','"+direccion+"','"+str(sexo)+"','"+correo+"','"+especialidad+"','"+observaciones+"')")
    con.commit()
    con.close()
    time.sleep(3)
    menu()

def menu():
    os.system("cls")
    print("Base de datos del Instituto del Sur")
    print("")
    print("1.- agregar datos del docente")
    print("2.- Reporte del docente")
    print("3.- modificar datos del docente")
    print("4.- iliminar datos del docente")
    print("5.- salir")
    while(1):
        try:
            print("ingrese una opcion")
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
        print("\t nombre:"'\t'+str(docentes[1]))
        print("\t apellidos:"'\t'+str(docentes[2]))
        print("\t edad:"'\t'+str(docentes[3]))
        print("\t dni:"'\t'+str(docentes[4]))
        print("\t direccion:"'\t'+str(docentes[5]))
        print("\t sexo:"'\t'+str(docentes[6]))
        print("\t correo:"'\t'+str(docentes[7]))
        print("\t especialidad:"'\t'+str(docentes[8]))
        print("\t observaciones:"'\t'+str(docentes[9]))
        print("\t codigo:"'\t'+str(docentes[0]))
    con.commit()
    con.close()
    input()
    menu()
def modificar():
    con=sqlite3.connect("trabajo-final.s3db")
    cursor=con.cursor()
    cursor.execute("select*from docentes ")
    for docentes in cursor:
        print("")
        print("\t docentes agregados")
        print("\t------------------------")
        print("\t nombre:"'\t'+str(docentes[1]))
        print("\t apellidos:"'\t'+str(docentes[2]))
        print("\t edad:"'\t'+str(docentes[3]))
        print("\t dni:"'\t'+str(docentes[4]))
        print("\t direccion:"'\t'+str(docentes[5]))
        print("\t sexo:"'\t'+str(docentes[6]))
        print("\t correo:"'\t'+str(docentes[7]))
        print("\t especialidad:"'\t'+str(docentes[8]))
        print("\t observaciones:"'\t'+str(docentes[9]))
        print("\t codigo:"'\t'+str(docentes[0]))
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
    sql = "UPDATE docentes set nombre ='"+nombre+"',apellidos ='"+apellidos+"', edad='"+edad+"',dni='"+dni+"',direccion ='"+direccion+"',sexo ='"+correo+"',nombre ='"+correo+"',nombre ='"+especialidad+"',nombre ='"+observaciones+"' where codigo = "+cod
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
        print("\t nombre:"'\t'+str(docentes[1]))
        print("\t apellidos:"'\t'+str(docentes[2]))
        print("\t edad:"'\t'+str(docentes[3]))
        print("\t dni:"'\t'+str(docentes[4]))
        print("\t direccion:"'\t'+str(docentes[5]))
        print("\t sexo:"'\t'+str(docentes[6]))
        print("\t correo:"'\t'+str(docentes[7]))
        print("\t especialidad:"'\t'+str(docentes[8]))
        print("\t observaciones:"'\t'+str(docentes[9]))
        print("\t codigo:"'\t'+str(docentes[0]))
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

