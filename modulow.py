
class matriculas:
    def __init__(self, nombre, apellidos, dni, direccion, area):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.area = area
        self.str = str
    '''def pronombres(self):
        texto = texto.title()
        texto = texto.split()
        print(texto)
        self.str, j = '', 0
        for i in texto:
            if i.isalpha():
                print(i)
                self.str += i+' '
                j +=1
        print()
        if len(texto) == j:
            return self.str[:-1]'''


    def Alumnos(self):
        return [self.nombre, self.apellidos, self.dni, self.direccion, self.area]

    '''def alphabetico_Pronombre(self, str): #sirve para ingrese de pronombres con espacios
        str = str.split()
        strConcatenado = ''
        j = 0
        for i in str:
            if i.isalpha():
                j+=1
                nombreConcatenado += i+' '
        if not len(nombre) == j:
            print('\tIngrese dato alfabetico')
        else: return nombreConcatenado[:-1]
        '''


'''seguridad de componentes autonomos por redes inalambricas.
    -Diseno software.

    -Perdida o saturacion.
proteccion datos.
politicas de seguridad.
    -nuevas tecnicas de programacion capaces de responder automaticamente a los ataques.
    -uso de nuevos interfaces poco propensos de fallos.
    -lenguaje de programacion bien identificada matematicamente..
sistemas de modulacion multiple.
configuraciones de antenas multiples.
sistemas de codificacion espacio tiempo multiples del estandar.'''