# Reto_6

1. Dado la figura de la imagen, desarrolle:
[![68747470733a2f2f692e706f7374696d672e63632f465276436d7078782f696d6167652e706e67.png](https://i.postimg.cc/wBTZYV1F/68747470733a2f2f692e706f7374696d672e63632f465276436d7078782f696d6167652e706e67.png)](https://postimg.cc/HrRBQb47)

* Una función matemática para calcular el volumen y el área superficial.
* Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
* Revise como utilizar el valor de pi usando import math y math.pi

```python

```

2. Dado la figura de la imagen, desarrolle:
[![68747470733a2f2f692e706f7374696d672e63632f3174344d727a734c2f696d6167652e706e67.png](https://i.postimg.cc/jjw6fwmt/68747470733a2f2f692e706f7374696d672e63632f3174344d727a734c2f696d6167652e706e67.png)](https://postimg.cc/wtzs8v9G)

* Una función matemática para calcular el área y el perimetro.  
* Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b. 
* Revise como utilizar el valor de pi usando import math y math.pi

```python

```

3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```python

```

4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```python
billete = int(input("Valor del billete a pagar: \n"))
h = int(input("Número de huevos: \n"))
p = int(input("Número de panes: \n"))
m = int(input("Número de bolsas de leche: \n"))

pan = p * 300
leche = m * 3300
huevos = h * 350
total = pan + leche + huevos
vuelto = billete - total
debe = total - billete
if billete in [2000, 5000, 10000, 20000, 50000, 100000]:
    
    if vuelto >= 0:
        print("El vuelto es:", vuelto)
    else:
        print("La persona debe:", debe, "pesos adicionales.")
else:
    print("No es un billete real.")
```

5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.

```python

```

6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.


```python
d=int(input("Dias que pasaron: "))
c=int(input("Personas  iniciales contaminadas: "))
personas_finales=c*(2**d)
if d>0 and c>0:
  print("Se contaminaron:",personas_finales,"personas en",d,"dias")
else:
  print("No hay dias negativos")
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

8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.


9. Consultar qué es y cómo funciona pip en python.
  

10. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

