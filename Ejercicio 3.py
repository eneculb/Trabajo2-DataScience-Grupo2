#3. Estadística descriptiva básica
#---------------------------------
#- Calcula el promedio, la mediana y la moda del ataque de todos los Pokémon.
#- ¿Cuál es el Pokémon con mayor defensa? ¿Y el de menor velocidad?
#- ¿Cuántos Pokémon tienen dos tipos?
#- Calcula el rango y la desviación estándar de los PS (Puntos de Salud).

import pandas as pd
df=pd.read_csv("pokemon_primera_gen.csv")

promedio_ataque=df["Ataque"].mean()
mediana_ataque=df["Ataque"].median()
moda_ataque=df["Ataque"].mode().values[0]

mayor_defensa=df[df["Defensa"]==df["Defensa"].max()]["Nombre"].values[0]
menor_velocidad=df[df["Velocidad"]==df["Velocidad"].min()]["Nombre"].values[0]

dos_tipos=df["Tipo 2"].notna().sum()

rango_ps=df["PS"].max()-df["PS"].min()
desviacion_estandar_ps=df["PS"].std()

print("\nESTADISTICAS POKEMONES\n")
print("Promedio de ataque:", promedio_ataque)
print("Mediana de ataque:", mediana_ataque)
print("Moda de ataque:", moda_ataque)
print("Pokémon con mayor defensa:", mayor_defensa)
print("Pokémon con menor velocidad:", menor_velocidad)
print("Cantidad de Pokémon con dos tipos:", dos_tipos)
print("Rango de PS:", rango_ps)
print("Desviación estándar de PS:", desviacion_estandar_ps)
print("")
