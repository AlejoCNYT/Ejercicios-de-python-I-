def intercambio_cont():
    print("Este programa sustituye dos valores ingresados previamente")
    val1 = int(input("Ingrese el valor 1: "))
    val2 = int(input("Ingrese el valor 2: "))

    print("El valor 1 ingresado es", val1, "y el valor 2 ingresado es", val2)

    sust = val1
    val1 = val2
    val2 = sust

    print("El nuevo valor 1 es", val1, "y el nuevo valor 2 es", val2)
    print("¡Feliz día!")
    
intercambio_cont()
