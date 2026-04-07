# 8. Ejercicios de interpretación
from Ejercicio_1 import datos
import os 

def mostrar_menupokemon():
    while True:
        os.system("cls")
          print("1.\n Ver conclusiones del graficos")
          print("2.\n Ver tipo Balanceado y mas especializado")
          print("0.\n Salir")
          opcion = input("Elige una opción: ")
          if opcion == "1":
           print("\nConclusiones sobre los Pokémon de la primera generación:")
           print("- Algunos tipos como Roca tienen mucha defensa pero baja velocidad.")
           print("- Los Pokémon de tipo Normal presentan gran variación en PS.")
           print("- No hay una relación fuerte entre ataque y velocidad.")
      
            input("\nPresiona Enter para continuar...")

          elif opcion == "2":
       
            promedios = datos.groupby("Tipo 1")[["Ataque", "Defensa", "Velocidad", "PS"]].mean()
             variabilidad = promedios.std(axis=1)
            
            balanceado = variabilidad.idxmin()
            especializado = variabilidad.idxmax()
            
            print(f"\nEl tipo de Pokémon más BALANCEADO es: {balanceado}")
            print("  -> Porque sus promedios de Ataque, Defensa, Velocidad y PS son super parecidos entre si.")
            
            print(f"\nEl tipo de Pokémon más ESPECIALIZADO es: {especializado}")
            print("  -> Porque destaca demasiado en una estadistica pero sacrifica las otras (ej: mucha defensa y nada de velocidad).")
            
            input("\nPresiona Enter para continuar...")

          elif opcion == "0":
            break

          else:
            print("\nOpción no valida.")
            input("Presiona Enter para continuar...")

# ejecutar
mostrar_menupokemon()
