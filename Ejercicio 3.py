# Estadística descriptiva

from Ejercicio_1 import datos
import os 

def mostrar_menu_estadistica():
  while True:
    os.system("cls") # Limmpiar pantalla en Windows
    print("1. Promedio, mediana y moda del ataque ")
    print("2. Pokémon con mayor defensa y menor velocidad")
    pŕint("3. Pokémon con dos tipos")
    print("4. Rango y desviación estándar de PS")
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
      #Calcular el promedio, la mediana y la moda del ataque de todos los Pokémon.
      Numeros_Ataque = datos["ataque"]
      Promedio = int(Numeros_Ataque.mean().round(0))
      Mediana = int(Numeros_Ataque.median())
      Moda = int(Numeros_.mode().iloc[0])
      print(f"\nEl promedio del ataque de los Pokémon es: {Promedio}")
      print(f"\La mediana del ataque de los Pokémones: {Mediana}")
      print(f"\la Moda del ataqur de los Pokémon es: {Moda}")
      input("\nPresiona Enter para continuar...")
      
    elif opcion == "2":
      #¿Cúal es el Pokémon con mayor defensa? ¿Y ellde menor velocidad?
      #Pokémon con mayor defensa
      Maxima_Defensa = datos["Defensa"].max()
      print("\nPokémon con mayor defensa:")
      print(datos["Defensa"] == Maxima_Defensa][["Nombre", "Defensa"]])
      
      #Pokémon con menor velocidad
      Minima_Velocidad = datos["Velocidad"].min()
      print("\nPokémon con menos velocidad:")
      print(datos[datos["Velocidad"] == Minima_velocidad][["Nombre", "Velocidad"]])
      
      input("\Presiona Enter para continuar...")
      
    elif opcion == "3":
      #¿Cuántos Pokémon tienen dos tipo?
      pokemones_dos_tipos = datos[datos["Tipo 1"].notna() & datoss["Tipo 2"].notna()]
      print("\nPokémon con dos tipos:")
      print(pokemones_dos_tipos[["Nombra", "Tipo 1", "Tipo 2"]])
      print(f"\nCantidad de Pokémon con ambos tipos: {len(pokemones_dos_tipos)}")
      
      input("\nPresiona Enter para continuar...")
      
    elif opcion == "4":
      #Calcula el rango y la desviación estándar de los PS (Puntos de Salud).
      Numero_PS = datos["PS"]
      Rango_PS = Numero_PS.max() - Numero_PS.min()
      Desviacion_estandar = round(Numero_PS.std())
      print(f"\nEl rango de los puntos de salud(PS): {Rango_PS}")
      print(f"\La desviación estándar de los puntos de salud(PS): {Desviación_estandar}")
      input("\nPresiona Enter para continuar...")
      
    elif opcion == "0":
      break
      
    else:
      print("\nOpción no válida.")
      input("Presiona Enter para continuar...")

#Ejecuttar menú
mostrar_menu_estadistica()
      
