#Desarrolle una función matemática para calcular el área y el perimetro, cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b y revise como utilizar el valor de pi usando import math y math.pi

import math
def are (a:float, b:float, r:float):
    return (b*a) + 2*(math.pi*r)
def per (a:float, b:float, r:float):
    return (2*(b+a)) + (2*math.pi*r)
if __name__ == "__main__":
    a = float(input("Altura del rectangulo: "))
    b = float(input("Base del rectangulo: "))
    r = float(input("Radio de los dos circulos: "))
area_t = are(a, b, r)
print("El area total del la figura es " + str(area_t) + "")
per_t = per(a, b, r)
print("El perimetro total del la figura es " + str(per_t) + "")