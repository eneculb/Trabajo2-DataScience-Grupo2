# 4. Visualización de datos
from Ejercicio_1 import datos
import seaborn as sns
import matplotlib.pyplot as plt
import os

def mostrar_menu_graficos():
  while True:
    os.system("cls") # Limpiar pantalla en Windows
    print("1. Histograma de los valores de ataque")
    print("2. Gráficos de dispersión: Ataque vs Velocidad")
    print("3. Boxplot de PS por tipo principal")
    print("4. Distribución de la defensa (Violin Plot)")
    print("0. Salir")
    opcion = input("Elige una opción:")
    
    if opcion == "1":
      # Haz un histograma de los valores de ataque .
      plt.hist(datos["Ataque"], bins=8, color ="red", edgecolor="black")
      plt.xlabel("Valores de Ataque")
      plt.ylabel("Número de Pokémon")
      plt.title("Histograma dde valores de Ataque ")
      plt.show()
      input("\nPresiona Enter para continuar...")
      
    elif opcion == "2":
      #Realiza un gráfico de dispersión entre ataque y velocidad.
      plt.scatter(datos["Ataque"],  datos["Velocidad"], color="red", alpha=0.85, edgecolor="red")
      plt.xlabel("Ataque")
      plt.ylabel("Velocidad")
      plt.title("Gráfico de dispersión: Ataque vs Velocidad")
      plt.show()
      input("\nPresiona Enter para continuar...")
      
    elif opcion == "3":
      # Haz un bLoxpot de los PS por tipo principal (Tipo 1).
      plt.figure(figsize=(14,6)) #Alto y ancho
      datos.boxplot(column="PS", by="Tipo 1")
      plt.title("Boxplot de PS por Tipo Principal")
      plt.suptitle("") # borra título que pandas deja en automatico
      plt.xlabel("Tipo 1")
      plt.ylabel("PS")
      plt.xticks(rotation=45) # inclinación de x
      plt.show()
      input("\nPresiona Enter para continuar...")
      
    elif opcion == "4":
      # Gráfica la distribución de la defensa usando en diagrama de violín. (tipo 1 x y defensa y)
      plt.figure(figsize=(14,6))
      sns.violinplot(x="Tipo 1", y="Defensa", data=datos)
      plt.title("Distribución de la defensa por Tipo Principal (Violin Plot)")
      plt.xlabel("Tipo 1")
      plt.ylabel("Defensa")
      plt.xticks(rotation=45) # inclinamos los nombres de los tipos 
      plt.show()
      input("\nPresiona Enter para continuar...")
      
    elif opcion == "0":
      break
      
    else:
      print("\nOpción no válida.")
      input("Presiona Enter para continuar...")

#Ejecutar menú
mostrar_menu_graficos()
