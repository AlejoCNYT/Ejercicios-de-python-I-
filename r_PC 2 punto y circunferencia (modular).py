'''
Universidad Escuela Colombiana de Ingeniería
Algoritmos y programación (AYPR)
Profesora: Ingeniera Patricia Salazar Perdomo

Estudiante: Acero Varela Daniel Alejandro

Lenguaje: Python
Referencia: Prueba corta No. 2. Estructura de control condicional if. (versión modular)

            Construya un programa en Python (una función) que solucione el siguiente problema:

            Pedir al usuario el radio y las coordenadas h,k del centro de una circunferencia (C(h,k)).
            También debe solicitar las coordenadas x,y de un punto (P(x,y)). 

            Averiguar:
            - Si el punto P pertenece a la circunferencia
            - En qué cuadrante (I, II, III o IV) está el punto P o si está sobre uno de los ejes coordenados.
 
            La ecuación de una circunferencia con centro de coordenadas h,k (C(h,k)) es:

            (x-h)^2+(y-k)^2=r^2

            VERSIÓN MODULAR.
            Datos de entrada: r, h, k, x, y
            Datos de salida: pertenencia, plano
'''

def pertenece(radio, h, k, x, y):

    dist_c_p = ((x - h) ** 2 + (y - k) ** 2) ** 0.5
    if x != 0 and y != 0:
        if x > 0 and y > 0:
            cuadr = "en el cuadrante I."
        else:
            if x < 0 and y > 0:
                cuadr = "en el cuadrante II."
            else:
                if x < 0 and y < 0:
                    cuadr = "en el cuadrante III."
                else:
                    if x > 0 and y < 0:
                        cuadr = "en el cuadrante IV."
                    else:
                        cuadr = "sobre los ejes coordenados."
    else:
        cuadr = "r_PC 2 punto y circunferencia.py"
    print ("\nA la circunferencia de radio", radio, "y centro C (", h, ",", k, ")", end =" ")
    if dist_c_p > radio:
        cuadr = "no."
    return cuadr

def punto_mensaje(mensaje):

    print(mensaje)
    x = float ( input ( "abscisa = " ) )
    y = float ( input ( "ordenada = " ) )
    return x, y
    
def main():

    print ("\nIngrese el radio y las coordenadas del centro de una circunferencia (C(h,k)),")
    print ("así como las coordenadas de un punto (P(x,y)).")
    print ("Le diré si el punto pertenece a la circunferencia y en qué cuadrante (I, II, III o IV)")
    print ("está o si está sobre uno de los ejes coordenados.")

    radio = float (input ("\nRadio de la circunferencia = "))    

    h, k = punto_mensaje("\nCoordenadas del centro de la circunferencia C(h,k)")
    x, y = punto_mensaje("\nCoordenadas del punto P(x,y)")
        
    clasifica = pertenece(radio, h, k, x, y)
    print("\nDicho punto está", clasifica)
    print("\nFin.")
    
main()
