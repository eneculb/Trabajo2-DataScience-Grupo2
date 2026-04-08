import pandas as pd

df=pd.read_csv("pokemon_primera_gen(sucio).csv")
df_original=df.copy()

df.columns=df.columns.str.strip()
df_original.columns=df_original.columns.str.strip()

columnas_texto=["Nombre", "Tipo 1", "Tipo 2"]
for col in columnas_texto:
    df[col]=df[col].fillna("").astype(str).str.strip()
    df_original[col]=df_original[col].fillna("").astype(str).str.strip()

reemplazos={
    "Eléctrico":"Electrico",
    "Psíquico":"Psiquico",
    "Dragón":"Dragon"
}

df["Tipo 1"]=df["Tipo 1"].replace(reemplazos)
df["Tipo 2"]=df["Tipo 2"].replace(reemplazos)

df_original["Tipo 1"]=df_original["Tipo 1"].replace(reemplazos)
df_original["Tipo 2"]=df_original["Tipo 2"].replace(reemplazos)

tipos_primera_gen=[
    "Normal", "Fuego", "Agua", "Planta", "Electrico",
    "Hielo", "Lucha", "Veneno", "Tierra", "Volador",
    "Psiquico", "Bicho", "Roca", "Fantasma", "Dragon"
]

df["Tipo 1"]=df["Tipo 1"].apply(lambda x: x if x in tipos_primera_gen else "Normal")
df["Tipo 2"]=df["Tipo 2"].apply(lambda x: x if x in tipos_primera_gen else "")

columnas_numericas=["Ataque", "Defensa", "Velocidad", "PS"]
for col in columnas_numericas:
    df[col]=pd.to_numeric(df[col], errors="coerce")

antes=df_original.fillna("").reset_index(drop=True)
despues=df.fillna("").reset_index(drop=True)

filas_cambiadas=antes.ne(despues).any(axis=1)

print("CAMBIOS REALIZADOS:\n")

for i in antes[filas_cambiadas].index:
    numero_pokemon=i+1
    nombre=despues.loc[i, "Nombre"]
    print(f"{numero_pokemon}. {nombre}")

    for columna in antes.columns:
        valor_antes=antes.loc[i, columna]
        valor_despues=despues.loc[i, columna]

        if valor_antes!=valor_despues:
            print(f"   - {columna}: '{valor_antes}' -> '{valor_despues}'")
    print()

repetidos=df[df.duplicated(subset="Nombre", keep=False)]
print("\nPokémon repetidos:")
print(repetidos)

df=df.drop_duplicates(subset="Nombre").reset_index(drop=True)
df.to_csv("pokemon_primera_gen.csv", index=False, encoding="utf-8")

print("\nPokedex limpia creada correctamente.")
print("Archivo original: pokemon_primera_gen(sucio).csv")
print("Archivo limpio: pokemon_primera_gen.csv")
print("")
