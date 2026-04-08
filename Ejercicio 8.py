#8. Ejercicios de interpretación
#-------------------------------
#- Interpreta los resultados de los gráficos y estadísticas: ¿qué conclusiones puedes sacar sobre los Pokémon de la primera generación?
#- ¿Qué tipo de Pokémon sería "más balanceado" según las estadísticas? ¿Y el más especializado?


import pandas as pd
df = pd.read_csv("pokemon_primera_gen.csv")

print("\n¿qué conclusiones puedes sacar sobre los Pokémon de la primera generación?\n")
print("Los pokemon de la primera generación muestran una variedad de tipos con diferentes promedios de ataque y defensa.")
print("Algunos tipos como losde fuego tienden a tener un ataque más alto, mientras que los de agua, pueden tener una defensa más alta.")
print("La relación entre ataque y velocidad es moderada, por ende lo pokemones con mayor ataque no necesariamente son más rápidos.")
print("LOS PS varía entre tipos, indicando los que tienen una mayor variabilidad en sus puntos de salud.")
print("Además, se identificaron algunos atipicos en los valores de ataque y PS, lo que podría indicar que ese pokemon es mucho másfuerte o debil.\n")

print("¿Qué tipo de Pokémon sería 'más balanceado' según las estadísticas? ¿Y el más especializado?\n")

df["Diferencia"] = df[["PS", "Ataque", "Defensa", "Velocidad"]].max(axis=1) - df[["PS", "Ataque", "Defensa", "Velocidad"]].min(axis=1)
balanceado = df.loc[df["Diferencia"].idxmin(), "Nombre"]

especializado = df.loc[df["Diferencia"].idxmax(), "Nombre"]

print("Pokémon más balanceado:", balanceado)
print("Pokémon más especializado:", especializado)
print("")
