import sqlite3
import os,time
os.system('clear')
print (end="\tINSTITUTO DEL SUR AREQUIPA\nCreando base datos...")
con=sqlite3.connect("trabajo-final.db")

print("OK")
time.sleep(1)
os.system("clear")
cursor=con.cursor()
cursor.execute("CREATE TABLE registro(id integer primary key,nombre var(20) not null,"
               "apellidos var(20) not null,edad int(2) not null,dni int(8) not null,direccion var(30) not null,"
               "sexo var(1) not null,correo var(32) not null,especialidad var(60) not null,observaciones var(60));")
con.commit()
#crecion de tablas cursos
cursor.execute("CREATE TABLE cursos(codigo integer primary key,descripcion var(20) not null,"
               "tipo_curso int(1) not null, creditos int(1) not null, observaciones var(60));")
con.commit()
#creacion de tabla matriculas
cursor.execute("CREATE TABLE matriculas(codigo integer primary key, ciclo int(20) not null,"
                "semestre_academico int(1) not null, codigo_alumno int );")

con.commit()
#creacion de tabla pagos
cursor.execute("CREATE TABLE pagos(codigo_recibo integer primary key, concepto var(60) not null,"
                "cantidad int(1) not null, codigo_nombre var(20) );")

con.commit()
#creacion de tabla docentes
cursor.execute("CREATE TABLE docentes(codigo integer primary key, nombre var(20) not null,"
                "apellidos var(20) not null, edad int(2) not null, dni int(8) not null, direccion var(30) not null,"
                "sexo var(1) not null, correo var(32) not null, especialidad var(60) not null, observaciones var(60));")

con.commit()
#creacion de tabla administrativos
cursor.execute("CREATE TABLE administrativos(codigo integer primary key,nombre var(20) not null,"
               "apellidos var(20) not null,edad int(2) not null,dni int(8) not null,direccion var(30) not null,"
               "sexo var(1) not null,correo var(32) not null,especialidad var(60) not null,observaciones var(60));")
con.commit()                
#cerrar coneccion
print(end="\tCerrando coneccion base datos... ")
con.close()
print("ok")
