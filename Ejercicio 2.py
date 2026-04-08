#2. Filtrado y selección
#-----------------------
#- Filtra todos los Pokémon de tipo "Fuego".
#- Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.

import pandas as pd

df=pd.read_csv("pokemon_primera_gen.csv")
fuego=df[df["Tipo 1"]=="Fuego"]
filtro=fuego[["Nombre","Tipo 1","Ataque","Velocidad"]]
print(filtro)
