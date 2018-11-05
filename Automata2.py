import string
#Brian Reyes A01633401
def automata2(cadena):
    estado=0
    for c in cadena:
        estado=trans(c,estado)
    print(estado)
    if(estado==2):
        print("La cadena es un n�mero natural")
        return None
    if(estado==4):
        print("La cadena es un n�mero Octal")
        return None
    elif(estado==10 or estado==7):
        print("La cadena es un n�mero de punto flotante")
        return None
    elif(estado==11):
        print("La cadena es un Hexadecimal")
        return None
    elif(estado==1):
        print("Natural")
        return None
    else:
        print("ERROR!")
        return None
    
def trans(c,estado):
    if(estado==0):
        if(c=="0"):
            return 1
        elif(c in string.digits):
            return 2
        else:
            return 8
    elif(estado==1):
        if(c.lower()=="x"):
            return 3
        elif(c in string.octdigits):
            return 4
        elif(c=="8" or c=="9"):
            return 5
        elif(c=="."):
            return 6
        else:
            return 8
    elif(estado==2):
        if(c in string.digits):
            return 2
        elif(c =="."):
            return 6
        else:
            return 8
    elif(estado==3):
        if(c in string.hexdigits):
            return 11
        else:
            return 8
    elif(estado==4):
        if(c in string.octdigits):
            return 4
        elif(c=="8" or c=="9"):
            return 5
        elif(c=="."):
            return 6
        else:
            return 8
    elif(estado==5):
        if(c in string.digits):
            return 5
        elif(c=="."):
            return 6
        else:
            return 8
    elif(estado==6):
        if(c in string.digits):
            return 7
        else:
            return 8
    elif(estado==7):
        if(c in string.digits):
            return 7
        elif(c.lower()=="e"):
            return 9
        else:
            return 8
    elif(estado==8):
        return 8
    elif(estado==9):
        if(c=="+" or c=="-" or c in string.digits):
            return 10
        else:
            return 8
    elif(estado==10):
        if(c in string.digits):
            return 10
        else:
            return 8
    elif(estado==11):
        if(c in string.hexdigits):
            return 11
        else:
            return 8
        
        
#Correctos
automata2("10.0078")
automata2("1.23e-25")
automata2("0170")
automata2("0xFA07B")
automata2("245000")
automata2("000000354")
#Incorrectos
automata2("1.0.34")
automata2("1.23e.34")
automata2("0190")
automata2("000xFB7A")
automata2("0890")
automata2("192.168.0.1")
