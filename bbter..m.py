from funciones import marcaD
from funciones import ageC
from funciones import suma
from funciones import pal
marcaD()

sesionU = ""
while not sesionU == "bokoserv" and not sesionU == "09273618":
    if sesionU != "":
        print("acceso denegado")
    sesionU = input("user:")
    

print("access garanted")
prompt = ""
while not prompt == "finish":
    prompt = input("j..ggbr:0:")
    if prompt == "git":
        f1 = input("folder 1:")
        if f1 == "open":
            print("proxima informacion")
    
        f2 = input("folder 2:")
        if f2 == "open":
            print("proxima informacion")
    
        f3 = input("folder 3:")
        if f3 == "open":
            print("profile number daniel:09273618")
            print("profile number jose:13580090")
        
        elif prompt == "pull serv 1":
            iveracion = input("yon35:")
        if iveracion == "dealing zones":
            print("coliseo")
            print("parque")
            print("LOJA")
            print("nada por ahora")
        elif iveracion == "recetasC":
           print("recetas raras de cafe que daniel invento")
           print("nada por ahora")
        elif iveracion == "actualversion":
            print("actualVersion:0,23")
    elif prompt == "finish session":
        break 
    elif prompt == "profile":
        indprofile = input("profile number:")
        if indprofile == "09273618":
           print("daniel:admin")
           print("numberProfile:09273618")
        elif indprofile == "13580090":
           print("jose:visadmin")
           print("numberProfile:13580090")
        else:
            print("this user does not exist")

    elif prompt == "calculator":
        suma = '+'
        resta = '-'
        multiplicacion = '*'
        division = '/'
        operacion = input('operacion + - * /:')
        operador1 = input('operador1:')
        operador2 = input('operador2:')
        if operacion == suma:
            resultado = int(operador1) + int(operador2)
            print(resultado)
        elif operacion == resta:
            resultado1 = int(operador1) - int(operador2)
            print(resultado1)
        elif operacion == multiplicacion:
            resultado2 = int(operador1) * int(operador2)
            print(resultado2)
        elif operacion == division:
            resultado3 = int(operador1) / int(operador2)
            print(resultado3)
        else:
            print('operacion incorrecta')
    elif prompt == "userslist":
        user = ['daniel','jose','marco','pato']
        for users in user:
            print("user:" ,users, )
    elif prompt == "help":
        print("COMMANDS")
        print("parlel")
    
        print("git")
        print("help")
        print("pull serv 1")
        print("userslist")
        print("profile")
        print("finish session")
        print("func")
        print("calculator")
    elif prompt == "func":
        func = input("func1:")
        if func == "CDE":
            ageC()
        elif func == "ss":
            suma()
        elif func == "palab":
            pal()
    elif prompt == "top secret":
        ir = input("password%")
        if ir == "09Fgjhh00ox{\/|\/}":
            print("00access granted00")
            print("")
        else:
            print("acceso denegado")
    elif prompt == "parlel":
        from funciones import paralelogramos
        paralelogramos()

            