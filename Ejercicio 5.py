# 5. Manipulación de datos
from Ejercicio_1 import datos
import os

def mostrar_menu_manipulacion():
  while True:
    os.system("cls") # Limpiar pantalla en Windows
    print("1. Crear columna Poder Total y mostrar primeros Pokémon")
    print("2. Ordenar por Poder Total de mayor a menor ")
    print("0. Salir")
    opcion= input("Elige una opción: ")
    
    if opcion == "1":
      # Crear una nueva columna llamada "Poder Total"
      Poder_Total = datos["Ataque"] + datos["Defensa"] + datos["Velocidad"] + datos["PS"]
      datos["Poder_Total] = Poder_Total
      print("\nDataFrame con nueva columna Poder Total:")
      print(datos)
      input("\nPresiona Enter para continuar...")
      
      elif opcion == "2":
          # Ordena el DataFrame por "Poder Total" de mayor a menor
          Orden_Poder_Total = datos.sort_values(by="Poder_Total", ascending=False)
          print("\nPokémon ordenados por Poder Total de mayor a menor:")
          print(Orden_Poder_Total)
          input("\nPresiona Enter para continuar...")
      
    elif opcion == "0":
          break
      
    else:
      print("\Opciónno válida.")
      input("Presiona Enter para continuar...")

#Ejecutar menú
mostrar_menu_manipulacion()
