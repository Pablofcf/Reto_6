#El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.

def personas_finales(c: int, d: int) -> int:
    return c * (2 ** d)

if __name__ == "__main__":
    d = int(input("Dias que pasaron: "))
    c = int(input("Personas iniciales contaminadas: "))
    
    if d > 0 and c > 0:
        personas_contaminadas = personas_finales(c, d)
        print("Se contaminaron:", personas_contaminadas, "personas en", d, "días.")
    else:
        print("No se pueden tener días o personas negativas.")