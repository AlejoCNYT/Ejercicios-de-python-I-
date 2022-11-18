def area_trapecio():
    print("Este programa realiza el cálculo de área de un trapecio")
    b = float(input("Ingrese la base menor: "))
    B = float(input("Ingrese la base mayor: "))
    h = float(input("Ingrese la altura: "))
    area = float(((b + B) * h)/2)
    print("El área del trapecio con base menor ", b, "base mayor ", B, "y altura ", h, "es ", area)
    print("¡Gracias por utilizar nuestra calculadora de área de trapecio!.")

area_trapecio()
