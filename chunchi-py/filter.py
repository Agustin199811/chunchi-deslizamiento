import pandas as pd

# Cargar el archivo CSV
file_path = "output_data.csv"
data = pd.read_csv(file_path)

# Filtrar la fila correspondiente al "lunes, 01 de marzo de 2021 – 20:02:50 Informe No. 10"
filtro = data["Fecha y Hora de actualización"] == "lunes, 01 de marzo de 2021 – 20:02:50 Informe No. 10"
fila_filtrada = data[filtro]

# Convertir las columnas numéricas a tipo entero (int)
columnas_numericas = [
    "Fallecidos", "Heridos", "Viviendas destruidas", "Bien público afectado",
    "Bien público destruido", "Puentes afectados", "Vías destruidas",
    "Productores afectados por pérdidas agrícolas", "Productores afectados por pérdidas en animales",
    "Viviendas afectadas", "Personas afectadas", "Personas damnificadas",
    "Animales con afectación", "Animales muertos"
]

# Rellenar valores NaN con 0 y convertir a enteros
fila_filtrada[columnas_numericas] = fila_filtrada[columnas_numericas].fillna(0).astype(int)

# Guardar la fila filtrada en un nuevo archivo CSV (opcional)
fila_filtrada.to_csv("fila_filtrada.csv", index=False)

# Mostrar la fila filtrada
print(fila_filtrada)