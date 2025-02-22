
# Proyecto de Extracción de Datos - Chunchi

Este proyecto tiene como objetivo comprender los factores y las consecuencias del deslizamiento de tierra ocurrido en el cantón Chunchi, específicamente en el sector La Armenia, el 12 de febrero de 2021. A través de un análisis detallado, se busca estudiar cómo se produjo este fenómeno natural, sus impactos en la comunidad y el entorno, y qué lecciones se pueden aprender para prevenir futuros.

## Clonar repositorio
```bash
  https://github.com/Agustin199811/chunchi-deslizamiento.git
``` 
## Instrucciones
Este proyecto contiene dos scripts que realizan diferentes tareas de extracción de información:

1. **Scraping de noticias sobre deslizamientos en Chunchi** usando Puppeteer.
2. **Extracción de información de informes del 12 de febrero de 2021**.

### 1. Scraping de Noticias con Puppeteer
Este script busca noticias en Google relacionadas con deslizamientos y aluviones en Chunchi y guarda los datos en formatos JSON y CSV.

#### Tecnologias utilizadas
- Node.js
- Puppeteer
- json2csv

#### Instalación y Uso
1. Instalar dependencias:
```bash
  npm install puppeteer json2csv
``` 
2. Ejecutar el script:
```bash
  node scraping.js
``` 
#### Resultados
Los datos extraídos se guardarán en los archivos chunchi-news.json y chunchi-news.csv en la carpeta data.

### 2. Extracción de Información de Informes
Este script extrae información de varios informes generados el 12 de febrero de 2021.

#### Tecnologias utilizadas
- Python 3.10
- Streamlit
- pdfplumber
- pandas

#### Instalación y Uso
1. Crear un entorno virtual (opcional pero recomendado):
```bash
  python -m venv venv source venv/bin/activate  
  # En Windows usa `venv\Scripts\activate`
``` 
2. Instalar dependencias:
```bash
    pip install -r requirements.txt
``` 
3. Ejecutar el script principal:
```bash
    streamlit run main.py
``` 
#### Resultados
La aplicación de Streamlit se abrirá en tu navegador, donde podrás cargar los informes y ver la información extraída.

## Visualización de Datos con POWER BI
Para visualizar los datos extraídos, puedes importar los archivos chunchi-news.csv y los datos generados por el script de Python en POWER BI.

### Resultados en POWER BI:


## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.

2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).

3. Realiza tus cambios y haz commit (git commit -am 'Añade nueva funcionalidad').

4. Haz push a la rama (git push origin feature/nueva-funcionalidad).

5. Abre un Pull Request.

## Autores

- Polanco Salome
- Rojas Leslie
- Toapanta Patricio

## Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo LICENSE.