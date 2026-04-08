#7. Análisis exploratorio (EDA)
#------------------------------
#- ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensaJustifica con estadísticas.
#- ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
#- ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)
#- Identifica posibles outliers en los valores de ataque y PS usando boxplots.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

datos=pd.read_csv("pokemon_primera_gen.csv")

def mostrar_menu_eda():
  while True:
    os.system("cls")
    print("1. Tipos con mayor ataque y defensa promedio")
    print("2. Correlación entre ataque y velocidad")
    print("3. Dispersión de los PS dentro de cada tipo")
    print("4. Identificación de posibles outliers en Ataque y PS")
    print("0. Salir")
    opcion=input("\nElige una opción: ")

    if opcion=="1":
        promedios=datos.groupby("Tipo 1")[["Ataque", "Defensa"]].mean()
        print("\nPromedio de ataque y defensa por tipo:\n")
        print(promedios)

        tipo_mayor_ataque=promedios["Ataque"].idxmax()
        tipo_mayor_defensa=promedios["Defensa"].idxmax()

        print("\nRespuesta:")
        print("Sí, existen tipos de Pokémon que tienden a tener mayor ataque o defensa.")
        print("El tipo con mayor promedio de ataque es:", tipo_mayor_ataque)
        print("El tipo con mayor promedio de defensa es:", tipo_mayor_defensa)

        promedios.plot(kind="bar", figsize=(14,6), color=["red", "blue"])
        plt.title("Promedio de Ataque y Defensa por Tipo 1")
        plt.xlabel("Tipo 1")
        plt.ylabel("Promedio")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        input("\nPresiona Enter para elegir otra opcion . . .")

    elif opcion=="2":
        correlacion = datos["Ataque"].corr(datos["Velocidad"])
        print("\nCoeficiente de correlación entre Ataque y Velocidad:", correlacion)

        if correlacion>0:
            print("Sí, hay correlación positiva entre ataque y velocidad.")
        elif correlacion<0:
            print("Sí, hay correlación negativa entre ataque y velocidad.")
        else:
            print("No hay correlación entre ataque y velocidad.")

        input("\nPresiona Enter para elegir otra opcion . . .")

    elif opcion=="3":
      dispersion_ps=datos.groupby("Tipo 1")["PS"].std()
      print("\nDesviación estándar de los PS por tipo:\n")
      print(dispersion_ps.to_string())

      plt.figure(figsize=(14,6))
      dispersion_ps.plot(kind="bar", color="green", edgecolor="black")
      plt.title("Dispersión de los PS por Tipo 1")
      plt.xlabel("Tipo 1")
      plt.ylabel("Desviación estándar de PS")
      plt.xticks(rotation=45)
      plt.tight_layout()
      plt.show()
      input("\nPresiona Enter para elegir otra opcion . . .")

    elif opcion=="4":
        fig, ax= plt.subplots(1, 2, figsize=(12,6))

        datos.boxplot(column="Ataque", ax=ax[0])
        ax[0].set_title("Boxplot de Ataque")
        ax[0].set_ylabel("Ataque")

        datos.boxplot(column="PS", ax=ax[1])
        ax[1].set_title("Boxplot de PS")
        ax[1].set_ylabel("PS")

        plt.suptitle("")
        plt.tight_layout()
        plt.show()

        input("\nPresiona Enter para elegir otra opcion . . .")

    elif opcion=="0":
      break

    else:
      print("\nOpción no válida.")
      input("\nPresiona Enter para elegir otra opcion . . .")

mostrar_menu_eda()
