#Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

billete: int

def panes_totales(p: int) -> int:
    return p * 300

def huevos_totales(d: int) -> int:
    return d * 350

def bolsas(c: int) -> int:
    return c * 3300

def total(p: int, d: int, c: int) -> int:
    return panes_totales(p) + huevos_totales(d) + bolsas(c)

def vuelto(billete: int, p: int, d: int, c: int) -> int:
    return billete - total(p, d, c)

def debe(billete: int, p: int, d: int, c: int) -> int:
    return total(p, d, c) - billete

if __name__ == "__main__":
    billete = int(input("Valor del billete a pagar: \n"))
    d = int(input("Número de huevos: \n"))
    p = int(input("Número de panes: \n"))
    c = int(input("Número de bolsas de leche: \n"))
    
    if billete in [2000, 5000, 10000, 20000, 50000, 100000]:
        billetes_comerciales = billete
        vuelto_final = vuelto(billete, p, d, c)
        if vuelto_final >= 0:
            print("El vuelto es:", vuelto_final)
        else:
            deber_final = debe(billete, p, d, c)
            print("La persona debe:", deber_final, "pesos adicionales.")
    elif billete != [2000, 5000, 10000, 20000, 50000, 100000]:
         print("No ingreso un billete valido")
    else:
        print("No es un billete real.") 
       