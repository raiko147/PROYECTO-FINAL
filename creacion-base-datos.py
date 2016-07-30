import sqlite3
import os,time
os.system('clear')
print (end="\tINSTITUTO DEL SUR AREQUIPA\nCreando base datos...")
con=sqlite3.connect("trabajo-final.s3db")

print("OK")
time.sleep(1)
os.system("clear")
cursor=con.cursor()
cursor.execute("CREATE TABLE registro(id integer primary key,nombre var(20) not null,"
               "apellidos var(20) not null,edad int(2) not null,dni int(8) not null,direccion var(30) not null,"
               "sexo var(1) not null,correo var(32) not null,especialidad var(60) not null,observaciones var(60));")
#cerrar coneccion
con.commit()
#creacion de tabla de pagos
cursor.execute("CREATE TABLE pagos(codigo recibo integer primary key, concepto var(60) not null,"
                "cantidad int(1) not null, nombre var(20));")
print(end="\tCerrando coneccion base datos... ")
con.close()
print("ok")
