from funciones import ordenar_numeros

def introducir():
    a : float = float(input("Piense en un numero y digitelo: \n "))
    b : float = float(input("Digite un numero completo y seguido del dia, mes y año de su nacimiento\nejemplo, dia 19 mes 10 año 2005, numero resultante 19102005: \n "))
    c : float = float(input("Digite su edad sumando el año en el que estamos: \n "))
    d : float = float(input("dteigi un numero re random: \n "))
    e : float = float(input("Preguntele a su amigo un numero mayor a 500 y escribalo: \n "))
    numeros = ordenar_numeros(a,b,c,d,e)
    desarrollo(a,b,c,d,e,numeros)

def promedio(a,b,c,d,e):
    promedio = (a+b+c+d+e)/5
    print(f"Promedio: {promedio}")
    return

def mediana(numeros):
    mediana = numeros[2]
    print(f"Mediana: {mediana}")
    return

def promedio_multiplicativo(a,b,c,d,e):
    promedio_multiplicativo : float = (a*b*c*d*e)/5
    print(f"Promedio multiplicativo: {promedio_multiplicativo}")
    return

def ascendente(numeros):
    print(f"Números de forma ascendente: {numeros}")
    return

def descendente(numeros):
    numeros.sort(reverse=True)
    print(f"Números de forma descendente: {numeros}")
    return

def potencia(numeros):
    potencia : float = (numeros[0])**numeros[-1]
    print(f"Potencia del mayor número elevado al menor número: {potencia}")
    return

def raiz(numeros):
    numero_menor = numeros[4]
    raiz : float = numero_menor ** (1/3)
    print(f"La raiz cúbica del número menor: {raiz}")
    return

def desarrollo(a,b,c,d,e,numeros):
    promedio(a,b,c,d,e)
    promedio_multiplicativo(a,b,c,d,e)
    ascendente(numeros)
    mediana(numeros)
    descendente(numeros)
    potencia(numeros)
    raiz(numeros)
    return
    
def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "_main_":
    print("Ingrese cinco número para realizar determinadas operaciones.")

    while True:
        introducir()
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Estas bien bro?")
            break

def ordenar_numeros(a,b,c,d,e):

    if a < b and a < c and a < d and a < e:
        numeros = [a, 0, 0, 0, 0]
    elif b < a and b < c and b < d and b < e:
        numeros = [b, 0, 0, 0, 0]
    elif c < a and c < b and c < d and c < e:
        numeros = [c, 0, 0, 0, 0]
    elif d < a and d < b and d < c and d < e:
        numeros = [d, 0, 0, 0, 0]
    else:
        numeros = [e, 0, 0, 0, 0]


    if (a <= b and a <= c and a <= d and a <= e) or numeros[0] == a:
        if b <= c and b <= d and b <= e:
            numeros[1] = b
        elif c <= b and c <= d and c <= e:
            numeros[1] = c
        elif d <= b and d <= c and d <= e:
            numeros[1] = d
        else:
            numeros[1] = e
    elif b <= a and b <= c and b <= d and b <= e:
        if a <= c and a <= d and a <= e:
            numeros[1] = a
        elif c <= a and c <= d and c <= e:
            numeros[1] = c
        elif d <= a and d <= c and d <= e:
            numeros[1] = d
        else:
            numeros[1] = e
    elif c <= a and c <= b and c <= d and c <= e:
        if a <= b and a <= d and a <= e:
            numeros[1] = a
        elif b <= a and b <= d and b <= e:
            numeros[1] = b
        elif d <= a and d <= b and d <= e:
            numeros[1] = d
        else:
            numeros[1] = e
    elif d <= a and d <= b and d <= c and d <= e:
        if a <= b and a <= c and a <= e:
            numeros[1] = a
        elif b <= a and b <= c and b <= e:
            numeros[1] = b
        elif c <= a and c <= b and c <= e:
            numeros[1] = c
        else:
            numeros[1] = e
    else:
        if a <= b and a <= c and a <= d:
            numeros[1] = a
        elif b <= a and b <= c and b <= d:
            numeros[1] = b
        elif c <= a and c <= b and c <= d:
            numeros[1] = c
        else:
            numeros[1] = d

    for i in range(2, 5):
        if numeros[i] == 0:
            smallest_remaining = min([num for num in [a, b, c, d, e] if num not in numeros])
            numeros[i] = smallest_remaining

    return numeros

def promedio(a,b,c,d,e):
    promedio = (a+b+c+d+e)/5
    print(f"Promedio: {promedio}")
    return

def mediana(numeros):
    if len(numeros) % 2 == 0:
        mediana : float  = (numeros[len(numeros)//2-1] + numeros[len(numeros)//2])/2
    else:
        mediana = numeros[len(numeros)//2]
    print(f"Mediana: {mediana}")
    return

def promedio_multiplicativo(a,b,c,d,e):
    promedio_multiplicativo : float = (a*b*c*d*e)/5
    print(f"Promedio multiplicativo: {promedio_multiplicativo}")
    return

def ascendente(numeros):
    print(f"Números de forma ascendente: {numeros}")
    return

def descendente(numeros):
    numeros.sort(reverse=True)
    print(f"Números de forma descendente: {numeros}")
    return

def potencia(numeros):
    potencia : float = (numeros[0])**numeros[-1]
    print(f"Potencia del mayor número elevado al menor número: {potencia}")
    return

def raiz(numeros):
    numero_menor = numeros[4]
    raiz : float = numero_menor ** (1/3)
    print(f"La raiz cúbica del número menor: {raiz}")
    return