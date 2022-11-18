def vol_cilindro():
    print("Este programa, calcula el volumen de un cilíndro de radio (r) y altura (h), determinados.")
    pi = 3.1415
    r = float(input("Ingrese el radio (r): "))
    h = float(input("Ingrese la altura (h): "))
    volCi = round(h * (2 * pi * r ** 2), 3)
    print("El volumen del cilíndro de radio", r, "y altura", h, "es aproximádamente:", volCi)
    print("¡Vuelva pronto!")
    
vol_cilindro()
