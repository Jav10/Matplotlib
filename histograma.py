#Importando la libreria para graficar
import matplotlib.pyplot as plt

#ayuda
# help(plt.hist)

#Generamos elementos a graficar (edad de gatos en meses)
gatosEdad = [1.5,3,7,12,2.5,6.8,3.4,8.7,2,7.3,10.2,8.5,9.1,1,3]
#hist(x-axis,binds) eje X y los intervalos que queremos
plt.hist(gatosEdad,3)
#Mostrar la o las gráficas
plt.show()
