from Ejercicio_1 import datos
import os

def mostrar_menu():
  while True:
    os.system("cls") # limpia la pantalla en Windows 
    print("1. Mostrar Pokémones tipo Fuego")    
    print("2. Mostrar columnas seleccionadas")
    print("0. Salir")
    opcion = input("Elegir una opción: ")
    
    if opcion == "1":
      print("\nPokemones tipo FUEGO")
      ### Filtrar todos los Pokémon de tipo "Fuego".
     fuego= datos[datos["Tipo 1"]]= = "Fuego"
      print(f"Cantidad de Pokémon tipo fuego: {len(fuego)}")
      print(fuego)
      ####
      input("\nPresiona Enter para continuar...")
    elif opcion == "2":
      print("\nSolo las columnas Nombre, Tipo 1, Ataque y Velocidad")
      ####Seleciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.
      print(datos[["Nombre", "Tipo 1", "Ataque", "Velocidad"]])
      ######
      input("\nPresiona Enter para continuar...")
    elif opcion == "0":
      break
    else:
      print("\nOpción no valida.")
      input("Presiona Enter para continuar...")

mostrar_menu()
