#Importando la libreria para graficar
import matplotlib.pyplot as plt
#Importando librería para arrays
import numpy as np


#ayuda
# help(plt.plot)
# help(plt.scatter)
# help(plt.hist)

#Generamos elementos a graficar en X y en Y
anio = [1990,1995,2000,2005,2010]
perros = [1,4,6,5,8]

#Colores
color = ['red','blue','pink','orange','green']

#Título y Etiquetas
xlab = "Años"
ylab = "Perros"
title = "Perros Callejeros por año"

#Tamaño de los puntos
tam = [107,416,639,522,811]
np_tam = np.array(tam)
np_tam = np_tam * 2

#scatter(x-axis) scatter(x-axis,y-axis)  Gráfica de disperción
#s=tamaño de los puntos
#c = color de los puntos puede ser uno o varios
#alpha = opacidad -> 0>opacidad<1 esta entre cero y uno el valor
plt.scatter(anio,perros,s=tam, c=color, alpha = 0.3)

#Agregar título
plt.title(title)

#Agregar Etiquetas de los Ejes
plt.xlabel(xlab)
plt.ylabel(ylab)

#Textos en la grafica
plt.text(1990,1,"Año 1990")
plt.text(1995,4,"Año 1995")
plt.text(2000,6,"Año 2000")
plt.text(2005,5,"Año 2005")
plt.text(2010,8,"Año 2010")

#Colocar cuadricula
plt.grid(True)

#Mostrar la o las gráficas
plt.show()