#5. Manipulación de datos
#-----------------------
#- Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa, velocidad y PS.
#- Ordena el DataFrame por "Poder Total" de mayor a menor.

import pandas as pd

df=pd.read_csv("pokemon_primera_gen.csv")
df["Poder Total"] = df["Ataque"] + df["Defensa"] + df["Velocidad"] + df["PS"]

df_ordenado = df.sort_values(by="Poder Total", ascending=False)
print("\nNUEVA COLUMNA DE PODER TOTAL\n")
print(df_ordenado.to_string())
print("============================================================================================")
print("\nTABLA ORDENADA DE FORMA ASCENDENTE DEL PODER TOTAL\n")
print(df_ordenado[["Nombre", "Tipo 1", "PS", "Ataque", "Defensa", "Velocidad", "Poder Total"]].to_string())
