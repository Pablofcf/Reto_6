#Desarrolle una función matemática para calcular el volumen y el área superficial, cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h y revise como utilizar el valor de pi usando import math y math.pi
 
import math
def calculo_volumen (r1:float, r2:float, h:float) ->float:
  Volumen = (4/3 * math.pi * r1**3)+((math.pi* r2**2* h)/3)
  return Volumen

def calculo_area_superficial (r1, r2, h) ->float:
  Area = (4*math.pi * r1**2)+((math.pi * r2**2)+(math.pi*r2* ((r2**2 + h**2) **0.5)))
  return Area

if __name__ == "__main__":
  r1 =float(input("Radio de la esfera: "))
  r2 =float(input("Radio del cono: "))
  h =float(input("Altura del cono: "))
  Volumen_figura = calculo_volumen(r1,r2,h)
  Area_superficial = calculo_area_superficial(r1,r2,h)
  print("El volumen es: " + str(Volumen_figura) + ", el area superficial es: " + str(Area_superficial))
