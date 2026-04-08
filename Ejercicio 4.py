# 4. Visualización de datos

import pandas as pd
import matplotlib.pyplot as plt
datos = pd.read_csv("pokemon_primera_gen.csv")

import seaborn as sns
import os

def mostrar_menu_graficos():
  while True:
    os.system("cls")
    print("1. Histograma de los valores de ataque")
    print("2. Gráficos de dispersión: Ataque vs Velocidad")
    print("3. Boxplot de PS por tipo principal")
    print("4. Distribución de la defensa (Violin Plot)")
    print("0. Salir")
    opcion = input("\nElige una opción: ")
    
    if opcion == "1":
      plt.hist(datos["Ataque"], bins=8, color ="red", edgecolor="black")
      plt.xlabel("Valores de Ataque")
      plt.ylabel("Número de Pokémon")
      plt.title("Histograma dde valores de Ataque ")
      plt.show()
      input("\nPresiona Enter para elegir otra opcion . . .")
      
    elif opcion == "2":
      plt.scatter(datos["Ataque"],  datos["Velocidad"], color="red", alpha=0.85, edgecolor="red")
      plt.xlabel("Ataque")
      plt.ylabel("Velocidad")
      plt.title("Gráfico de dispersión: Ataque vs Velocidad")
      plt.show()
      input("\nPresiona Enter para elegir otra opcion . . .")
      
    elif opcion == "3":
        fig, ax = plt.subplots(figsize=(14,6))
        datos.boxplot(column="PS", by="Tipo 1", ax=ax)
        plt.title("Boxplot de PS por Tipo Principal")
        plt.suptitle("")
        plt.xlabel("Tipo 1")
        plt.ylabel("PS")
        plt.xticks(rotation=45)
        plt.show()
        input("\nPresiona Enter para elegir otra opcion . . .")
      
    elif opcion == "4":
      plt.figure(figsize=(14,6))
      sns.violinplot(x="Tipo 1", y="Defensa", data=datos)
      plt.title("Distribución de la defensa por Tipo Principal (Violin Plot)")
      plt.xlabel("Tipo 1")
      plt.ylabel("Defensa")
      plt.xticks(rotation=45)
      plt.show()
      input("\nPresiona Enter para elegir otra opcion . . .")
      
    elif opcion == "0":
      break
      
    else:
      print("\nOpción no válida.")
      input("\nPresiona Enter para elegir otra opcion . . .")

#Ejecutar menú
mostrar_menu_graficos()
