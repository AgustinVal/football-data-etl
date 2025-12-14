
# Test Football

## Descripción Test

Este proyecto implementa un pipeline de datos que extrae información desde la API pública de Football-Data.org, transforma los datos, los carga en una base de datos PostgreSQL dentro de un entorno completamente contenedor, para luego generar un resumen en formato CSV como output.

El proyecto sigue una estructura modular basada en un pipeline ETL simplificado:

```
src/
 ├── extract/       → Extracción de datos desde la API
 ├── transform/     → Transformación y creación de Tablas
 ├── load/          → Insertar datos en PostgreSQL
 ├── export/        → Consulta pedida exportada como CSV
```

## Pasos para la ejecución

### 1. Requisitos previos

- Docker 
- Git
- API Key válida de Football-Data.org

Python y PostgreSQL se instalan localmente en el contenedor.

### 2. Configurar variables de entorno

```
API_KEY=tu_api_key
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=football_db
```

### 3. Construir y ejecutar los contenedores

```docker compose up --build ```


## Flujo del Pipeline

### Parte Zero

Se utilizó Docker para garantizar la ejecución del pipeline sin necesitar de otras instalaciones. Para ello se separaron los servicios en postgres y pipeline. Para una mayor eficiencia se realizó todo el montaje dentro de la carpeta del proyecto evitando tener mayores puertos que el por defecto.

### Parte 1

Los Endpoints son:

- https://api.football-data.org/v4/competitions
- https://api.football-data.org/v4/competitions/{id}/teams

Los datos extraídos incluyen:
- Lista de competiciones
- Lista de equipos para cada competición

Además para la descarga de datos se implemento un manejo de rate limits en caso de existir muchas peticiones. Para ello se utilizó time.sleep() con el fin de evitar el error 429.

### Parte 2

Se guardan archivos JSON en la carpeta data con el fin de mantener la trazabilidad del pipeline, es decir, tener un historial entre difentes ejecuciones y evaluar posibles errores:

- data/competitions/competition.json
- data/teams/{competition_id}.json

### Parte 3.1

Se crearon tres tablas:

- dim_teams
- dim_competitions
- fact_competitions

Se utilizó SQLAlchemy para mayor escabilidad junto con claridad en el código. Además se cuido detalles como evitar duplicados y dejar explicitas las llaves primarias en cada tabla.

### Parte 3.2

Utilizando pandas junto a la consulta pedida, se exporta el archivo output.csv dentro de la carpeta outputs, el cual contiene la siguiente información:

```
competition,num_teams
Copa Libertadores,47
UEFA Champions League,36
European Championship,24
Championship,24
Primera Division,20
Serie A,20
Premier League,20
Campeonato Brasileiro Série A,20
Eredivisie,18
Ligue 1,18
Bundesliga,18
Primeira Liga,18
FIFA World Cup,13
```

## Estructura de carpetas final

```
football_test/
|
├── docker-compose.yml
├── Dockerfile
├── .env
├── .gitgnore
├── requirements.txt
├── outputs/
│   └── output.csv
│
├── data/
│   └── competitions/
│       └── competitions.json
│   └── teams/
│           ├── id1.json
│           ├── id2.json
│           └── ...
│
└── src/
    ├── extract/
    ├── transform/
    ├── load/
    └── export/
```

## Observaciones

El resultado obtenido en el output.csv es similar pero no igual al expuesto en el enunciado del test, donde efectivamente se encuentran las mismas 13 competencias pero varian el número de teams en algunas de ellas.



## Mejoras Futuras

Estos son algunos de los siguientes pasos que deberían hacerse al escalar el proyecto en un entorno real

- Validar y limpiar datos erroneos o nulos a traves de procesamiento de lenguaje natural y controles de calidad.
- Incorporar tests automáticos.
- Agregar cache y control de rate limits para mejorar eficiencia de descarga.
- Agregar más manejo de errores y sistema de reintentos para fallos de la API.
- Automatizar el pipeline con un algún orquestador.



















