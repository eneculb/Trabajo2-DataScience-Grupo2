#5. Manipulación de datos
#-----------------------
#- Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa, velocidad y PS.
#- Ordena el DataFrame por "Poder Total" de mayor a menor.

import pandas as pd

df=pd.read_csv("pokemon_primera_gen.csv")

df["Poder Total"]=df["Ataque"]+df["Defensa"]+df["Velocidad"]+df["PS"]

df_ordenado=df.sort_values(by="Poder Total", ascending=False)

print(df_ordenado)
