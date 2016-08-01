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
    con=sqlite3.connect("trabajo final.s3db")
    cursor=con.cursor()
    cursor.execute("insert into instituto (nombre,edad,dni) values ('"+nombre+"','"+str(edad)+"','"+str(dni)+"')")
    con.commit()
    con.close()
    time.sleep(3)
    menu()

def menu():
    os.system("cls")
    print("     ****** ***   ** ******* ******** ****** ******** **  ** ******** ******")
    print("       **   ****  ** ***        **      **      **    **  **    **    **  **")
    print("       **   ** ** ** *******    **      **      **    **  **    **    **  **")
    print("       **   **  ****     ***    **      **      **    **  **    **    **  **")
    print("     ****** **   *** *******    **    ******    **    ******    **    ******")
    print(" ")
    print(" ")
    print("      ******** ****** **       ********  ***   ***  ********* ")
    print("        **  ** **     **       ***       ***   ***  ***   *** ")
    print("        **  ** ****** **       ***       ***   ***  ********* ")
    print("        **  ** **     **       ********  ***   ***  ******    ")
    print("      ******** ****** ******        ***  ***   ***  ********* ")
    print("                                    ***  *********  ***   *** ")
    print("                               ********  *********  ***   *** ")
    print("--------------------------------------------------")
    print("\t BASE DE DATOS DEL INSTITUTO DEL SUR")
    print("")
    print("1.- AGREGAR DATOS DEL ALUMNO")
    print("2.- REPORTE DEL ALUMNO")
    print("3.- MODIFICAR DATOS DEL ALUMNO")
    print("4.- ELIMINAR DATOS DEL ALUMNO")
    print("5.- SALIR")
    print("--------------------------------------------------")
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
    con=sqlite3.connect("trabajo final.s3db")
    cursor=con.cursor()
    cursor.execute("select*from instituto ")
    for instituto in cursor:
        print("")
        print("\t ALUMNOS AGREGADOS")
        print("\t------------------------")
        print("\t NOMBRE:"'\t'+str(instituto[1]))
        print("\t EDD:"'\t'+str(instituto[2]))
        print("\t DNI:"'\t'+str(instituto[3]))
        print("\t CODIGO:"'\t'+str(instituto[0]))
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
        print("\t ALUMNOS AGREGADOS")
        print("\t------------------------")
        print("\t NOMBRE:"'\t'+str(instituto[1]))
        print("\t EDAD:"'\t'+str(instituto[2]))
        print("\t DNI:"'\t'+str(instituto[3]))
        print("\t CODIGO:"'\t'+str(instituto[0]))
    cod=input("DIGITE EL CODIGO DEL ALUMNO PARA MODIFICAR")
    for intituto in cursor:
        if int(instituto[0])==int(cod):
            nombre=instituto[1]
            edad=instituto[2]
            dni=instituto[3]
            break
    nombre= input("Digite nuevo nombre o corrija" )
    edad=input("Digite nueva edad o corrija")
    dni= input("Digite nuevo dni o corrija" )
    sql = "UPDATE instituto set nombre ='"+nombre+"', edad='"+str(edad)+"',dni='"+str(dni)+"' where codigo = "+cod
    cursor.execute(sql)

    con.commit()
    con.close()
    print("")
    print("El archivo fue modificado exitoxamente-.......")
    input()
    menu()
def iliminar():
    con=sqlite3.connect("trabajo final.s3db")
    cursor=con.cursor()
    cursor.execute("select*from instituto ")
    for instituto in cursor:
        print("")
        print("\t ALUMNOS AGREGADOS")
        print("\t------------------------")
        print("\t NOMBRE:"'\t'+str(instituto[1]))
        print("\t EDAD:"'\t'+str(instituto[2]))
        print("\t DNI:"'\t'+str(instituto[3]))
        print("\t CODIGO:"'\t'+str(instituto[0]))
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
