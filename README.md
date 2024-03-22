# Reto_6

1. Dado la figura de la imagen, desarrolle:
[![68747470733a2f2f692e706f7374696d672e63632f465276436d7078782f696d6167652e706e67.png](https://i.postimg.cc/wBTZYV1F/68747470733a2f2f692e706f7374696d672e63632f465276436d7078782f696d6167652e706e67.png)](https://postimg.cc/HrRBQb47)

* Una función matemática para calcular el volumen y el área superficial.
* Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
* Revise como utilizar el valor de pi usando import math y math.pi

```python
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
```
Valor de pi en math
```python
import math
x =math.pi
print(x)
# 3.1415...
```

2. Dado la figura de la imagen, desarrolle:
[![68747470733a2f2f692e706f7374696d672e63632f3174344d727a734c2f696d6167652e706e67.png](https://i.postimg.cc/jjw6fwmt/68747470733a2f2f692e706f7374696d672e63632f3174344d727a734c2f696d6167652e706e67.png)](https://postimg.cc/wtzs8v9G)

* Una función matemática para calcular el área y el perimetro.  
* Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b. 
* Revise como utilizar el valor de pi usando import math y math.pi

```python
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
```

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python
def masa(n:float,m:float,k:float) -> float:
  return n*6+m*7+k*1
if __name__ == "__main__":
    n=float(input("Cantidad de gallinas: "))
    m=float(input("Cantidad de gallos: "))
    k=float(input("Cantidad de pollitos: "))
    masa_total = masa(n,m,k)
    print("La cantidad o masa total es "+str(masa_total)+" kilogramos")
```

4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
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
```

5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

```python

```

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.


```python
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
```

7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

* El promedio  
* La mediana  
* El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
* Ordenar los números de forma ascendente
* Ordenar los números de forma descendente
* La potencia del mayor número elevado al menor número
* La raíz cúbica del menor número

```python

```

9. Consultar qué es y cómo funciona pip en python.

pip es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python. Muchos paquetes pueden ser encontrados en el Python Package Index (PyPI). pip es un acrónimo recursivo que se puede interpretar como Pip Instalador de Paquetes o Pip Instalador de Python. Una característica particular de pip es que permite gestionar listas de paquetes y sus números de versión correspondientes a través de un archivo de requisitos. Esto nos permite una recreación eficaz de un conjunto de paquetes en un entorno separado (p. ej. otro ordenador) o entorno virtual. 

10. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

* Colecciones
* CSV
* Aleatorio
* Tkinter
* Solicitudes
* BeautifulSopa4
* Numpy
* pandas
* matplotlib
* TensorFlow
* Keras
* Scikitt-Aprende
* Django
* Frasco

<h2>Bibliografía</h2>
    <div class="bibliografia">
        <table>
          <tr>
                <td>Hafeezul Kareem Shaik. 14 bibliotecas y módulos de Python que todo desarrollador debería conocer. Recuperado de https://geekflare.com/es/popular-python-libraries-modules/<a href="https://geekflare.com/es/popular-python-libraries-modules/"></a></td>
            </tr> 
          <tr>
                <td>Wikipedia. (2024). Pip (administrador de paquetes). Recuperado de (https://es.wikipedia.org/wiki/Pip_(administrador_de_paquetes))<a href="(https://es.wikipedia.org/wiki/Pip_(administrador_de_paquetes))"></a></td>
          </tr>            
        </table>
    </div>
