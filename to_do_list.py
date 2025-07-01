td = []
# lista de todas las tareas

th = input("cuantas tareas vas a hacer hoy?:")
# pregunta cuantas tareas haras hoy
for i in range(int(th)):
    t = input("tarea:")
    td.append(t)
# cuenta todas las tareas
print(td)
trco = []
while len(trco) != len(td):
    trc = input("tarea que acabas de completar:")
    if len(trco) != len(td):
        print("ya creo que es hora de dormir hasta mañana.")
        break
    else:
        pass
# introduce una condicion que si se cumple termina el codigo
