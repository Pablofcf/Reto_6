#Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

def masa(n:float,m:float,k:float) -> float:
  return n*6+m*7+k*1
if __name__ == "__main__":
    n=float(input("Cantidad de gallinas: "))
    m=float(input("Cantidad de gallos: "))
    k=float(input("Cantidad de pollitos: "))
    masa_total = masa(n,m,k)
    print("La cantidad o masa total es "+str(masa_total)+" kilogramos")