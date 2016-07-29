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
