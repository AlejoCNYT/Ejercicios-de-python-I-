'''
Ejercicio 3.2 Escribir los pares que pertenecen a [1, límite] y calcular y escribir su suma.
Datos de entrada: límite
Datos de salida: suma, pares
'''

def suma_pares():
    print("Yo le digo cuáles pares hay hasta un ñimite ingresado...")
    suma = 0
    par = 2
    lim = int(input("Diga el límite: "))
    while par <= lim:
        print(par)
        suma = suma + par
        par = par + 2
        
    print("La suma de los pares es:", suma)
    print("Fin.")
    
suma_pares()
