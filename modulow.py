class matriculas:
    def __init__(self, nombre, apellidos, dni, direccion, area):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.area = area
        self.str = str

    def Alumnos(self):
        return [self.nombre, self.apellidos, self.dni, self.direccion, self.area]

    '''def ingresoAlfabetico(self):
        self.nombre , self.j= '', 0
        while not (len(self.nombre) == j and j>0):
            self.nombre = str(input('Ingrese Nombres Completos: \n'))
            self.nombre = nombre.title()
            self.nombre = nombre.split()
            self.nombreConcatenado = ''
            self.j = 0
            for i in self.nombre:
                if i.isalpha():
                    self.j+=1
                    self.nombreConcatenado += i+' '
            if not (len(self.nombre) == j and j>0):
                print('\tIngrese nombre alfabetico o nombre aceptable')
            self.nombreConcatenado = self.nombreConcatenado[:-1]
        return self.nombreConcatenado   '''

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
                    reporte("administrativos","codigo")
                #modificar datos

                elif opcionElegido == "3":
                    print("\tModificacion de datos")
                    modificar("administrativos","codigo")
                #eliminar datos
                elif opcionElegido == "4":
                    print("\tEliminar registro")
                    codigo = tablaCodigo("administrativo","codigo")
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


