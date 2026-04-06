import pandas as pd 
from limpiar import limpiar_pokemones
# Limpiar datos
df_limpio = limpiar_pokemones("pokemon_primera_gen.csv", index=Flase)
## 1. Lectura de datos
datos = pd.read_csv("pokemones_primera_gen_limpio.csv")
print(datos)
