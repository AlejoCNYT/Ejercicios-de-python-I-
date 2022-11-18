'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Apellidos Nombre

Lenguaje: Python
Referencia: Ejercicios No. 3. Python básico.
            Estructuras de control condicionales if y while.

6.  Escribir los números pares que pertenecen al intervalo [a, b], a y b enteros, en orden descendente.

    Ejemplo. Intervalo [28, 39]

    Los pares que pertenecen al intervalo [28, 39], en orden descendente, son: 38 36 34 32 30 28

Datos de entrada: 
Datos de salida: 
'''

def main():
    print("Cálculo de los pares en un intervalo dado.")
    print("Por favor, digite los valores enteros del intervalo [a,b]: ")
    a = int ( input ("a = ") )
    b = int ( input ("b = ") )
    m = b - (b % 2)
    print("Los pares que pertenecen al intervalo [", a, ",", b, "] son ")
    while m >= a and m <= b:
        print(m)
        m = m - 2

main()
