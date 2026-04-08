#6. Agrupamiento y análisis por grupo
#-------------------------------------
#- Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo principal (Tipo 1).
#- ¿Qué tipo tiene el mayor promedio de velocidad?
#- Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?

import pandas as pd

df=pd.read_csv("pokemon_primera_gen.csv")

estadisticas_ataque=df.groupby("Tipo 1")["Ataque"].agg(["mean", "median", "std"])

estadisticas_ataque = df.groupby("Tipo 1")["Ataque"].agg(
    Promedio="mean",
    Mediana="median",
    Desviación_estándar="std"
)

estadisticas_ataque = estadisticas_ataque.rename(
    columns={"Desviación_estándar": "D-E"}
)

promedio_velocidad=df.groupby("Tipo 1")["Velocidad"].mean()
tipo_mas_veloz=promedio_velocidad.idxmax()

mayor_ps=df.loc[df.groupby("Tipo 1")["PS"].idxmax(), ["Tipo 1", "Nombre", "PS"]]
menor_ps=df.loc[df.groupby("Tipo 1")["PS"].idxmin(), ["Tipo 1", "Nombre", "PS"]]

print("\nEstadísticas de ataque del Tipo 1:\n")
print(estadisticas_ataque)

print("\nTipo con mayor promedio de velocidad: " + tipo_mas_veloz)

print("\nPokémon con mayor PS por Tipo 1:\n")
print(mayor_ps)

print("\nPokémon con menor PS por Tipo 1:\n")
print(menor_ps)
print("")
