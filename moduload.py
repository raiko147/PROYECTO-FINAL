# Modulo AD
def title(n,texto):
    b = "-"*80
    print("{0}\nPrograma {1}: {2}\n{0}" .format(b,n,texto))
def interes_compuesto(m,i,t):
    cf = m*(1+i)**t
    return cf
def notas(n,b):
    nota = []
    i=1
    while i<=n:
        while True:
            try:
                a = float(input("Ingrese su nota {0} : " .format(i)))
                if a <= b and a >= 0 :
                    nota.append(a)
                    break
                else:
                    print("no se encuentra en el rango de notas")
            except ValueError:
                print("ERROR!!!")
        i+=1
    return nota
def promedio_lista(n):
    a=0
    for i in n:
        a = a + i
    a/=len(n)
    return a
def pago_semanal(h):
    if h > 40:
        s = (h-40)*20+(40*16)
    else:
        s = h*16
    return s
def escribir_edades(n):
    num = []
    for i in range (0,n):
        while True:
            try:
                a = float(input("ingrese promedios de edades del salon {0}: " .format(i+1)))
                num.append(a)
                break
            except ValueError:
                print("ERROR!!!")
        
    return num
def escribir_numeros(n):
    num = []
    for i in range(0, n):
        while True:
            try:
                a = float(input("ingrese numero {0}: ".format(i + 1)))
                num.append(a)
                break
            except ValueError:
                print("ERROR!!!")

    return num
def posicion_equipo(n):
    equipos = []
    for i in range (0,n):
        while True:
            try:
                a = input("equipo en la posicion {0}: " .format(i+1))
                equipos.append(a)
                break
            except ValueError:
                print("ERROR!!!")

    return equipos
