archivo = "prueba.txt"
try:
    f = open(archivo, "r")
except IOError:
    f.close()
    exit()

contenido = f.readlines()
f.close()

lista = []
lista_final = []

for numero in contenido:
    lista += numero.split()
lista.sort()
set_lista = set(lista)
set_lista = list(set_lista)
set_lista.sort()
print
"Valor:Ocurrencias"
for numero in set_lista:
    lista_final.append((lista.count(numero), numero))

lista_final.sort(reverse=True)
print(lista_final)