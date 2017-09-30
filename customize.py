import matplotlib.pyplot as plt

#Generamos elementos a graficar en X y en Y
anio = [1990,1995,2000,2005,2010]
perros = [1,4,6,5,8]

#plot(x-axis) plot(x-axis,y-axis)  Gráfica de lineas
plt.plot(anio,perros)

#Título y Etiquetas
xlab = "Años"
ylab = "Perros"
title = "Perros Callejeros por año"

#Agregar título
plt.title(title)

#Agregar Etiquetas de los Ejes
plt.xlabel(xlab)
plt.ylabel(ylab)

#Etiquetas de la graduación en X
xtick = [1990,1995,2000,2005,2010] #Localización
xval = ["90's","95's","2000's","2005's","2010's"] #Etiquetas

#Etiquetas de la graduación en Y
ytick = [0,2,4,6,8]
yval = ["Cero","Dos","Cuatro","Seis","Ocho"]

#Agregar etiquetas de la graduación
plt.xticks(xtick,xval)
plt.yticks(ytick,yval)

#Mostrar la o las gráficas
plt.show()