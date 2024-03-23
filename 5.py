#Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

c: int
ti: float  # tasa de interes (en porcentaje)
t: int  # tiempo

def interes(c: int, ti: float) -> float:
    return c * (ti / 100)  # Convertimos la tasa de interés a porcentaje

def valor_final(c: int, ti: float, t: int) -> float:
    return c * (1 + interes(c, ti)) ** t

if __name__ == "_main_":
    c = int(input("Ingrese el capital del préstamo: "))
    ti = float(input("Ingrese la tasa de interés  sin el signo %): "))
    t = int(input("Ingrese el tiempo en meses: "))
    print("Este es el interés compuesto:", valor_final(c, ti, t))