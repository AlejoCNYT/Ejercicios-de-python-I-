'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Apellidos Nombre

Lenguaje: Python
Referencia: Ejercicios No. 3. Python básico.
            Estructuras de control condicionales if y while.

4.  Pedir 2 puntos para cada una de n rectas y hallar y escribir su pendiente. 
    Ejemplo. n igual a 3
    Puntos dados:
    (10.0, 2.0), (4.0, 5.0) Pendiente = 0.5
    (3.0, 0.0), (0.0, 3.0) Pendiente = -1
    (5.0, 1.5), (-2.0, 1.5) Pendiente = 0
    (-1.0, 1.5), (-1.0, -3.5) Pendiente indefinida

Datos de entrada: n, x1, x2, y1, y2
Datos de salida: m
'''

def main():
    print("Cálculo de las pendientes de n coordenadas.")
    n = int ( input("n = "))
    cont = 1
    while cont <= n:
        x1 = float ( input ("x1 = ") )
        y1 = float ( input ("y1 = ") )
        x2 = float ( input ("x2 = ") )
        y2 = float ( input ("y2 = ") )
        if x2 - x1 != 0 and y2 - y1 != 0:
            print("La pendiente de (", x1, ",", y1, ") (", x2, ",", y2, ") es", (y2 - y1) / (x2 - x1))
        else:
            print("Pendiente indefinida.")
    print("\nFin.")

main()


    

