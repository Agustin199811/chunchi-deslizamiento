import pandas as pd

# Cargar el archivo CSV
file_path = "output_data.csv"
data = pd.read_csv(file_path)

# Filtrar la fila correspondiente al "lunes, 01 de marzo de 2021 – 20:02:50 Informe No. 10"
filtro = data["Fecha y Hora de actualización"] == "lunes, 01 de marzo de 2021 – 20:02:50 Informe No. 10"
fila_filtrada = data[filtro]

# Guardar la fila filtrada en un nuevo archivo CSV (opcional)
fila_filtrada.to_csv("fila_filtrada.csv", index=False)

# Mostrar la fila filtrada
print(fila_filtrada)