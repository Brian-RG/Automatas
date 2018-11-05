import string
#Brian Reyes A01633401
def automata(cadena):
    estado=0
    reservadas= ["program","var","begin","end","if","then","else"]
    if(cadena not in reservadas):
        for c in cadena:
            estado=transicion(c,estado)
        print(estado)
        if(estado==3):
            print("La cadena es un identificador")
            return None
    print("Error! No es un identificador!!")
    return None

def transicion(c,estadoactual):
    if(estadoactual==0):
        if(c in string.ascii_letters or c=="_"):
            return 1
        elif(c in string.digits):
            return 2
        else:
            return 1
    elif(estadoactual==1):
        if(c in string.ascii_letters):
            return 3
        elif(c =="_"):
            return 1
        elif(c in string.digits):
            return 1
        else:
            return 2
    elif(estadoactual==2):
        if(c in string.ascii_letters or c=="_"):
            return 2
        elif(c in string.digits):
            return 2
        else:
            return 2
    elif(estadoactual==3):
        if(c in string.ascii_letters or c=="_"):
            return 3
        elif(c in string.digits):
            return 3
        else:
            return 2


automata("_3__a")
