def pide_ent_pos_msj(mensaje):

    num = 0
    while num <= 0:
        num = int(input(mensaje))
    return num

def main():
    
    edad = pide_ent_pos_msj("Cantidad de casas: ")
    print(edad)
    print("Fin.")
    
main()
