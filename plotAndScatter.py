#Importando la libreria para graficar
import matplotlib.pyplot as plt

#ayuda
# help(plt.plot)
# help(plt.scatter)
# help(plt.hist)

#Generamos elementos a graficar en X y en Y
anio = [1990,1995,2000,2005,2010]
perros = [1,4,6,5,8]

#plot(x-axis) plot(x-axis,y-axis)  Gráfica de lineas
plt.plot(anio,perros)
#scatter(x-axis) scatter(x-axis,y-axis)  Gráfica de disperción
plt.scatter(anio,perros)
#Mostrar la o las gráficas
plt.show()
