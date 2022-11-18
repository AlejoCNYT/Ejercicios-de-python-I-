'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Apellidos Nombre

Lenguaje: Python
Referencia: Ejercicios No. 3. Python básico.
            Estructuras de control condicionales if y while.

5.  Escribir los múltiplos de p que pertenecen al intervalo [a, b].

    Ejemplo. p igual a 7, intervalo [37, 80]

    Los múltiplos de 7 que pertenecen al intervalo [37, 80] son 42 49 56 63 70 77

Datos de entrada: p, a, b
Datos de salida: m
'''


def main():
    print("Cálculo de los múltiplos de p, en un intervalo dado.")
    p = int ( input ("p = ") )
    print("Por favor, digite los puntos del intervalo [a,b]: ")
    a = int ( input ("a = ") )
    b = int ( input ("b = ") )
    cont = 1
    m = a - (a % p)
    m = m + p
    print("Los múltiplos de", p, "que pertenecen al intervalo [", a, ",", b, "] son ")
    while m <= b:
        print(m)
        m = m + p

main()
    
