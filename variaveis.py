import os


def var():
    try:
        x = int(input("digite uma variavel do tipo int\n"))

    except ValueError:
        os.system("clear")
        print("vc não digitou uma variavel do tipo int, tente novament")
        var()



    try:
        y = float(input("digite uma variavel do tipo float\n"))

    except ValueError:
        os.system("clear")
        print("vc não digitou uma variavel do tipo float, tente novamente")
        var()



    try:
        z = str(input("digite uma variavel do tipo str\n"))

    except ValueError:
        os.system("clear")
        print("vc não digitou uma variavel do tipo str, tente novamente")
        var()
        
        
    try:
        b = bool(input("digite uma variavel do tipo boleano\n"))

    except ValueError:
        os.system("clear")
        print("vc não digitou uma variavel do tipo boleano, tente novament")
        var()
    
    os.system("clear")


    print(type(x),x)
    print(type(y),y)
    print(type(z),z)
    print(type(b),b)


var()
