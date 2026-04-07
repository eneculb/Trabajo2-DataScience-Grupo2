# 7. Análisis exploratorio (EDA)
from Ejercicio_1 import datos
import seaborn as sns
import matplotlib.pyplot as plt
import os

def mostrar_menu_EDA():
    while True:
        os.system("cls")  # Limpiar pantalla en Windows
        print("1. Estadísticas de Ataque y Defensa por Tipo 1")
        print("2. Correlación entre Ataque y Velocidad")
        print("3. Dispersión de PS por tipo")
        print("4. Boxplots de Ataque y PS")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            # ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa?
            Estadisticas = datos.groupby("Tipo 1").agg(
                Promedio_Ataque=("Ataque", "mean"),
                Desviacion_Estandar_Ataque=("Ataque", "std"),
                Promedio_Defensa=("Defensa", "mean"),
                Desviacion_Estandar_Defensa=("Defensa", "std")
            )
            # Redondear y convertir a int
            Estadisticas = Estadisticas.round(0).astype(int)
            print("\nEstadísticas de Ataque y Defensa por Tipo 1:")
            print(Estadisticas)
            input("\nPresiona Enter para continuar...")

        elif opcion == "2":
            # ¿Hay correlación entre ataque y velocidad?
            correlacion = datos["Ataque"].corr(datos["Velocidad"])
            correlacion = round(correlacion, 2)
            print(f"\nCoeficiente de correlación entre Ataque y Velocidad: {correlacion}")
            if correlacion > 0.5:
                print("Hay correlación positiva moderada/alta: Pokémon con mayor ataque tienden a ser más rápidos.")
            elif correlacion < -0.5:
                print("Hay correlación negativa moderada/alta: Pokémon con mayor ataque tienden a ser más lentos.")
            else:
                print("No hay correlación fuerte entre ataque y velocidad.")
            input("\nPresiona Enter para continuar...")

        elif opcion == "3":
            # ¿Qué tan dispersos están los PS dentro de cada tipo?
            dispersion_ps = datos.groupby("Tipo 1")["PS"].std().astype(int)
            print("\nDesviación estándar de PS por tipo:")
            print(dispersion_ps)
            input("\nPresiona Enter para continuar...")

        elif opcion == "4":
            # Identifica posibles outliers en los valores de ataque y PS usando boxplots.
            # Boxplot de Ataque
            plt.figure(figsize=(10,5))
            sns.boxplot(x="Ataque", data=datos)
            plt.title("Boxplot de Ataque")
            plt.show()

            # Boxplot de PS
            plt.figure(figsize=(10,5))
            sns.boxplot(x="PS", data=datos)
            plt.title("Boxplot de PS")
            plt.show()
            input("\nPresiona Enter para continuar...")

        elif opcion == "0":
            break

        else:
            print("\nOpción no válida.")
            input("Presiona Enter para continuar...")

# Ejecutar menú
mostrar_menu_EDA()
