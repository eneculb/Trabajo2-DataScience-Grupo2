# 6. Agrupamiento y análisis por grupo
from Ejercicio_1 import datos
import os

def mostrar_menu_agrupamiento():
    while True:
        os.system("cls")  # Limpiar pantalla en Windows
        print("1. Estadísticas de ataque por Tipo 1")
        print("2. Tipo con mayor promedio de velocidad")
        print("3. Pokémon con mayor y menor PS por tipo")
        print("0. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            # Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo principal (Tipo 1)
            estadisticas_ataque = datos.groupby("Tipo 1")["Ataque"].agg(
                Promedio="mean",
                Mediana="median",
                Desviacion_Estandar="std"
            )
            estadisticas_ataque = estadisticas_ataque.astype(int)
            print("\nEstadísticas de Ataque por Tipo 1:")
            print(estadisticas_ataque)
            input("\nPresiona Enter para continuar...")

        elif opcion == "2":
            # ¿Qué tipo tiene el mayor promedio de velocidad?
            prom_vel = datos.groupby("Tipo 1")["Velocidad"].mean()
            tipo_max = prom_vel.idxmax()
            valor_max = int(prom_vel.max()2)
            print(f"\nEl tipo con más promedio de velocidad es: {tipo_max} con un {valor_max}")
            input("\nPresiona Enter para continuar...")

        elif opcion == "3":
            # Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?
            mayor_ps = datos.loc[datos.groupby("Tipo 1")["PS"].idxmax(), ["Tipo 1", "Nombre", "PS"]]
            menor_ps = datos.loc[datos.groupby("Tipo 1")["PS"].idxmin(), ["Tipo 1", "Nombre", "PS"]]

            # Combinar ambos para imprimir lado a lado
            resultado = mayor_ps.set_index("Tipo 1").join(
                menor_ps.set_index("Tipo 1"), lsuffix=" Mayor", rsuffix=" Menor"
            )
            print("\nPokémon con mayor y menor PS por Tipo 1:")
            print(resultado)
            input("\nPresiona Enter para continuar...")

        elif opcion == "0":
            break

        else:
            print("\nOpción no válida.")
            input("Presiona Enter para continuar...")

# Ejecutar menú
mostrar_menu_agrupamiento()
