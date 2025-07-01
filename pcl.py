invitados = []
numero_invitados = input("cuantos invitados iran a la fiesta de hoy?:")
for ni in range(int(numero_invitados)):
    invitado2 = input("nombre del invitado:")
    invitados.append(invitado2)
print("estos son todos los invitados", invitados)

llegados = []
while len(llegados) != len(invitados):
    iqadll = input("invitado que acaba de llegar:")
    if iqadll in invitados:
        print("si esta en la lista")
        llegados.append(iqadll)
        if len(llegados) == len(invitados):
            print("todos han llegado ya es hora de comenzar la fiesta")
        else:
            pass
    else:
        print("no se de quien me hablas")
