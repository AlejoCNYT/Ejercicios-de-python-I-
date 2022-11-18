'''
Ejercicio3.1
Datos de entrada: a, b, c, d, operacion
Datos de salida: Resultado
'''

def opera_numeros():
    print("Dígame cuatro números y yo los opero matemáticamente...")
    a = int(input("Ingrese el numerador del primer fraccionario: "))
    b = int(input("Ingrese el denominador del primer fraccionario: "))
    c = int(input("Ingrese el numerador del segundo fraccionario: "))
    d = int(input("Ingrese el denominador del segundo fraccionario: "))
    print("Seleccione 1 para adición, 2 para sustracción, 3 para producto y 4 para cociente.")
    op = int(input("Ingrese el código de la operación: "))

    if b != 0 and d != 0:
        if op == 1:
            print("La sustracción de los números", a, "/", b, "-", c, "/", d, "=", (a * d) + (c * b), "/", b * d)
        else:
            if op == 2:
                print("La sustracción de los números", a, "/", b, "-", c, "/", d, "=", (a * d) - (c * b), "/", b * d)
            else:
                if op == 3:
                    print("El producto de los números", a, "*", c, "/", b, "*", d, "=", (a * c), "/", (b * d))
                else:
                    if op == 4:
                        print("El producto de los números", a, "/", c, "/", b, "/", d, "=", (a * d), "/", (c * b))
                    else:
                        print("Esta operación no está definida.")
    else:
        print("Esta operación no está definida.")
    print("Fin.")

opera_numeros()
                        
                        
        
